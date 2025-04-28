from langchain.chains.llm import LLMChain

from .prompts.table_name_prompt import table_name_prompt as prompt

table_name_chain = lambda llm: LLMChain(
    llm=llm,
    prompt=prompt,
)