from langchain.chains.llm import LLMChain

from .llms.deepseek import llm
from .prompts.table_name_prompt import table_name_prompt

table_name_chain = LLMChain(
    llm=llm,
    prompt=table_name_prompt
)
