import streamlit as st

def render_footer():
    
    st.markdown('<hr style="border:5px solid ##F4A259">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.image("img/logo.png", width=300)
        
    with col2:
        
        st.markdown("""
                <div style='text-align: center; color: #666;'>
            <p>Developed by Clàudia Ondategui, Social Media and Data Analyst.</p>
            <p>Visit my 
               <a href="https://github.com/condategui">GitHub.</a> to discover more projects or check my
                <a href="https://www.linkedin.com/in/claudia-ondategui/">LinkedIn</a> page.
            </p>
        </div>
        """,
        unsafe_allow_html=True
        )
        
    with col3:
        st.empty()