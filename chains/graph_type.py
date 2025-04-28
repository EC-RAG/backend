from langchain.chains.llm import LLMChain

from .prompts.graph_type_prompt import graph_type_prompt as prompt

graph_type_chain = lambda llm: LLMChain(
    llm=llm,
    prompt=prompt,
)
