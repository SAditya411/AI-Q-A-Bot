import os
import requests
import streamlit as st

# --------------------
# Hugging Face API setup
# --------------------
HF_API_KEY = os.getenv("HF_API_KEY")
HF_HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

# Example models:
QA_MODEL = "deepset/roberta-base-squad2"       # Q&A
SUMMARIZATION_MODEL = "facebook/bart-large-cnn" # Summarization

HF_API_URL = "https://api-inference.huggingface.co/models/{}"

# --------------------
# Helper functions
# --------------------
def ask_question(question, context=""):
    """
    Ask a question to a Hugging Face QA model.
    Optional: you can provide context for better answers.
    """
    payload = {"inputs": {"question": question, "context": context}}
    response = requests.post(HF_API_URL.format(QA_MODEL), headers=HF_HEADERS, json=payload)
    if response.status_code == 200:
        answer = response.json()
        if isinstance(answer, list) and "answer" in answer[0]:
            return answer[0]["answer"]
        return str(answer)
    else:
        return f"Error: {response.status_code} - {response.text}"


def summarize_text(text):
    """
    Summarize text using a Hugging Face model.
    """
    payload = {"inputs": text}
    response = requests.post(HF_API_URL.format(SUMMARIZATION_MODEL), headers=HF_HEADERS, json=payload)
    if response.status_code == 200:
        summary = response.json()
        if isinstance(summary, list) and "summary_text" in summary[0]:
            return summary[0]["summary_text"]
        return str(summary)
    else:
        return f"Error: {response.status_code} - {response.text}"

# --------------------
# Streamlit UI
# --------------------
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

st.title("🤖 QA + Summarization Chatbot")
st.markdown("Built with **Streamlit** + **Hugging Face API** 🚀")

tab1, tab2 = st.tabs(["💬 Q&A Bot", "📝 Text Summarizer"])

with tab1:
    st.header("Ask me anything!")
    question = st.text_input("Enter your question here:")
    context = st.text_area("Optional: Provide context for better answers")
    if st.button("Get Answer", key="qa"):
        if question.strip():
            with st.spinner("Thinking..."):
                answer = ask_question(question, context)
            st.success(answer)
        else:
            st.warning("Please enter a question.")

with tab2:
    st.header("Summarize your text")
    text = st.text_area("Paste text to summarize (article, blog, etc.)")
    if st.button("Summarize", key="summarize"):
        if text.strip():
            with st.spinner("Summarizing..."):
                summary = summarize_text(text)
            st.success(summary)
        else:
            st.warning("Please paste some text to summarize.") 
