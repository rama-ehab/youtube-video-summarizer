# YouTube Video Summarizer

An AI-powered YouTube video summarizer that extracts video transcripts and generates concise summaries using **BART-large-CNN**.

## Tech Stack

* Python
* Streamlit
* FastAPI
* Hugging Face Transformers
* BART-large-CNN
* YouTube Transcript API
* PyTorch
* Kaggle GPU
* ngrok

## Architecture

```text
Streamlit → ngrok → FastAPI → YouTube Transcript → BART → Summary
```

The **FastAPI backend** and BART model run on a Kaggle GPU, while **Streamlit** provides the user interface.

## Project Structure

```text
├── app.py
├── youtube_summarizer.ipynb
└── README.md
```

## Features

* YouTube transcript extraction
* Long-text chunking
* AI-powered summarization
* GPU-accelerated inference
* FastAPI REST API
* Streamlit interface
