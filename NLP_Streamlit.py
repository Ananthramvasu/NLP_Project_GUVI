import streamlit as st
import pickle
import pandas as pd
# Load vectorizer and model
with open("NLP_Model.pkl", "rb") as f:
    model = pickle.load(f)

vec = pd.read_pickle('vectorizer.pkl')

# Set up Streamlit page
st.set_page_config(page_title="Sentiment Predictor", layout="centered")
st.title("ChatGPT Review Sentiment Analyzer")
st.markdown("Enter a review and get the sentiment prediction (Positive, Neutral, or Negative).")

# User input
user_input = st.text_area("Your review here:", height=150)
got = vec.transform([user_input])

# Predict button
if st.button("Predict Sentiment"):
    if not user_input.strip():
        st.warning("Please enter a review first.")
    else:
        # In Streamlit
        prediction = model.predict([got][0])

        if prediction == "Positive":
            st.markdown("Looks like the user loved it!")
        elif prediction == "Negative":
            st.markdown("Sounds like a complaint.")
        else:
            st.markdown("Seems neutral.")

        # Display result
        st.success(f"**Predicted Sentiment: {prediction}**")

