import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


hobby = st.selectbox("Tags : ",
                     ["Question", "Review", "Templates", "Stylus problems"])
agree = st.checkbox('Show Analysis by tags')
 
def get_data(path):
  data = pd.read_csv(path)
  df_full_data = data.sort_values(by=['score'],ascending=False)
  return df_full_data


def get_monthly_threads_by_tag(df, tag):
  df['created'] =  pd.to_datetime(df['created'])
  df["Created"] = df["created"].dt.strftime('%Y-%m')
  # data["month"] = data['created'].dt.month
  new_df = df[df["tag"] == tag]
  return new_df.filter(["submission_id", "tag", "created", "submission_title", "reply_body", "score"], axis = 1)

def line_chart_for_tag(df, tag):
  df['created'] =  pd.to_datetime(df['created'])
  df["Created"] = df["created"].dt.strftime('%Y-%m')
  # data["month"] = data['created'].dt.month
  new_df = df[df["tag"] == tag]
  test_df = new_df.groupby(["tag", "Created"]).count()
  test_df.reset_index(level=["tag", "Created"], inplace = True)
  test_df = test_df.sort_values(by=['score'],ascending=False)
  return test_df

def line_chart_for_data(df):
  df['created'] =  pd.to_datetime(df['created'])
  df["Created"] = df["created"].dt.strftime('%Y-%m')
  # data["month"] = data['created'].dt.month
  full_dataframe = df.groupby(["tag", "Created"]).count()
  full_dataframe.reset_index(level=["tag", "Created"], inplace = True)
  full_dataframe = full_dataframe.sort_values(by=['score'],ascending=False)
  return full_dataframe

def gen_wordcloud(dataframe):
  df = dataframe
  tokens = [[token for token in sentence] for sentence in df["reply_body"].apply(eval)]
  # Flatten the list of lists to create a single list of all tokens
  flattend_token = [token for sentence in tokens for token in sentence]
  wc = WordCloud(background_color='black', colormap = 'binary', width = 800, height = 500, max_words = 100, stopwords=STOPWORDS)
  wordcloud_image = wc.generate_from_text(' '.join(flattend_token))
  fig, ax = plt.subplots(figsize = (12, 8))
  ax.imshow(wordcloud_image, interpolation = "bilinear")
  plt.axis("off")
  st.pyplot(fig)

data = get_data("tagged_threads.csv")


if agree == True:
  st.markdown("# Subreddit Threads Dashboard")
#   tags_data = data.query(f"tag == '{hobby}'")
  st.markdown("## Thread mentioning GoodNotein other competitor Subreddit")
  st.dataframe(get_monthly_threads_by_tag(data, str(hobby)))
  st.markdown("## Tag-Level Monthly Threads")
  st.line_chart(line_chart_for_tag(data, str(hobby)), x = "Created", y = "submission_id", color = "tag")
  st.markdown("## Tag-Level Word Cloud from Thread Title")
  gen_wordcloud(get_monthly_threads_by_tag(data, "Question"))
else:
  data = get_data("tagged_threads.csv")
  st.markdown("# Subreddit Threads Dashboard")
  st.markdown("## Thread mentioning GoodNotein other competitor Subreddit")
  st.dataframe(data)
  st.markdown("## Tag-Level Monthly Threads")
  st.line_chart(line_chart_for_data(data), x = "Created", y = "submission_id", color = "tag")
  st.markdown("## Tag-Level Word Cloud from Thread Title")
  gen_wordcloud(data)
