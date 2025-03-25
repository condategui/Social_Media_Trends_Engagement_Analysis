import streamlit as st
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


from components.header import render_header
from components.footer import render_footer
from components.home import home_page
from components.platforms import platforms_section
from components.hashtags import hashtags_section
from components.content_type import content_type_section
from components.regions import regions_section
from components.machine_learning import machine_learning_section
from components.PowerBI import BI_section
from components.conclusions import conclusions_section

st.set_page_config(
    page_title="📊 Social Media Trends Engagement Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS for a black background, button colors, and white text
st.markdown(
    """
    <style>
    .reportview-container {
        background: #000000;
        color: white;
    }
    .sidebar .sidebar-content {
        background: #000000;
        color: white;
    }
    .stButton > button {
        color: white;
    }
    .stButton > button:nth-of-type(1) {
        background-color: #d04243;
    }
    .stButton > button:nth-of-type(2) {
        background-color: #BBDB90;
    }
    .stButton > button:nth-of-type(3) {
        background-color: #d0c2f7;
    }
    .stButton > button:nth-of-type(4) {
        background-color: #f4a259;
    }
    .stButton > button:nth-of-type(5) {
        background-color: #A5D9E3;
    }
    .stButton > button:nth-of-type(6) {
        background-color: #CF6679;
    }
    .stButton > button:nth-of-type(7) {
        background-color: #d04243;
    }
    .stButton > button:nth-of-type(8) {
        background-color: #BBDB90;
    }
    .stButton > button:hover {
        filter: brightness(1.2);
    }
    .stTitle, .stHeader {
        color: #A5D9E3;
    }
    .stMarkdown > div {
        color: #CF6679;
    }
    </style>
    """,
    unsafe_allow_html=True
)

@st.cache_data
def load_data():
    try:
        cleaned_data = pd.read_csv('data/Viral_Social_Media_Trends_Cleaned.csv')
        return cleaned_data
    except FileNotFoundError as e:
        st.error(f"Error: {e}")
        return None, None
    except pd.errors.EmptyDataError as e:
        st.error(f"Error: {e}")
        return None, None
    except pd.errors.ParserError as e:
        st.error(f"Error: {e}")
        return None, None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None, None


def main():
    render_header()
    cleaned_data = load_data() # Unpack the tuple returned by load_data
    
    if cleaned_data is not None:
        st.sidebar.title("Menu")
        
        # Define the components with their icons and functions
        components = {
            "🏠 Home Page": home_page,
            "📱 Platforms": platforms_section,
            "#️⃣ Hashtags": hashtags_section,
            "🤳🏻 Content Type": content_type_section,
            "🌍 Regions": regions_section,
            "📊 PowerBI": BI_section,
            "🤖 Machine Learning": machine_learning_section,
            "🔎 Conclusions": conclusions_section
        }
        
        # Store the current page in session state if it doesn't exist yet
        if 'current_page' not in st.session_state:
            st.session_state.current_page = "🏠 Home Page"
        
        # Create a button for each page
        for page_name in components.keys():
            if st.sidebar.button(page_name, key=page_name):
                st.session_state.current_page = page_name
        
        # Display the selected page
        components[st.session_state.current_page]()
        
        render_footer()
    else:
        st.error("Failed to load data. Please check the data files.")

if __name__ == "__main__":
    main()