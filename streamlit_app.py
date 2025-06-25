import os
import streamlit as st
from langflow import load_flow_from_json
from langflow.interface.run import run_flow_from_json

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-default-key")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN", "")
ASTRA_DB_ID = os.getenv("ASTRA_DB_ID", "")

st.set_page_config(page_title="Finance RAG Chatbot", layout="wide")

st.title("💰 Finance RAG Chatbot (PSX Reports 2001–2024)")
st.markdown("Ask financial questions based on Pakistan Stock Exchange (PSX) data.")

question = st.text_area("📨 Ask a Question", height=100)

if st.button("Submit"):
    with st.spinner("💭 Thinking..."):
        try:
            flow_path = "flow/finance-rag.json"
            inputs = {
                "input_value": question,
                "OPENAI_API_KEY": OPENAI_API_KEY,
                "ASTRA_DB_APPLICATION_TOKEN": ASTRA_DB_APPLICATION_TOKEN,
                "ASTRA_DB_ID": ASTRA_DB_ID
            }
            result = run_flow_from_json(flow_path, inputs)
            st.markdown("### ✅ Response:")
            st.success(result["output_value"])
        except Exception as e:
            st.error(f"Error: {str(e)}")
