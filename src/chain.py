from langchain_groq import ChatGroq

def get_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",   # ✅ FINAL FIX
        temperature=0
    )

def ask_question(llm, retriever, query):
    docs = retriever.invoke(query)

    if not docs:
        return "No relevant information found."

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer ONLY from the context below.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)
    return response.content