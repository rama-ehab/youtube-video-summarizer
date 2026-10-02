import streamlit as st
import requests

# Your Kaggle/ngrok API
API_URL = "https://huskiness-antiques-theatrics.ngrok-free.dev/summarize"
API_KEY = "secret123"


st.title("🎥 YouTube Video Summarizer")

youtube_url = st.text_input(
    "Enter YouTube URL"
)


if st.button("Summarize"):

    if not youtube_url:
        st.warning("Please enter a YouTube URL.")

    else:
        with st.spinner("Generating summary..."):

            response = requests.post(
                API_URL,
                headers={
                    "Authorization": f"Bearer {API_KEY}"
                },
                json={
                    "url": youtube_url
                }
            )

        if response.status_code == 200:

            result = response.json()

            st.subheader("Summary")
            st.write(result["summary"])

        else:

            st.error(
                f"Error {response.status_code}: "
                f"{response.text}"
            )