"""
embedding with volcengine API use openai API
"""
from openai import OpenAI
from utils.config import config

client = OpenAI(
    api_key= config['models']['embedding']['api_key'],
    base_url=config['models']['embedding']['base_url'],
    
)

def embedding(text: str):
    response = client.embeddings.create(
        model=config['models']['embedding']['model'],
        input=[text],
    )
    return response.data[0].embedding
