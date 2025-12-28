from flask import jsonify
from get_response import get_response

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

if __name__ == "__main__":
    print("--- Testing RAG Pipeline Manually ---")
    test_q = "What is Python used for?"
    
    # We call the LOGIC function directly to avoid Flask 'jsonify' errors
    response_data = ask_question(test_q)
    
    print(f"\nQ: {test_q}")
    print(f"A: {response_data['answer']}")
    print("\nSources:")
    for s in response_data['sources']:
        print(f"- {s['content']} (Page {s['metadata']['page']})")