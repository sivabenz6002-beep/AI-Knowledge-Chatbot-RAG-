from langchain_community.vectorstores import FAISS

def create_vectorstore(docs, embeddings):
    return FAISS.from_documents(docs, embeddings)

def save_db(db, path="db"):
    db.save_local(path)

def load_db(embeddings, path="db"):
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)