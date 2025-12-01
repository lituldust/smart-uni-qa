from flask import Blueprint, request, jsonify

questions_bp = Blueprint("questions", __name__)

@questions_bp.route("", methods=["POST"])
def ask_question():
    data = request.get_json(silent=True) or {}
    question = data.get("question")
    if not question:
        return jsonify({"error": "question is required"}), 400

    # temporary stub answer for now
    return jsonify({
        "answer": f"You asked: {question}. RAG is not wired yet.",
        "sources": []
    })