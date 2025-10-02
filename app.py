import os
import openai
import streamlit as st

# Use environment variable for API key (safer)
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --------------------
# Helper functions
# --------------------
def ask_question(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for answering questions."},
            {"role": "user", "content": question}
        ]
    )
    # For v1, 'choices' is in the 'response' object; distill to just the message content
    return response.choices[0].message.content.strip()


def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize text into 3 clear sentences."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()

# --------------------
# Streamlit UI
# --------------------
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

st.title("🤖 QA + Summarization Chatbot")
st.markdown("Built with **Streamlit** + **OpenAI API** 🚀")

# Create tabs
tab1, tab2 = st.tabs(["💬 Q&A Bot", "📝 Text Summarizer"])

with tab1:
    st.header("Ask me anything!")
    question = st.text_input("Enter your question here:")
    if st.button("Get Answer", key="qa"):
        if question.strip():
            with st.spinner("Thinking..."):
                answer = ask_question(question)
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
