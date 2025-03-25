import streamlit as st

def render_header():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.empty()  # This is just to balance the columns
    
    with col2:
        # Título de la aplicación
        st.markdown("<h1 style='text-align: center;'>Social Media Trends and Engagement Analysis</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'> - Trust the Data - </h3>", unsafe_allow_html=True)
    
    with col3:
        st.empty()  # This is just to balance the columns
    
    # Línea divisoria
    st.markdown("---")