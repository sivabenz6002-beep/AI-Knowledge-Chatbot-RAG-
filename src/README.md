# 📄 AI Knowledge Chatbot (RAG)

🚀 **LangChain Messages + Groq + FAISS + Streamlit**

An AI-powered chatbot that allows users to upload PDFs and ask questions based on the document content using Retrieval-Augmented Generation (RAG).

---

## 🧠 Project Overview

This project combines:

* ⚡ **Groq LLM** for ultra-fast responses
* 🔎 **FAISS Vector Store** for similarity search
* 🧱 **LangChain Messages API** for structured LLM interaction
* 🌐 **Streamlit** for an interactive UI

Users can upload documents and interact with them conversationally.

---

## ✨ Features

* 📂 Upload PDF documents
* 💬 Ask questions from documents
* ⚡ Fast responses using Groq LLM
* 🔍 Context-aware answers (RAG pipeline)
* 🧠 Semantic search with FAISS
* 🖥️ Simple Streamlit interface

---

## 🏗️ Project Structure

```
ai-knowledge-chatbot/
│── app.py
│── requirements.txt
│── .env
│
├── src/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── chain.py
│   └── utils.py
│
├── data/
├── db/
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-knowledge-chatbot.git
cd ai-knowledge-chatbot
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
pip install langchain-text-splitters
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 🔄 How It Works (RAG Pipeline)

1. 📄 Upload PDF
2. ✂️ Split text into chunks
3. 🔢 Convert text into embeddings
4. 🗂️ Store embeddings in FAISS
5. 🔍 Retrieve relevant chunks
6. 🤖 Generate answer using Groq LLM

---

## 🧠 Tech Stack

* **LangChain**
* **Groq API**
* **FAISS**
* **HuggingFace Embeddings**
* **Streamlit**

---

## 📌 Example Use Cases

* 📚 Study assistant
* 📑 Resume / document analyzer
* 🏢 Company knowledge base chatbot
* 📖 Research assistant

---

## 🚀 Future Improvements

* 💬 Chat history (memory)
* 📂 Multiple document support
* 📌 Source citations
* 🤖 Multi-agent system (LangGraph)
* 🌍 Deployment (Streamlit Cloud / HuggingFace)

---

## 🧑‍💻 Resume Description

**Built an AI Knowledge Chatbot using LangChain Messages, Groq LLM, FAISS vector store, and Streamlit implementing Retrieval-Augmented Generation (RAG).**

---

## ⭐ Acknowledgements

* LangChain
* Groq
* HuggingFace
* Streamlit

---

## 📜 License

This project is open-source and available under the MIT License.
