import streamlit as st
from dotenv import load_dotenv
import os

from src.loader import load_pdf
from src.splitter import split_docs
from src.embeddings import get_embeddings
from src.vectorstore import create_vectorstore, save_db, load_db
from src.chain import get_llm, ask_question
from src.utils import save_uploaded_file

load_dotenv()

os.makedirs("data", exist_ok=True)
os.makedirs("db", exist_ok=True)

st.set_page_config(page_title="AI Chatbot")
st.title("📄 AI Knowledge Chatbot")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    file_path = save_uploaded_file(uploaded_file)

    docs = load_pdf(file_path)
    chunks = split_docs(docs)

    embeddings = get_embeddings()
    db = create_vectorstore(chunks, embeddings)
    save_db(db)

    st.success("✅ Document processed!")

query = st.text_input("Ask a question")

if query:
    embeddings = get_embeddings()
    db = load_db(embeddings)

    retriever = db.as_retriever()
    llm = get_llm()

    answer = ask_question(llm, retriever, query)

    st.write("### 🤖 Answer")
    st.write(answer)