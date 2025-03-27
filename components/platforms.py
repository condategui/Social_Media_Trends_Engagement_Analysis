import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static

def platforms_section():
    st.title("📱 Platforms")

    st.markdown("""
    In this section, we will analyze the most popular platforms in the dataset. 
    We will start by looking at the number of posts per platform and then we will 
    analyze the engagement metrics for each platform.
    """)
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['🔎 Overview', '📷 Instagram', '⚡️ TikTok', '👤 Facebook', '🐥 Twitter', '🚀Take Aways'])
    
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
        Instagram has been evolving over the years, with new features like Stories, Reels so right now the content that is better working are videos (Reels), but the users keep posting Photos and Carrousels (more than one photo on the same post).
        """)
        
        graph11 = px.bar(cleaned_data[cleaned_data['Platform'] == 'Instagram'].groupby('Content_Type')['Engagement_Rate'].mean().reset_index(),
                    x='Content_Type', y='Engagement_Rate', 
                    title='Instagram Engagement Rate by Content Type',
                    labels={'Engagement_Rate': 'Engagement Rate', 'Content_Type': 'Content Type'},
                    color='Content_Type', color_discrete_sequence=palette)
        
        # Update layout for better readability
        graph11.update_layout(xaxis_title='Content Type', yaxis_title='Engagement Rate',
                        xaxis={'categoryorder':'total descending'}, yaxis_range=[0.25, 0.30])
        st.plotly_chart(graph11)
        
        st.markdown("""
        The engagement rate on Instagram is higher for photos than for videos.
        
        Views not always correlate with engagement. The engagement rate is a more reliable metric for assessing content performance.
        """)
        
        graph2 = px.pie(cleaned_data[cleaned_data['Platform'] == 'Instagram'].groupby('Hashtag')['Views'].sum().reset_index(),
                    names='Hashtag', values='Views', 
                    title='Instagram Views by Hashtag',
                    labels={'Views': 'Total Views', 'Hashtag': 'Hashtag'},
                    color_discrete_sequence=palette)
        
        # Update layout for better readability
        graph2.update_layout(xaxis_title='Hashtag', yaxis_title='Total Views',
                        xaxis={'categoryorder':'total descending'})
        st.plotly_chart(graph2)
        
        st.markdown("""
        Here you can see that the Hashtags / Topics are distributed in a similar across all the posts. This is becuase the company wanted to have consistency in the topics they were posting about.
        """)
    
    with tab3:
        st.markdown("""
        # TikTok
        TikTok is a short-form video platform known for its viral content, creative challenges, 
        and engaging, quick-to-consume videos. The platform primarily focuses on entertainment, 
        trends, and user-generated content.
        """)
        
        graph3 = px.bar(cleaned_data[cleaned_data['Platform'] == 'TikTok'].groupby('Content_Type')['Views'].sum().reset_index(),
                    x='Content_Type', y='Views', 
                    title='TikTok Views by Content Type',
                    labels={'Views': 'Total Views', 'Content_Type': 'Content Type'},
                    color='Content_Type', color_discrete_sequence=palette)
        
        # Update layout for better readability
        graph3.update_layout(xaxis_title='Content Type', yaxis_title='Total Views',
                        xaxis={'categoryorder':'total descending'})
        st.plotly_chart(graph3)
        
        st.markdown("""
        TikTok's content strategy revolves around short, engaging videos that capture users' 
        attention quickly, within the first 3 seconds. 
        """)
        
        graph33 = px.bar(cleaned_data[cleaned_data['Platform'] == 'TikTok'].groupby('Content_Type')['Engagement_Rate'].mean().reset_index(),
                    x='Content_Type', y='Engagement_Rate', 
                    title='Instagram Engagement Rate by Content Type',
                    labels={'Engagement_Rate': 'Engagement Rate', 'Content_Type': 'Content Type'},
                    color='Content_Type', color_discrete_sequence=palette)
        
        # Update layout for better readability
        graph33.update_layout(xaxis_title='Content Type', yaxis_title='Engagement Rate',
                        xaxis={'categoryorder':'total descending'}, yaxis_range=[0.25, 0.30])
        st.plotly_chart(graph33)
        
        st.markdown("""
        The engagement rate on TikTok is higher for videos than for photos.
        The platform's algorithm favors engaging, high-quality video content,
        which can lead to higher visibility and interaction rates.
        """)
        
        graph4 = px.pie(cleaned_data[cleaned_data['Platform'] == 'TikTok'].groupby('Hashtag')['Views'].sum().reset_index(),
                    names='Hashtag', values='Views', 
                    title='TikTok Views by Hashtag',
                    labels={'Views': 'Total Views', 'Hashtag': 'Hashtag'},
                    color_discrete_sequence=palette)
        
        # Update layout for better readability
        graph4.update_layout(xaxis_title='Hashtag', yaxis_title='Total Views',
                        xaxis={'categoryorder':'total descending'})
        st.plotly_chart(graph4)
        
        st.markdown("""
        The distribution of hashtags demonstrates a consistent approach to content 
        categorization and topic selection across TikTok posts, as well as on the other platforms.
        """)
    
    with tab4:
        st.markdown("""
        # Facebook
        Facebook is a long-form video platform that supports a wide variety of content. 
        The platform allows for more in-depth content, 
        with creators able to produce longer, more detailed videos.
        """)
        
        graph5 = px.bar(cleaned_data[cleaned_data['Platform'] == 'Facebook'].groupby('Content_Type')['Views'].sum().reset_index(),
                    x='Content_Type', y='Views', 
                    title='Facebook Views by Content Type',
                    labels={'Views': 'Total Views', 'Content_Type': 'Content Type'},
                    color='Content_Type', color_discrete_sequence=palette)
        
        # Update layout for better readability
        graph5.update_layout(xaxis_title='Content Type', yaxis_title='Total Views',
                        xaxis={'categoryorder':'total descending'}, yaxis_range=[50000000, 64000000])
        st.plotly_chart(graph5)
        
        st.markdown("""
        Facebook offers versatility in content types, only Text and Photo posts are the ones that get more views.
        """)
        
        graph55 = px.bar(cleaned_data[cleaned_data['Platform'] == 'Facebook'].groupby('Content_Type')['Engagement_Rate'].mean().reset_index(),
                    x='Content_Type', y='Engagement_Rate', 
                    title='Instagram Engagement Rate by Content Type',
                    labels={'Engagement_Rate': 'Engagement Rate', 'Content_Type': 'Content Type'},
                    color='Content_Type', color_discrete_sequence=palette)
        
        # Update layout for better readability
        graph55.update_layout(xaxis_title='Content Type', yaxis_title='Engagement Rate',
                        xaxis={'categoryorder':'total descending'}, yaxis_range=[0.25, 0.30])
        st.plotly_chart(graph55)
        
        st.markdown("""
        Carrousels and Photo posts are the most popular content type on Facebook with higher engagement rates.
        Only Text posts are the least popular content type since users prefer to interact with dynamic content.
        """)
        
        graph6 = px.pie(cleaned_data[cleaned_data['Platform'] == 'Facebook'].groupby('Hashtag')['Views'].sum().reset_index(),
                    names='Hashtag', values='Views', 
                    title='Facebook Views by Hashtag',
                    labels={'Views': 'Total Views', 'Hashtag': 'Hashtag'},
                    color_discrete_sequence=palette)
        
        # Update layout for better readability
        graph6.update_layout(xaxis_title='Hashtag', yaxis_title='Total Views',
                        xaxis={'categoryorder':'total descending'})
        st.plotly_chart(graph6)
        
        st.markdown("""
        The hashtag distribution reflects a strategic approach to content 
        categorization and topic consistency across Facebook posts.
        """)
    
    with tab5:
        st.markdown("""
        # Twitter (X)
        Twitter, now known as X, is a microblogging and social networking platform 
        known for real-time, concise communication and trending topics.
        
        The platform emphasizes short-form text content, but also supports images, 
        videos, and links, making it a versatile communication tool.
        """)
        
        graph7 = px.bar(cleaned_data[cleaned_data['Platform'] == 'Twitter'].groupby('Content_Type')['Views'].sum().reset_index(),
                    x='Content_Type', y='Views', 
                    title='Twitter Views by Content Type',
                    labels={'Views': 'Total Views', 'Content_Type': 'Content Type'},
                    color='Content_Type', color_discrete_sequence=palette)
        
        # Update layout for better readability
        graph7.update_layout(xaxis_title='Content Type', yaxis_title='Total Views',
                        xaxis={'categoryorder':'total descending'}, yaxis_range=[50000000, 64000000])
        st.plotly_chart(graph7)
        
        st.markdown("""
        Plain tweets are the most popular content type on Twitter, Videos are the least popular since users prefer to watch videos on other platforms.
        """)
        
        graph77 = px.bar(cleaned_data[cleaned_data['Platform'] == 'Twitter'].groupby('Content_Type')['Engagement_Rate'].mean().reset_index(),
                    x='Content_Type', y='Engagement_Rate', 
                    title='Instagram Engagement Rate by Content Type',
                    labels={'Engagement_Rate': 'Engagement Rate', 'Content_Type': 'Content Type'},
                    color='Content_Type', color_discrete_sequence=palette)
        
        # Update layout for better readability
        graph77.update_layout(xaxis_title='Content Type', yaxis_title='Engagement Rate',
                        xaxis={'categoryorder':'total descending'}, yaxis_range=[0.25, 0.30])
        st.plotly_chart(graph77)
        
        st.markdown("""
        Posts with images and videos have a higher engagement rate than plain text posts. Users are more likely to interact with visually appealing content.
        """)
        
        graph8 = px.pie(cleaned_data[cleaned_data['Platform'] == 'Twitter'].groupby('Hashtag')['Views'].sum().reset_index(),
                    names='Hashtag', values='Views', 
                    title='Twitter Views by Hashtag',
                    labels={'Views': 'Total Views', 'Hashtag': 'Hashtag'},
                    color_discrete_sequence=palette)
        
        # Update layout for better readability
        graph8.update_layout(xaxis_title='Hashtag', yaxis_title='Total Views',
                        xaxis={'categoryorder':'total descending'})
        st.plotly_chart(graph8)
        
        st.markdown("""
        The hashtag distribution shows a consistent approach to content 
        categorization across Twitter posts.
        """)
    
    with tab6:
        st.markdown("""
        # Take Aways
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
.instagram {
background-color: rgba(208, 66, 67, 0.5);
}
.tiktok {
background-color: rgba(187, 219, 144, 0.5);
}
.facebook {
background-color: rgba(208, 194, 247, 0.5);
}
.twitter {
background-color: rgba(244, 162, 89, 0.5);
}
</style>

