from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# simple global singleton for MVP
_vectorstore = None
_embeddings = None

def get_embeddings():
    global _embeddings
    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    return _embeddings

def get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        embeddings = get_embeddings()

        # sample_texts = [
        #     "Machine learning is a subset of AI that learns from data.",
        #     "Neural networks are inspired by biological neurons.",
        #     "Python is commonly used for machine learning."
        # ]

        # sample_metadata = [
        #     {"page": 1, "source": "ML Lecture"},
        #     {"page": 2, "source": "ML Lecture"},
        #     {"page": 3, "source": "ML Lecture"}
        # ]

        # For MVP, initialize empty. Later, persist to disk.
        _vectorstore = FAISS.from_texts(["Initial index"], embeddings)
        print("Vectorstore succesfully initiated.")
    return _vectorstore

def add_documents(docs):
    global _vectorstore
    vectorstore = get_vectorstore()

    vectorstore.add_documents(docs)
    print(f"Added {len(docs)} document chunks to the vector store.")