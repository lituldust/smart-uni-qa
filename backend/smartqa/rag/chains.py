from langchain.chains import RetrievalQA
from langchain_community.llms import OpenAI
from .vectorstore import get_vectorstore

def get_qa_chain():
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    llm = OpenAI(
        api_key = GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain