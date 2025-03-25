import streamlit as st  

def home_page():
    st.title("Welcome to the Social Media Trends Engagement Analysis")
    st.markdown(
        """
        This application is a dashboard that allows you to analyze the engagement of social media trends. 
        You can navigate through the different sections using the sidebar on the left. 
        The data used in this application is a dataset of viral social media trends. 
        """
    )
    st.markdown(
        """
        The dataset contains the following columns:
        - `id`: The unique identifier of the trend.
        - `platform`: The social media platform where the trend was posted.
        - `post_date`: The date when the trend was posted.
        - `post_time`: The time when the trend was posted.
        - `content_type`: The type of content of the trend (e.g., image, video, text).
        - `hashtags`: The hashtags used in the trend.
        - `likes`: The number of likes of the trend.
        - `shares`: The number of shares of the trend.
        - `comments`: The number of comments of the trend.
        - `engagement`: The engagement of the trend (i.e., the sum of likes, shares, and comments).
        - `region`: The region where the trend was posted.
        """
    )
    st.markdown(
        """
        The sidebar on the left allows you to navigate through the different sections of the application:
        - `🏠 Home Page`: The welcome page of the application.
        - `📱 Platforms`: The analysis of the engagement by social media platform.
        - `#️⃣ Hashtags`: The analysis of the engagement by hashtags.
        - `🤳🏻 Content Type`: The analysis of the engagement by content type.
        - `🌍 Regions`: The analysis of the engagement by region.
        - `📊 PowerBI`: The PowerBI report of the trends.
        - `🤖 Machine Learning`: The machine learning model to predict the engagement.
        - `🔎 Conclusions`: The conclusions of the analysis.
        """
    )
    st.markdown(
        """
        The data used in this application is a dataset of viral social media trends. 
        You can download the dataset from [this link](https://www.kaggle.com/datasnaek/youtube-new).
        """
    )

    st.markdown(
        """
        The source code of this application
        is available on [GitHub]""")