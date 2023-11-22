# Streamlit-Subreddit-Visualization

## Project Overview
This project utilizes Streamlit for data visualization purposes. The main functionalities include creating a DataFrame, displaying it in a Streamlit app, generating a line graph for all tags, and creating a WordCloud. The app allows users to interact with the data through a dropdown menu for different tags and checkboxes to customize the displayed visualizations.

### Features
#### DataFrame Display:
The project initializes a DataFrame and showcases it on the Streamlit app.
![DataFrame](https://github.com/highplainscomputing/Streamlit-Subreddit-Visualization/blob/main/Demo%20(2).png)

#### Line Graph:
A line graph is generated to visualize data trends for all tags.
![Line Graph](https://github.com/highplainscomputing/Streamlit-Subreddit-Visualization/blob/main/Demo%20(1).png)

#### WordCloud:
The project incorporates a WordCloud to provide a visually appealing representation of the dataset.
![WordCloud](https://github.com/highplainscomputing/Streamlit-Subreddit-Visualization/blob/main/Demo%20(3).png)

#### Tag Filtering:
Users can interact with the app using a dropdown menu to select different tags.
Checkboxes enable users to toggle the display of the DataFrame, line graph, and WordCloud for the selected tag.
![Checkbox](https://github.com/highplainscomputing/Streamlit-Subreddit-Visualization/blob/main/Demo%20(4).png)

## Setup Instructions
### Virtual Environment
Create a virtual environment (optional but recommended):
```bash
python -m venv myenv
```
Activate the virtual environment:
On Windows:
```bash
myvenv\Scripts\activate
```
On macOS/Linux:
```bash
source myvenv/bin/activate
```
### Requirements Installation
Install the required packages using the provided requirements.txt file:
```bash
pip install -r requirements.txt
```
### Running the Streamlit App
To run the Streamlit app, execute the following command in the terminal:
```bash
streamlit run app.py
```

## Usage
After running the app, a web page will open in your default browser.
Use the dropdown menu to select different tags.
Toggle checkboxes to show/hide the DataFrame, line graph, and WordCloud for the selected tag.
If no checkboxes are selected, the visualizations will be displayed for the entire dataset.
Feel free to explore and interact with the visualizations to gain insights from the data!

Note: Ensure that your virtual environment is activated while running the Streamlit app.

