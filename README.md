# 🚌 RedBus Customer Support Chatbot

A simple AI-powered customer support chatbot for RedBus, built with Streamlit and Google Gemini.

---

## 📋 Prerequisites

- Python 3.10+
- Google Gemini API key

---

## 📦 Installation

```bash
pip3 install streamlit google-genai
```

---

## 📁 Project Structure

```
AI/
├── chatbot.py
├── india_bus_dataset.txt
└── README.md
```

> Make sure `india_bus_dataset.txt` is in the **same folder** as `chatbot.py`.

---

## ⚙️ Configuration

Open `chatbot.py` and replace the API key:

```python
API_KEY = "YOUR_API_KEY_HERE"
```

---

## 🚀 Running the App

```bash
python3 -m streamlit run chatbot.py
```

Then open your browser at: [http://localhost:8501](http://localhost:8501)

---

## 💬 Features

- Conversational chat interface
- Answers based only on the knowledge base (`india_bus_dataset.txt`)
- Maintains full chat history within the session
- Politely declines questions outside the knowledge base

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/)
- [Google Gemini API](https://ai.google.dev/) — `gemini-2.5-flash`
