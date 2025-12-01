from flask import Flask
from flask_cors import CORS
from smartqa.api.documents import documents_bp
from smartqa.api.questions import questions_bp
from smartqa.api.quiz import quiz_bp
from smartqa.api.code_explain import code_explain_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register blueprints
    app.register_blueprint(documents_bp, url_prefix="/api/documents")
    app.register_blueprint(questions_bp, url_prefix="/api/questions")
    app.register_blueprint(quiz_bp, url_prefix="/api/quiz")
    app.register_blueprint(code_explain_bp, url_prefix="/api/code-explain")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)