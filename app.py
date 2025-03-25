import streamlit as st
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


from components.header import render_header
from components.footer import render_footer
from pages.home import home_page
from pages.platforms import platforms_section
from pages.hashtags import hashtags_section
from pages.content_type import content_type_section
from pages.regions import regions_section
from pages.machine_learning import machine_learning_section
from pages.PowerBI import BI_section
from pages.conclusions import conclusions_section

st.set_page_config(
    page_title="📊 Social Media Trends Engagement Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
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
    raw_data, cleaned_data = load_data() # Unpack the tuple returned by load_data
    
    if raw_data is not None and cleaned_data is not None:
        st.sidebar.title("Menu")
        
        # Define the pages with their icons and functions
        pages = {
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
        for page_name in pages.keys():
            if st.sidebar.button(page_name, key=page_name):
                st.session_state.current_page = page_name
        
        # Display the selected page
        pages[st.session_state.current_page]()
        
        render_footer()
    else:
        st.error("Failed to load data. Please check the data files.")

if __name__ == "__main__":
    main()