import streamlit as st
import pandas as pd


def platforms_section():
    st.title("📱 Platforms")

    st.markdown("""
    In this section, we will analyze the most popular platforms in the dataset. 
    We will start by looking at the number of posts per platform and then we will 
    analyze the engagement metrics for each platform.
    """)

    st.markdown("---")

    st.subheader("Number of Posts per Platform")

    # Group the data by platform and count the number of posts
    posts_per_platform = pd.DataFrame(cleaned_data['Platform'].value_counts()).reset_index()
    posts_per_platform.columns = ['Platform', 'Number of Posts']

    st.write(posts_per_platform)

    st.markdown("---")

    st.subheader("Engagement Metrics per Platform")

    # Group the data by platform and calculate the mean engagement metrics
    engagement_per_platform = cleaned_data.groupby('Platform').mean().reset_index()

    st.write(engagement_per_platform)

    st.markdown("---")

    st.subheader("Engagement Metrics Distribution per Platform")

    # Create a boxplot to visualize the distribution of engagement metrics per platform
    st.write("Average Engagement Metrics per Platform")
    st.write(engagement_per_platform)

    st.markdown("---")

    st.subheader("Platform Distribution")

    # Create a pie chart to visualize the distribution of posts per platform
    st.write("Number of Posts per Platform")
    st.write(posts_per_platform)

    st.markdown("---")