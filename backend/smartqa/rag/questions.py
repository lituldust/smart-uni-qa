from flask import Blueprint, request, jsonify
from smartqa.rag.chains import get_qa_chain

questions_bp = Blueprint("questions", __name__)

@questions_bp.route("", methods=["POST"])
def ask_question():
    data = request.get_json()
    question = data.get("question")
    if not question:
        return jsonify({"error": "question is required"}), 400

    qa_chain = get_qa_chain()
    result = qa_chain({"query": question})
    answer = result["result"]
    sources = [
        {"content": doc.page_content, "metadata": doc.metadata}
        for doc in result.get("source_documents", [])
    ]

    return jsonify({"answer": answer, "sources": sources})