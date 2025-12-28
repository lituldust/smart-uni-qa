from flask import jsonify
from smartqa.rag.get_response import get_response

def ask_question(question):
    if not question:
        return jsonify({"error": "question is required"}), 400
    
    result = get_response(question)
    formatted_sources = [
        {"content": doc.page_content, "metadata": doc.metadata}
        for doc in result["source_documents"]
    ]

    return {
        "answer": result["answer"], 
        "sources": formatted_sources
    }