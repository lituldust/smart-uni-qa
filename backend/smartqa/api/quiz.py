from flask import Blueprint, jsonify

quiz_bp = Blueprint("quiz", __name__)

@quiz_bp.route("", methods=["POST"])
def generate_quiz():
    # temporary stub
    return jsonify({"quiz": [], "message": "quiz endpoint OK (stub)"})