import streamlit as st
import pandas as pd
import plotly.express as px

def content_type_section():
    st.title("📷 Content Type Analysis")

    st.markdown("""
    In this section, we will dive deep into the different content types across various social media platforms. 
    We'll explore how different types of content perform and their characteristics.
    """)
    
    # Create tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['🔎 Overview', '🎥 Video', '📸 Photo', '🎠 Carrousel', '📝 Text', '🚀 Takeaways'])
    
    # Load the data
    cleaned_data = pd.read_csv('data/social_media_dataset.csv')
    
    # Custom color palette
    palette = ['#d04243', '#BBDB90', '#d0c2f7', '#f4a259', '#A5D9E3', '#CF6679']
    
    with tab1:
        st.subheader("Content Type Metrics Overview")
        
        # Calculate average metrics per content type
        metrics = cleaned_data.groupby('Content_Type').agg({
            'Engagement_Rate': 'mean',
            'Likes': 'mean',
            'Comments': 'mean',
            'Shares': 'mean',
            'Views': 'mean', 
            'Impressions': 'mean'
        }).reset_index()
        
        # Convert engagement rate to percentage string
        metrics['Engagement_Rate'] = metrics['Engagement_Rate'].apply(lambda x: f"{x*100:.2f}%")
        
        # Format numbers with comma separators and two decimals
        metrics['Likes'] = metrics['Likes'].apply(lambda x: f"{x:,.2f}")
        metrics['Comments'] = metrics['Comments'].apply(lambda x: f"{x:,.2f}")
        metrics['Shares'] = metrics['Shares'].apply(lambda x: f"{x:,.2f}")
        metrics['Views'] = metrics['Views'].apply(lambda x: f"{x:,.2f}")
        metrics['Impressions'] = metrics['Impressions'].apply(lambda x: f"{x:,.2f}")
        
        # Rearrange columns
        metrics = metrics[['Content_Type', 'Engagement_Rate', 'Likes', 'Comments', 'Shares', 'Views', 'Impressions']]
        
        # Set the table style to center text
        styled_metrics = metrics.style.set_table_styles(
            [{'selector': 'td', 'props': [('text-align', 'center')]},
            {'selector': 'th', 'props': [('text-align', 'center')]}]
        )
        
        # Display the table
        st.table(styled_metrics)
        
        st.markdown(""" 
        - **Engagement Rate**: The percentage of users who engaged with the post (likes, comments, shares) out of the total views.
        - **Videos**: Posts that contain video content get a higher engagement rate compared to other content types.
        """)
        
        st.markdown("---")
    
    with tab2:
        st.markdown("""
        # Video Content
        Videos have become a dominant form of content across social media platforms. 
        They offer dynamic, engaging ways to communicate messages, tell stories, and capture audience attention.
        """)
        
        # Platform distribution for Video content
        graph1 = px.bar(cleaned_data[cleaned_data['Content_Type'] == 'Video'].groupby('Platform')['Engagement_Rate'].mean().reset_index(),
                    x='Platform', y='Engagement_Rate', 
                    title='Video Engagement Rate by Platform',
                    labels={'Engagement_rate': 'Engagement Rate', 'Platform': 'Platform'},
                    color='Platform', color_discrete_sequence=palette)
        
        graph1.update_layout(xaxis_title='Platform', yaxis_title='Engagement Rate', yaxis_range=[0.0, 0.28])
        st.plotly_chart(graph1)
        
        st.markdown("""
        - **Facebook**: offers longer, more in-depth content.
        - **Instagram**: Reels and Stories provide quick, engaging clips.
        - **TikTok**: focuses on short, viral videos.
        - **Twitter**: videos are often used to complement text posts.
        """)
    
    with tab3:
        st.markdown("""
        # Photo Content
        Photos remain a crucial content type, especially on visually-driven platforms. 
        They provide quick, impactful ways to communicate messages and tell stories.
        """)
        
        # Platform distribution for Photo content
        graph3 = px.bar(cleaned_data[cleaned_data['Content_Type'] == 'Photo'].groupby('Platform')['Engagement_Rate'].mean().reset_index(),
                    x='Platform', y='Engagement_Rate', 
                    title='Photo Engagement Rate by Platform',
                    labels={'Engagement_Rate': 'Engagement Rate', 'Platform': 'Platform'},
                    color='Platform', color_discrete_sequence=palette)
        
        graph3.update_layout(xaxis_title='Platform', yaxis_title='Engagement Rate', yaxis_range=[0.0, 0.30])
        st.plotly_chart(graph3)
        
        st.markdown("""
        - **Facebook**: also sees significant photo engagement.
        - **Instagram**: audience keeps engaging with photo posts.
        - **TikTok**: has a smaller focus on photos, with more emphasis on videos since the algorithm favors video content.
        - **Twitter**: photos are used to complement text posts.
        """)
    
    with tab4:
        st.markdown("""
        # Carrousel Content
        Carousels offer a multi-image storytelling format, allowing for more comprehensive content presentation.
        """)
        
        # Platform distribution for Carousel content
        graph5 = px.bar(cleaned_data[cleaned_data['Content_Type'] == 'Carrousel'].groupby('Platform')['Engagement_Rate'].mean().reset_index(),
                    x='Platform', y='Engagement_Rate', 
                    title='Carousel Engagement Rate by Platform',
                    labels={'Engagement_Rate': 'Engagement Rates', 'Platform': 'Platform'},
                    color='Platform', color_discrete_sequence=palette)
        
        graph5.update_layout(xaxis_title='Platform', yaxis_title='Engagement Rate', yaxis_range=[0.0, 0.29])
        st.plotly_chart(graph5)
        
        st.markdown("""
        - **Facebook**: gets the higger engagement rate since the audience tends to spend more time scrolling through multiple images (compared to ther content type).
        - **Instagram**: Carousels are a popular format, allowing users to swipe through multiple images or videos.
        - **Twitter**: Carousels get a great engagement rate.
        """)
    
    with tab5:
        st.markdown("""
        Text-based posts provide direct communication, allowing for detailed explanations and commentary.
        """)
        
        # Platform distribution for Text content
        graph7 = px.bar(cleaned_data[cleaned_data['Content_Type'] == 'Text'].groupby('Platform')['Engagement_Rate'].mean().reset_index(),
                    x='Platform', y='Engagement_Rate', 
                    title='Text Engagement Rate by Platform',
                    labels={'Engagement_Rate': 'Engagement Rate', 'Platform': 'Platform'},
                    color='Platform', color_discrete_sequence=palette)
        
        graph7.update_layout(xaxis_title='Platform', yaxis_title='Engagement Rate')
        st.plotly_chart(graph7)
        
        st.markdown("""
        - **Facebook**: text posts are often used for announcements and discussions.
        - **Twitter**: text posts are the primary format, with a focus on brevity and immediacy.
        """)

    with tab6:
        st.markdown("""
        # Content Type Takeaways
        """)
        
        st.markdown("""
    <style>
table {
width: 100%;
border-collapse: collapse;
}
th, td {
border: 1px solid #000000;
padding: 8px;
text-align: center;
}
th {
background-color: #000000;
color: white;
text-align: center;
}
.video {
background-color: rgba(208, 66, 67, 0.5);
}
.photo {
background-color: rgba(187, 219, 144, 0.5);
}
.carousel {
background-color: rgba(208, 194, 247, 0.5);
}
.text {
background-color: rgba(244, 162, 89, 0.5);
}
</style>

<table>
<tr>
<th></th>
<th class="video">Video</th>
<th class="photo">Photo</th>
<th class="carousel">Carousel</th>
<th class="text">Text</th>
</tr>
<tr>
<td>Best Platform</td>
<td class="video">TikTok, Instagram</td>
<td class="photo">Instagram, Facebook, Twitter</td>
<td class="carousel">Instagram, Facebook, Twitter</td>
<td class="text">Twitter, Facebook</td>
</tr>
<tr>
<td>Engagement</td>
<td class="video">High (especially short-form)</td>
<td class="photo">Moderate to High</td>
<td class="carousel">Less than Photos</td>
<td class="text">Moderate</td>
</tr>
<tr>
<td>Content Strategy</td>
<td class="video">Quick, entertaining, trend-driven</td>
<td class="photo">Aesthetic, storytelling, brand showcase</td>
<td class="carousel">Storytelling</td>
<td class="text">Informative</td>
</tr>
<tr>
<td>Average Length</td>
<td class="video">7-60 seconds</td>
<td class="photo">Single image/graphic design</td>
<td class="carousel">Multiple images (2-20)</td>
<td class="text">Short to medium (280 chars)</td>
</tr>
</table>
    """, unsafe_allow_html=True)
