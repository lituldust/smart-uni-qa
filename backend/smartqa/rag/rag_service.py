from flask import jsonify
import os
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI
from smartqa.rag.vectorstore import get_vectorstore

env_path = Path(__file__).resolve().parents[3] / '.env'
load_dotenv(dotenv_path=env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def generate_answer(question):
    if not question:
        return jsonify({"error": "question is required"}), 400
    
    # 1. Retrieval
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    search_results = retriever.invoke(question)

    # 2. Query Building
    context = "\n\n".join([doc.page_content for doc in search_results])

    system_prompt = "You are a smart university assistant. Use the provided Context to answer the Question."
    user_prompt = f"Context:\n{context}\n\nQuestion: {question}\n\nAnswer:"

    # 3. Generation
    try:
        response = client.chat.completions.create(
            model="gemini-2.5-flash", # Using model gemini 2.5 flash
            messages=[
                {
                "role": "system",
                "content": system_prompt
                },
                {
                "role": "user",
                "content": user_prompt
                }
            ],
        )
        answer_text = response.choices[0].message.content
    except Exception as e:
        print(f"LLM Error: {e}")
        return {"error": "Failed to generate answer from AI."}
    
    # 4. Formatting
    formatted_sources = [
        {"content": doc.page_content, "metadata": doc.metadata}
        for doc in search_results
    ]

    return {
        "answer": answer_text, 
        "sources": formatted_sources
    }