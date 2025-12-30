import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from smartqa.services.ingestion_service import process_uploaded_file

documents_bp = Blueprint("documents", __name__)

UPLOAD_FOLDER = "../tmp/uploads"  # Ensure this folder exists and is writable
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@documents_bp.route("/uploads", methods=["POST"])
def upload_document():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        filename = secure_filename(file.filename)
        print("Received file:", filename)  # Debug Print
        temp_path = os.path.join(UPLOAD_FOLDER, filename)

        file.save(temp_path)

        result = process_uploaded_file(temp_path, filename)
        
        if "error" in result:
             return jsonify(result), 500
             
        return jsonify(result), 200