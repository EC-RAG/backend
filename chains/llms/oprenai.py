from langchain_openai import ChatOpenAI
from utils.config import config

provider_dict = {
    'deepseek': 'https://api.deepseek.com/v1',
}

def gen_llm():
    base_url = provider_dict.get(config['models']['llm']['type'])
    return ChatOpenAI(
        base_url=base_url,
        api_key=config['models']['llm']['api_key'],
        model=config['models']['llm']['model'],
        temperature=0
    )
