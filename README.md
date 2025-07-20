# 🌐 LangChain Summarizer: YouTube & Website Content

This is a Streamlit application that summarizes the content of a **YouTube video** or **any website URL** using **LangChain**, **Groq’s LLM**, and **OpenAI-compatible interface**. The app fetches the content, processes it using a pre-defined prompt, and returns a 300-word summary.

---

## 🚀 Features

- ✅ Summarize content from **YouTube videos**
- ✅ Summarize **website text** using URL
- 🔐 Secure API key input via sidebar
- ⚡ Powered by **Groq** and **LangChain**
- 🧠 Uses `Gemma-7b-It` for fast, high-quality summaries

---

## 📦 Requirements

- Python 3.9+
- Groq API Key
- Streamlit

---

## 📁 Installation

```bash
git clone https://github.com/RITIKA-01A/URL_Content_Summarisation.git
cd URL_Content_Summarisation
pip install -r requirements.txt
```
## 🧪 Run the App
```
streamlit run app.py
```
## 🧠 How It Works
- User inputs a YouTube or Website URL.

- App loads the content using:

- YoutubeLoader for videos

- UnstructuredURLLoader for websites

- A prompt instructs the LLM to summarize the content in 300 words.

- Summary is displayed in the UI.

## 📌 Tech Stack
- LangChain

- Groq (Gemma-7b-It)

- Streamlit

- OpenCV (for URL validation)

- Python


