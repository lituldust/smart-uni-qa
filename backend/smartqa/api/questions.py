from flask import Blueprint, request, jsonify
from smartqa.rag.rag_service import generate_answer

questions_bp = Blueprint("questions", __name__)

@questions_bp.route("", methods=["POST"])
def handle_ask_question():
    data = request.get_json(silent=True) or {}
    question = data.get("question")

    if not question:
        return jsonify({"error": "question is required"}), 400

    try:
        response_data = generate_answer(question)
        
        if "error" in response_data:
             return jsonify(response_data), 400

        return jsonify(response_data)

    except Exception as e:
        print(f"Error processing question: {e}")
        return jsonify({"error": "An internal error occurred processing your request."}), 500