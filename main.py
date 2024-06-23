import streamlit as st
import matplotlib.pyplot
import sentiment as se
import pandas as pd
import matplotlib.pyplot as plt

# Custom CSS for styling
def set_custom_style():
    st.markdown(
        """
        <style>
        .title {
            font-size: 3em;
            color: #2e4053;
            text-align: center;
            margin-bottom: 30px;
        }
        .subtitle {
            font-size: 1.5em;
            color: #34495e;
            text-align: center;
            margin-bottom: 20px;
        }
        .result {
            font-size: 1.2em;
            margin-top: 20px;
            text-align: center;
        }
        .positive {
            color: #27ae60;
        }
        .negative {
            color: #c0392b;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to analyze sentiment and accumulate results
def analyze_sentiment_batch(user_input):
    results = []
    statements = user_input.split('\n')  # Split input by new lines for multiple statements
    for statement in statements:
        if statement.strip():  # Check if statement is not empty
            output = se.prediction(statement)
            results.append(output)  # Append sentiment result
    return results

# Function to calculate and display sentiment percentages
def display_sentiment_stats(results):
    if not results:
        return

    st.subheader('Sentiment Analysis Results')
    df = pd.DataFrame(results)
    sentiment_counts = df['sentiment'].value_counts()
    total_count = len(results)
    positive_percentage = (sentiment_counts.get('positive', 0) / total_count) * 100
    negative_percentage = (sentiment_counts.get('negative', 0) / total_count) * 100

    st.write(f"Total Statements Analyzed: {total_count}")
    st.write(f"Percentage of Positive Sentiments: {positive_percentage:.2f}%")
    st.write(f"Percentage of Negative Sentiments: {negative_percentage:.2f}%")

    # Plotting sentiment distribution
    plt.figure(figsize=(8, 6))
    plt.bar(sentiment_counts.index, sentiment_counts.values, color=['#27ae60', '#c0392b'])
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.title('Sentiment Distribution')
    st.pyplot(plt)

# Function to display individual sentiment results
def display_individual_results(results):
    st.subheader('Individual Sentiment Results')
    for result in results:
        sentiment = result['sentiment']
        positive_prob = result['positive_probability']
        negative_prob = result['negative_probability']
        st.markdown(f'<p class="result {sentiment}">Sentiment: {sentiment.capitalize()} </p>', unsafe_allow_html=True)
        st.write(f"Positive Probability: {positive_prob:.2f}%")
        st.write(f"Negative Probability: {negative_prob:.2f}%")
        st.markdown('---')

# Streamlit app layout
def main():
    set_custom_style()

    st.title(' Sentiment Analyzer')
    st.markdown('---')
    st.markdown('Enter social media statements to analyze sentiment:')
    
    user_input = st.text_area('Input your text here:', '')

    if st.button('Analyze'):
        if user_input:
            statements = user_input.split('\n')
            with st.spinner('Analyzing...'):
                results = analyze_sentiment_batch(user_input)
                display_individual_results(results)
                display_sentiment_stats(results)

if __name__ == '__main__':
    main()
