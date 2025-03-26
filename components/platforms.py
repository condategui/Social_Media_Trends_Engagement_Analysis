import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static

#from components.functions import (count_plot, bar_chart, pie_chart, violin_plot, box_plot, scatter_plot, count_plot_swapped)


def platforms_section():
    st.title("📱 Platforms")

    st.markdown("""
    In this section, we will analyze the most popular platforms in the dataset. 
    We will start by looking at the number of posts per platform and then we will 
    analyze the engagement metrics for each platform.
    """)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(['🔎 Overview', '📷 Instagram', '⚡️ TikTok', '📺 YouTube', '🐥 Twitter'])
    
    # Load the data
    cleaned_data = pd.read_csv('data/social_media_dataset.csv')
    
    # Custom color palette
    palette = ['#d04243', '#BBDB90', '#d0c2f7', '#f4a259', '#A5D9E3', '#CF6679']
    
    with tab1:
        st.subheader("Engagement Metrics Overview")
        
        # Calculate average engagement metrics per platform
        metrics = cleaned_data.groupby('Platform').agg({
            'Likes': 'mean',
            'Comments': 'mean',
            'Shares': 'mean',
            'Views': 'mean', 
            'Impressions': 'mean'
        }).reset_index()
        
        # Calculate engagement rate
        metrics['Engagement Rate'] = ((metrics['Likes'] + metrics['Comments'] + metrics['Shares']) / metrics['Views']) * 100
        
        # Convert engagement rate to percentage string
        metrics['Engagement Rate'] = metrics['Engagement Rate'].apply(lambda x: f"{x:.2f}%")
        
        # Format numbers with comma separators and two decimals
        metrics['Likes'] = metrics['Likes'].apply(lambda x: f"{x:,.2f}")
        metrics['Comments'] = metrics['Comments'].apply(lambda x: f"{x:,.2f}")
        metrics['Shares'] = metrics['Shares'].apply(lambda x: f"{x:,.2f}")
        metrics['Views'] = metrics['Views'].apply(lambda x: f"{x:,.2f}")
        metrics['Impressions'] = metrics['Impressions'].apply(lambda x: f"{x:,.2f}")
        
        # Rearrange columns
        metrics = metrics[['Platform', 'Engagement Rate', 'Likes', 'Comments', 'Shares', 'Views', 'Impressions']]
        
        # Set the table style to center text
        styled_metrics = metrics.style.set_table_styles(
            [{'selector': 'td', 'props': [('text-align', 'center')]},
            {'selector': 'th', 'props': [('text-align', 'center')]}]
        )
        
        # Display the table
        st.table(styled_metrics)
        
        st.markdown(""" 
        - **Engagement Rate**: The percentage of users who engaged with the post (likes, comments, shares) out of the total views.
        - **TikTok**: The platform with the highest engagement rate.
        """)
        
        st.markdown("---")
    
    
    
    
    with tab2:
        st.markdown("""
        # Instagram
        Instagram is primarily used for sharing visual content such as photos, videos, and stories.
        Users interact with posts through likes, comments, and sharing content via direct messages.
        The platform also supports features like Stories and Reels, which are short, engaging video clips.
        
        Instagram's algorithm favors visually appealing content that quickly captures attention.
        The most viral content on Instagram tends to be high-quality images, lifestyle content, and short, catchy videos, particularly Reels, which often include trending music and challenges.
        """)
        
        
        graph1 = px.bar(cleaned_data[cleaned_data['Platform'] == 'Instagram'].groupby('Content_Type')['Views'].sum().reset_index(),
                    x='Content_Type', y='Views', 
                    title='Instagram Views by Content Type',
                    labels={'Views': 'Total Views', 'Content_Type': 'Content Type'},
                    color='Content_Type', color_discrete_sequence=palette)
        
        # Update layout for better readability
        graph1.update_layout(xaxis_title='Content Type', yaxis_title='Total Views',
                        xaxis={'categoryorder':'total descending'})
        st.plotly_chart(graph1)
        
        st.markdown("""
        
        """)
    
    
    
    
    
    
    with tab3:
        st.write("TikTok specific analysis goes here.")
    
    
    
    
    
    
    with tab4:
        st.write("YouTube specific analysis goes here.")
    
    
    
    
    
    
    with tab5:
        st.write("Twitter specific analysis goes here.")