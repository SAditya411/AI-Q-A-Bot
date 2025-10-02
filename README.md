
# 🤖 Text Summarizer (Hugging Face + Streamlit)

This is a **Text Summarizer Web App** built using **Streamlit** and **Hugging Face API**. Originally, the app also included a **Q&A feature**, but it has been commented out due to API constraints.

---
## **Live Demo**

Access the deployed Text Summarizer here:  

[**View Live App**](https://ai-q-a-bot-5czm.onrender.com/)

## **Project Features**

* Summarize any text (article, blog, etc.) into concise summaries.
* Built with **Streamlit** for interactive UI.
* Uses **Hugging Face Inference API** for summarization.

---

## **Table of Contents**

1. [Installation](#installation)
2. [Setup](#setup)
3. [Running Locally](#running-locally)
4. [Deployment on Render](#deployment-on-render)
5. [Why Q&A Was Commented Out](#why-qa-was-commented-out)
6. [Common Errors](#common-errors)

---

## **Installation**

1. Clone the repository:

```bash
git clone <https://github.com/SAditya411/AI-Q-A-Bot.git>
```

2. Create a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
streamlit==1.29.0
requests==2.31.0
```

---

## **Setup**

1. Get a Hugging Face API key:

   * Sign up at [huggingface.co](https://huggingface.co/).
   * Go to **Settings → Access Tokens → New Token**.
   * Copy the API key.

2. Set environment variable:

**Linux / Mac**

```bash
export HF_API_KEY="YOUR_HUGGINGFACE_API_KEY"
```

**Windows**

```bash
set HF_API_KEY="YOUR_HUGGINGFACE_API_KEY"
```

3. Make sure your app reads the key from `os.getenv("HF_API_KEY")`.

---

## **Running Locally**

Run the Streamlit app:

```bash
streamlit run app.py
```

* Open your browser at `http://localhost:8501`.
* Paste the text you want to summarize.
* Click **Summarize** to get a summary.

---

## **Deployment on Render**

1. Create a new **Web Service** on [Render](https://render.com/).
2. Connect your GitHub repository.
3. Add **Environment Variable**:

   * Key: `HF_API_KEY`
   * Value: `<your Hugging Face API key>`
4. Add a **start command** in Render:

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

5. Deploy. Your app will be live at the Render URL.

---

## **Why Q&A Was Commented Out**

* Initially, the app included a Q&A tab using the Hugging Face model `google/flan-t5-small`.
* **Problem:** The model is **not hosted on Hugging Face Inference API**, causing **404 errors**:

```
Error: 404 - Not Found
```

* Alternative models like `deepset/roberta-base-squad2` **require a context**, and cannot answer free-form questions without it. Using an empty context gives:

```
Error: 400 - {"error":"context cannot be empty"}
```

* **Decision:** Commented out all Q&A code and UI to prevent runtime errors.
* The app now **focuses only on Text Summarization**, which works reliably with the Hugging Face API.

---

## **Common Errors & Fixes**

1. **404 - Not Found**

   * Cause: Using a model that is not hosted on Hugging Face Inference API.
   * Fix: Use hosted models (`facebook/bart-large-cnn` for summarization) or provide a default context for Q&A.

2. **400 - Context cannot be empty**

   * Cause: Q&A model requires a non-empty context.
   * Fix: Either provide a default context or remove Q&A functionality.

3. **Missing HF_API_KEY**

   * Cause: Environment variable not set.
   * Fix: Add `HF_API_KEY` in environment variables or `.env` file.

4. **Rate limits**

   * Cause: Hugging Face free tier allows limited inference requests per month.
   * Fix: Cache results with `st.cache_data` or upgrade your Hugging Face plan.

---

## **Future Improvements**

* Re-add Q&A using a free GPT-like API that doesn’t require context.
* Add **caching** to reduce API calls.
* Improve **UI** with Markdown formatting for summaries.

---

## **Project Structure**

```
my-app/
│
├─ app.py                # Streamlit app code
├─ requirements.txt      # Python dependencies
├─ start.sh (optional)   # For Render deployment
└─ README.md             # This file



