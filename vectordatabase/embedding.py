"""
embedding with volcengine API use openai API
"""
from openai import OpenAI

BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"
ARK_API_KEY = "84b340ef-4f05-46ae-a5c5-cedcc8910111"

client = OpenAI(
    api_key=ARK_API_KEY,
    base_url=BASE_URL,
    
)

def embedding(text: str):
    response = client.embeddings.create(
        model="doubao-embedding-text-240715",
        input=[text],
    )
    return response.data[0].embedding
