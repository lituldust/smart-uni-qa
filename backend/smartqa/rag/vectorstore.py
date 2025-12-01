import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# simple global singleton for MVP
_vectorstore = None

def get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        # For MVP, initialize empty. Later, persist to disk.
        _vectorstore = FAISS.from_texts(["init"], embeddings)
    return _vectorstore