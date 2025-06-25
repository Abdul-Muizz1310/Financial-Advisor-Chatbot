# Finance RAG Chatbot

A Streamlit-based chatbot that uses Retrieval-Augmented Generation (RAG) over Pakistan Stock Exchange documents (2001–2024).

## 🔧 Setup

1. Clone the repo.
2. Create a `.env` file with:
   ```
   OPENAI_API_KEY=
   ASTRA_DB_ID=
   ASTRA_DB_REGION=
   ASTRA_DB_KEYSPACE=
   ASTRA_DB_APPLICATION_TOKEN=
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run locally:
   ```
   streamlit run app.py
   ```

## 🚀 Deploy on Streamlit Community Cloud

1. Push code to GitHub.
2. Connect GitHub repo on [streamlit.io](https://streamlit.io/cloud).
3. Add `.env` values in Streamlit Cloud **Secrets Manager**.
