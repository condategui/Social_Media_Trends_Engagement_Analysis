import streamlit as st

def machine_learning_section():
    st.title("Machine Learning")
    
    st.markdown("""
    The machine learning model was trained using the cleaned data to predict the engagement of a post. 
    The model used was a Random Forest Regressor, which is a supervised learning algorithm that uses ensemble learning 
    to build a model. The model was trained using the following features:
    
    - **Platform**: The social media platform where the post was published.
    - **Type**: The type of content of the post.
    - **Hashtags**: The hashtags used in the post.
    - **Region**: The region where the post was published.
    - **Date**: The date when the post was published.
    
    The model was evaluated using the Mean Absolute Error (MAE) metric, which measures the average absolute difference 
    between the predicted and actual engagement values. The model achieved a MAE of 0.5, which indicates that the model 
    is accurate in predicting the engagement of a post.
    """)
    
    st.markdown("""
    The model was deployed as a web application using Streamlit, a Python library that allows you to create interactive 
    web applications with simple Python scripts. The web application allows users to input the features of a post and 
    get the predicted engagement value. The web application is hosted on Heroku, a cloud platform that allows you to deploy 
    web applications easily.
    """)
    
    st.markdown("""
    The web application can be accessed [here](https://social-media-trends-engagement.herokuapp.com/).
    """)
    
    st.markdown("""
    The code for the machine learning model can be found [here]""")