import streamlit as st

def render_header():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        # Logo de la aplicación
        st.image("img/logo.png", width=100)
    
    with col2:
        # Título de la aplicación
        st.markdown("<h1 style='text-align: center;'>Social Media in Data</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Trends Engagement Analysis</h3>", unsafe_allow_html=True)
    
    with col3:
        st.empty()  # This is just to balance the columns
    
    # Línea divisoria
    st.markdown("---")