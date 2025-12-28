from vectorstore import get_vectorstore
from generate_response import generate_augmented_response

def get_response(query):
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

    answer, docs = generate_augmented_response(query, retriever)

    result = {
        "answer": answer,
        "source_documents": docs
    }

    return result