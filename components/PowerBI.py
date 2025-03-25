import streamlit as st

def BI_section():
    st.title("PowerBI")
    st.markdown(
        """
        <iframe width="100%" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiNzY5MzIzZjItZmQ4Zi00YzYzLWI2MzItZjE4ZjYwYjM2MzIyIiwidCI6IjQwM2U5MmE5LWY2ZjUtNDFjYi1hZjIwLWY2MjYwMjUyYjYyZiIsImMiOjN9" frameborder="0" allowFullScreen="true"></iframe>
        """,
        unsafe_allow_html=True
    )