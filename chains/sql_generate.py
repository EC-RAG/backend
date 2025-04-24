from langchain.chains.llm import LLMChain

from .llms.deepseek import llm
from .prompts.sql_generate_prompt import sql_generate_prompt as prompt

sql_generate_chain = LLMChain(
    llm=llm,
    prompt=prompt,
)
