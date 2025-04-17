from langchain.chains.llm import LLMChain

from .llms.deepseek import llm
from .prompts.table_name_prompt import table_name_prompt as prompt

table_name_chain = prompt | llm
