import streamlit as st

def BI_section():
    st.title("PowerBI")
    st.markdown(
        """
        <iframe width="100%" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiZWU2ZDY3NjktMTQ1Ni00MTFiLTllZGEtMDVjOGU3ZWYzM2NiIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>
        """,
        unsafe_allow_html=True
    )