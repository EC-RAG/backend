from langchain_openai import ChatOpenAI
from utils.config import config

llm = ChatOpenAI(
    base_url='https://api.deepseek.com/v1',
    api_key = config['models']['deepseek']['api_key'],
    model= config['models']['deepseek']['model'],
    temperature= 0
)