<table>
<tr>
<th></th>
<th class="instagram">Instagram</th>
<th class="tiktok">TikTok</th>
<th class="facebook">Facebook</th>
<th class="twitter">Twitter</th>
</tr>
<tr>
<td>Audience</td>
<td class="instagram">Millennials, Gen Z, 18-34, B2C</td>
<td class="tiktok">Gen Z and younger Millennials, 16-24, viral content consumers, B2C</td>
<td class="facebook">Baby Boomers, Gen X, and older Millennials, 25-55, family-oriented, community groups, B2C and B2B</td>
<td class="twitter">Professionals, 22-45, opinion leaders, B2C</td>
</tr>
<tr>
<td>Content Type</td>
<td class="instagram">Photos, Reels, Stories, Carousels. Aesthetic visual content and Influencer marketing</td>
<td class="tiktok">Short-form videos, Challenges, Trending dance/music clips, Memes, Quick tutorials</td>
<td class="facebook">Long-form posts, Photo albums, Videos, Event invitations and Community discussions</td>
<td class="twitter">Text updates, News links, Short videos and Real-time commentary</td>
</tr>
<tr>
<td>Tone</td>
<td class="instagram">Curated, Polished, Aspirational, Lifestyle-focused, Visually compelling</td>
<td class="tiktok">Authentic, Energetic, Playful, Spontaneous, Trend-driven</td>
<td class="facebook">Conversational, Personal, Community-oriented, Informative, Diverse</td>
<td class="twitter">Direct, Opinionated, Concise, Current-events focused</td>
</tr>
<tr>
<td>Frequency</td>
<td class="instagram">3-5 posts per week, consistent aesthetic, High-quality content</td>
<td class="tiktok">1-3 posts daily, Rapid content creation, Trend responsiveness</td>
<td class="facebook">1-2 posts per week, less frequent but more substantial</td>
<td class="twitter">Multiple posts daily, real-time engagement, quick turnaround</td>
</tr>
</table>
    """, unsafe_allow_html=True)