import streamlit as st
from components.chat_input import ChatInput
from components.openai_llm import OpenAIModel
from components.keyword_extractor import KeywordExtractor
from components.astra_db import AstraDB
from components.parser import Parser
from components.prompt_template import PromptTemplate
from components.chat_output import ChatOutput

from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Finance RAG Chatbot", layout="wide")
st.title("📈 Finance RAG Chatbot")
st.markdown("_Query PSX filings and financial reports (2001–2024) with context-aware responses._")

user_input = st.text_area("Your question", height=100, placeholder="e.g. Which sectors showed strongest recovery after 2020 downturn?")

if st.button("Ask"):
    with st.spinner("Thinking..."):
        chat_input = ChatInput(user_input)
        intermediate_llm = OpenAIModel()
        keywords, question = intermediate_llm.generate(chat_input)

        extractor = KeywordExtractor()
        search_query = extractor.extract(keywords)

        astra_db = AstraDB()
        retrieved_data = astra_db.query(search_query)

        parser = Parser()
        context = parser.parse(retrieved_data)

        prompt = PromptTemplate(context=context, question=question)
        final_prompt = prompt.build()

        final_llm = OpenAIModel()
        response = final_llm.generate(final_prompt)

        chat_output = ChatOutput()
        chat_output.render(response)
