from langchain.chains.llm import LLMChain

from .llms.deepseek import llm
from .prompts.graph_type_prompt import graph_type_prompt as prompt

graph_type_chain = prompt | llm
