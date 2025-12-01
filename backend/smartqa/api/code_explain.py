from flask import Blueprint, request, jsonify

code_explain_bp = Blueprint("code_explain", __name__)

@code_explain_bp.route("", methods=["POST"])
def explain_code():
    data = request.get_json(silent=True) or {}
    code = data.get("code", "")
    if not code:
        return jsonify({"error": "code is required"}), 400

    # temporary stub
    explanation = "Step-by-step code explanation will go here (stub)."
    return jsonify({"code": code, "explanation": explanation})