import streamlit as st
import plotly.express as px
import pandas as pd

def ov_section():
    st.title("⚖️ Other Variables")

    st.markdown("""
    Social media is a complex ecosystem where multiple factors intersect to determine content performance, audience engagement, and communication effectiveness.
    
    This section breaks down a bit more in depth other variables that influence social media strategies.
    """)

    # Create tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(['🔎 Overview', '📌 Topic', '🌎 Region', '👥 Audience', '💼 Business'])

    # Custom color palette
    palette = ['#d04243', '#BBDB90', '#d0c2f7', '#f4a259', '#A5D9E3', '#CF6679']

    # Load the data
    cleaned_data = pd.read_csv('data/social_media_dataset.csv')

    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            st.header("🚀 Strategies for Better Engagement")
            st.markdown("""
1. **Post Timing Matters:** Analyze when your audience is most active and schedule posts accordingly.
2. **Content Format Optimization:** Use a mix of images, videos, carousels, and text posts for maximum reach.
3. **Hashtag Strategy:** Utilize relevant hashtags to improve content discoverability and engagement.
4. **Community Interaction:** Respond to comments, participate in discussions, and engage with your followers.
5. **Data-Driven Decisions:** Regularly analyze metrics such as reach, engagement, and conversion rates to optimize strategy.
6. **Consistency is Key:** Maintain a regular posting schedule to keep your audience engaged and algorithm-favored.
7. **Collaboration & Influencer Marketing:** Partner with influencers or brands to expand reach and credibility.
8. **Call-to-Action (CTA):** Encourage users to interact with your content through clear CTAs (e.g., “Comment below,” “Share this post”).
9. **A/B Testing:** Experiment with different headlines, visuals, and captions to determine what resonates best with your audience.
10. **Leverage User-Generated Content:** Encourage followers to create and share content related to your brand.
            """)
            
            st.success("📌 Apply these insights to optimize your social media presence and boost engagement!")
        
        with col2:
            st.image("img/sm.jpg", width=700, caption="Social Media Connections")

    with tab2:
        st.markdown("# Topic")
        
        # Hashtag Analysis Visualization
        st.subheader("Hashtag Impact Analysis")
        
        # Total views by hashtag
        hashtag_views = cleaned_data.groupby('Hashtag')['Views'].sum().reset_index()
        
        graph1 = px.bar(hashtag_views, 
                        x='Hashtag', 
                        y='Views', 
                        title='Total Views by Hashtag',
                        labels={'Views': 'Total Views', 'Hashtag': 'Hashtag'},
                        color='Hashtag',
                        color_discrete_sequence=palette)
        
        st.plotly_chart(graph1)
        
        st.markdown("""
        ### Hashtag Strategies
        
        Hashtags are powerful tools for:
        - Content Categorization
        - Increasing Discoverability
        - Joining Trending Conversations
        - Building Community

        #### Best Practices:
        1. Use Relevant and Specific Hashtags
        2. Research Trending Topics
        3. Create Branded Hashtags
        4. Limit to 3-5 Hashtags per Post
        """)

    with tab3:
        st.markdown("# Region")
        
        st.markdown("""
        ## Regional Variations in Social Media Usage
        
        Social media platforms are used differently across regions due to:
        - Cultural Norms
        - Local Trends
        - Internet Accessibility
        - Regulatory Environments
        """)
        
        # Regional Comparison Table
        region_data = {
            'Region': ['North America', 'Europe', 'Asia', 'Latin America', 'Middle East', 'Africa'],
            'Most Popular Platform': ['Facebook/Instagram', 'Instagram/TikTok', 'WeChat/TikTok', 'WhatsApp/Instagram', 'Instagram/Twitter', 'WhatsApp/Facebook'],
            'Content Preference': ['Professional/Lifestyle', 'Short-form Video', 'Local Platforms', 'Messaging-based', 'News/Political', 'Community-driven'],
            'Engagement Style': ['Analytical', 'Creative', 'Mobile-first', 'Social Commerce', 'Opinion-driven', 'Community Support']
        }
        
        region_df = pd.DataFrame(region_data)
        st.table(region_df)

    with tab4:
        st.markdown("# Audience")
        
        st.markdown("""
        ## Audience Segmentation Strategies
        
        Different platforms attract distinct audience segments:
        
        ### Professional Platforms
        - LinkedIn: Career, B2B, Professional Networking
        - Primarily 25-45 age group
        - Focus: Professional achievements, industry insights
        
        ### Creative Platforms
        - Instagram: Visual storytelling, lifestyle
        - TikTok: Entertainment, trends
        - Primarily 16-34 age group
        - Focus: Personal branding, creativity
        
        ### Community Platforms
        - Facebook: Family, community groups
        - Reddit: Niche interests, discussions
        - Broader age range
        - Focus: In-depth conversations
        """)
        
        # Audience Pie Chart
        st.subheader("Audience Distribution")
        audience_data = {
            'Platform': ['Instagram', 'TikTok', 'Facebook', 'LinkedIn', 'Twitter'],
            'Audience Share': [30, 25, 20, 15, 10]
        }
        
        graph2 = px.pie(values=audience_data['Audience Share'], 
                        names=audience_data['Platform'], 
                        title='Social Media Platform Audience Share')
        st.plotly_chart(graph2)

    with tab5:
        st.markdown("# Business Communication")
        
        st.markdown("""
        ## Business Communication Strategies by Platform
        
        ### B2B Communication
        - LinkedIn: Professional, data-driven content
        - Twitter: Thought leadership, industry news
        - Focus: Expertise, credibility, networking
        
        ### B2C Communication
        - Instagram: Visual storytelling, product showcase
        - TikTok: Trendy, authentic content
        - Facebook: Community engagement
        - Focus: Emotional connection, brand personality
        
        ### Key Differences
        - Tone
        - Content Type
        - Engagement Metrics
        - Target Audience
        """)
        
        # B2B vs B2C Comparison
        comparison_data = {
            'Aspect': ['Communication Tone', 'Content Length', 'Visual Style', 'Engagement Goal'],
            'B2B': ['Professional', 'Detailed', 'Data-driven', 'Lead Generation'],
            'B2C': ['Conversational', 'Concise', 'Emotional', 'Brand Loyalty']
        }
        
        comparison_df = pd.DataFrame(comparison_data)
        st.table(comparison_df)

# Note: This function would be called in your main Streamlit app file