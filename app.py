import streamlit as st
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


from components.header import render_header
from footer import render_footer
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
    .css-18e3th9 {
        background-color: #000000;
        color: white;
    }
    .css-1d391kg, .css-1d391kg div {
        background-color: #000000;
        color: white;
    }
    .stButton > button {
        color: white;
    }
    .stButton > button:nth-of-type(1) {
        background-color: #d04243;
    }
    .stButton > button:hover {
        background-color: #f4a259;
    }
    h1, h2, h3, h4, h5, h6, p, div {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True)

@st.cache_data
def load_data():
    try:
        cleaned_data = pd.read_csv('data/social_media_dataset.csv')
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
        st.sidebar.image("img/logo.png", width=300)
        st.sidebar.title("Menu")
        
        # Define the components with their icons and functions
        components = {
            "🏠 Home Page": home_page,
            "📱 Platforms": platforms_section,
            "#️⃣ Hashtags": hashtags_section,
            "📷 Content Type": content_type_section,
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
        
        st.sidebar.markdown("---")
        st.sidebar.markdown("""
        “If you torture the data long enough, it will confess.”
        
        Ronald Coase """)
        
        # Display the selected page
        components[st.session_state.current_page]()
        
        render_footer()
    else:
        st.error("Failed to load data. Please check the data files.")

if __name__ == "__main__":
    main()