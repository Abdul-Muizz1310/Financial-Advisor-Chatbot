# 💰 Finance RAG Chatbot (Streamlit + Langflow)

This is a Streamlit UI wrapper for a Langflow-powered RAG chatbot using financial data from Pakistan Stock Exchange (2001–2024).

## 🚀 Features

- Langflow JSON-based flow execution
- Streamlit for interactive UI
- AstraDB as vector DB
- OpenAI LLM backend

## 🛠️ Local Setup

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## 🌐 Deployment

Deploy easily to [Streamlit Cloud](https://streamlit.io/cloud). Set environment secrets:
- `OPENAI_API_KEY`
- `ASTRA_DB_APPLICATION_TOKEN`
- `ASTRA_DB_ID`
