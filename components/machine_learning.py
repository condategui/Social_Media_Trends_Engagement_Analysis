import streamlit as st
import pandas as pd

def machine_learning_section():
    st.title("Why Machine Learning May Not Be Suitable for Social Media Project")
    st.markdown("""
This analysis examines the limitations of applying various machine learning approaches to social media data
and explains why these approaches may not meet our project requirements.
""")

# Create tabs with Summary first, followed by the other tabs
    tab_summary, tab1, tab2 = st.tabs(["Summary", "Data Challenges", "Model Limitations"])

    # New Tab: Summary Table
    with tab_summary:
        st.header("Summary of Key Points")
        
        col12, col13 = st.columns(2)
        
        with col12:
            st.markdown("""
        ## Data Challenges
        
        - High Variability
        - Trend Volatility
        - Platform Differences
        - Predicting Virality
            """)
        
        with col13:
            st.markdown("""
        ## Model Limitations
        
        - Emotional Response
        - Human psychology
        - Short Shelf-Life
        - Cultural Context
            """)

# Tab 1: Data Challenges
    with tab1:
        st.header("Data Challenges in Social Media Analysis")
    
        st.subheader("1. High Variability and Non-Stationarity")
        st.markdown("""
    - **Platform Algorithm Changes**: Social platforms frequently modify their algorithms, causing sudden shifts in content distribution patterns
    - **Trend Volatility**: Viral trends emerge and fade rapidly, often within days or hours
    - **Seasonal Effects**: Content performance varies based on time of day, day of week, and seasonal events
        """)
    
        st.subheader("2. Data Sparsity and Cold Start Problems")
        st.markdown("""
    - **Incomplete Features**: Many posts lack sufficient engagement metrics for reliable prediction
    - **New Content Types**: Novel content formats (e.g., new AR features) have no historical data
    - **Platform Differences**: Metrics from one platform cannot reliably transfer to another
        """)
    
        st.subheader("3. Feature Interdependence and Leakage")
        st.markdown("""
    - **Predicting Engagement Rate**: Using impressions, views, likes as features creates circular prediction
    - **Content Popularity**: Similar metrics are both inputs and outcomes
    - **Predicting Virality**: Early engagement metrics often directly determine virality
        """)

# Tab 2: Model Limitations
    with tab2:
        st.header("Model Limitations")
    
        st.subheader("1. Oversimplification of Complex Phenomena")
        st.markdown("""
        - **Cultural Context**: Content performance is heavily influenced by cultural context and current events
    - **Emotional Response**: Emotional reactions drive engagement but are difficult to quantify
    - **Network Effects**: Content spreads through complex social networks with cascade effects
        """)
    
        st.subheader("2. Temporal Relevance and Model Decay")
        st.markdown("""
    - **Short Shelf-Life**: Models trained on historical data quickly become irrelevant
    - **Continuous Retraining Needed**: Requires constant model updates and retraining
    - **Shifting Baselines**: What constitutes "good" engagement changes over time
        """)