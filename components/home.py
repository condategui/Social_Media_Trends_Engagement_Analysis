import streamlit as st  

def home_page():
    st.header("📱 Project Overview")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        Welcome to my **Social Media Trends Engagement Analysis** dashboard!
        
        This project represents the culmination of my Data Analysis and AI BootCamp journey.
        
        As a Social Media Manager, I've created this interactive tool to demonstrate how data analysis is crucial for understanding platform performance and audience engagement patterns. Through visualizations and metrics, we'll explore what drives successful content across various social platforms.
        
        The custom dataset used in this analysis combines real-world data from previous projects, providing authentic insights into social media performance metrics.
        """)
    
    with col2:
        st.info("""
        **Key Benefits:**
        - Identify top-performing content types
        - Compare engagement across platforms
        - Understand audience preferences
        - Optimize posting strategies
        - Make data-driven social media decisions
        """)
    
    # Dataset description
    st.header("📊 Dataset Information")
    
    st.markdown("""
    The analysis is based on a comprehensive dataset containing social media performance metrics across multiple platforms. Each entry represents a specific social media post with the following attributes:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        - **`id`**: Unique identifier for each post
        - **`platform`**: Social media platform (Facebook, Instagram, Twitter and TikTok)
        - **`content_type`**: Format of the content (image, video, text and carrousel)
        - **`likes`**: Number of likes/reactions received
        - **`shares`**: Number of times the content was shared
        """)
    
    with col2:
        st.markdown("""
        - **`comments`**: Number of comments on the post
        - **`engagement_rate`**: percentage of users who engaged with the post (likes, comments, shares) out of the total views
        - **`views`**: Number of content views
        - **`impressions`**: Total number of times content was displayed
        """)
    
    # Dashboard navigation
    st.header("🧭 Dashboard Navigation")
    
    st.markdown("""
    Explore different aspects of social media performance through these dedicated sections:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        - **🏠 Home Page**: Overview and introduction
        - **📱 Platforms**: Platform-specific engagement analysis
        - **🤳 Content Type**: Performance by content format
        """)
    
    with col2:
        st.markdown("""
        - **#️⃣ Other Variables**: Additional engagement factors
        - **📊 PowerBI**: Interactive PowerBI reports
        - **🔎 Conclusions**: Key findings and recommendations
        """)
    
    # Call to action
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.success("""
        ### Ready to explore social media insights?
        
        Use the sidebar to navigate through different sections of the analysis and discover 
        what drives engagement across platforms.
        """)
    
    # Resources and links
    st.markdown("---")
    
    st.header("📚 Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Dataset Source
        The dataset used in this analysis is available for download at:
        [GitHub - Clàudia Ondategui](https://github.com/condategui/Social_Media_Trends_Engagement_Analysis/tree/main/data)
        
        *Note: The original dataset has been modified for the purposes of this analysis.*
        """)
    
    with col2:
        st.markdown("""
        ### Project Repository
        View the complete source code and additional resources on GitHub:
        [GitHub Repository](https://github.com/condategui/Social_Media_Trends_Engagement_Analysis)
        
        Feel free to star the repository if you find this analysis helpful!
        """)