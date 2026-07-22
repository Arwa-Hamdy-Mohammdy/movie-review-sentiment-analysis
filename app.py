import streamlit as st

from predict import predict_sentiment

st.title("🎬 Movie Review Sentiment Analysis")

review = st.text_area("Enter your movie review:")

if st.button("Predict"):

    if review.strip():

        result, confidence = predict_sentiment(review)

        if result == "Positive":
            st.success("🎉 Positive Review")
            st.write(f"Confidence: {confidence*100:.2f}%")
            st.balloons()

        else:
            st.error("😞 Negative Review")
            st.write(f"Confidence: {confidence*100:.2f}%")

    else:
        st.warning("Please enter a review first.")