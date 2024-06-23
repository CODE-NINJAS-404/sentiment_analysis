import streamlit as st
import sentiment as se

# Streamlit app layout
def main():
    # Set up the page configuration
    st.set_page_config(
        page_title="Social Media Sentiment Analysis",
        page_icon="😊",
        layout="centered",
        initial_sidebar_state="collapsed",
    )
    
    # Add some custom styling
    st.markdown("""
        <style>
        .main {
            background-color: #f7f7f7;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 24px;
            border: none;
            font-size: 16px;
            margin-top: 10px;
            transition: background-color 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        .stTextArea textarea {
            background-color: #ffffff;
            color: #333333;
            border: 1px solid #d4d4d4;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
        }
        .stMarkdown p {
            font-size: 18px;
            color: #333333;
        }
        .stTextArea textarea:focus {
            border-color: #4CAF50;
        }
        </style>
    """, unsafe_allow_html=True)

    # App title and description
    st.title('Social Media Sentiment Analysis App')
    st.write('Enter any social media statements to analyze their sentiment.')

    # User input area
    st.text_area('Input your text here:', key='user_input', height=150)

    # Analyze button
    if st.button('Analyze'):
        user_input = st.session_state.user_input
        if user_input:
            output = se.prediction(user_input)
            if output[0] == "positive":
                st.success("**Sentiment:** Positive 😀")
            elif output[0] == 'negative':
                st.error("**Sentiment:** Negative 😞")
            else:
                st.warning("**Something went wrong. Please type another sentence.**")

    # Sidebar information
    st.sidebar.header('About the App')
    st.sidebar.write("""
        This app analyzes the sentiment of social media statements. It uses natural language processing (NLP) techniques 
        to classify the sentiment as positive or negative. Simply enter a statement and click 'Analyze' to see the result.
    """)

if __name__ == '__main__':
    main()
