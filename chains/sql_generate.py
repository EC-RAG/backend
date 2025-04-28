from langchain.chains.llm import LLMChain

from .prompts.sql_generate_prompt import sql_generate_prompt as prompt

sql_generate_chain = lambda llm: LLMChain(
    llm=llm,
    prompt=prompt,
)
