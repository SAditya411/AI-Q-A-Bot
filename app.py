import os
import requests
import streamlit as st

# --------------------
# Hugging Face API setup
# --------------------
HF_API_KEY = os.getenv("HF_API_KEY")
HF_HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

# Models
# QA_MODEL = "google/flan-t5-small"          # General Q&A (commented out)
SUMMARIZATION_MODEL = "facebook/bart-large-cnn"  # Summarization

HF_API_URL = "https://api-inference.huggingface.co/models/{}"

# --------------------
# Helper functions
# --------------------
# def ask_question(question):
#     """
#     Ask a question using Flan-T5 (does not require context)
#     """
#     payload = {"inputs": question}
#     response = requests.post(HF_API_URL.format(QA_MODEL), headers=HF_HEADERS, json=payload)
#     if response.status_code == 200:
#         result = response.json()
#         if isinstance(result, list) and "generated_text" in result[0]:
#             return result[0]["generated_text"]
#         return str(result)
#     else:
#         return f"Error: {response.status_code} - {response.text}"


def summarize_text(text):
    """
    Summarize text using BART model
    """
    payload = {"inputs": text}
    response = requests.post(HF_API_URL.format(SUMMARIZATION_MODEL), headers=HF_HEADERS, json=payload)
    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and "summary_text" in result[0]:
            return result[0]["summary_text"]
        return str(result)
    else:
        return f"Error: {response.status_code} - {response.text}"

# --------------------
# Streamlit UI
# --------------------
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

st.title("🤖 Text Summarizer")
st.markdown("Built with **Streamlit** + **Hugging Face API** 🚀")

# Only one tab now for summarization
# tab1, tab2 = st.tabs(["💬 Q&A Bot", "📝 Text Summarizer"])
# with tab1:
#     st.header("Ask me anything!")
#     question = st.text_input("Enter your question here:")
#     if st.button("Get Answer", key="qa"):
#         if question.strip():
#             with st.spinner("Thinking..."):
#                 answer = ask_question(question)
#             st.success(answer)
#         else:
#             st.warning("Please enter a question.")

st.header("Summarize your text")
text = st.text_area("Paste text to summarize (article, blog, etc.)")
if st.button("Summarize", key="summarize"):
    if text.strip():
        with st.spinner("Summarizing..."):
            summary = summarize_text(text)
        st.success(summary)
    else:
        st.warning("Please paste some text to summarize.")
