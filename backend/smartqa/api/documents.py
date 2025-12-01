from flask import Blueprint, jsonify

documents_bp = Blueprint("documents", __name__)

@documents_bp.route("", methods=["GET"])
def list_documents():
    # temporary stub
    return jsonify({"message": "documents endpoint OK"})