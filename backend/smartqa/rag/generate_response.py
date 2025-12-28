import os
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI

env_path = Path(__file__).parent.parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key = GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def generate_augmented_response(query, retriever):
  search_results = retriever.invoke(query)
  context = "\n\n".join([doc.page_content for doc in search_results])

  prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
  response = client.chat.completions.create(
      model="gemini-2.5-flash", # Using model gemini 2.5 flash
      messages=[
        {
          "role": "system",
          "content": "You are a helpful assistant."
        },
        {
          "role": "user",
          "content": prompt
        }
      ],
  )

  answer_text = response.choices[0].message.content

  return answer_text, search_results