from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

from .llms.deepseek import llm

prompt = PromptTemplate(
    input_variables=["query"],
    template='''
    <system>
        你是一个语义搜索引擎，你的任务是提取用户查询语句中的表名。
    </system>

    <user>
        提取用户查询语句中的表名: {query}
        要求输出只有表名，不包含其他信息
    </user>
    ''',
)

table_name_chain = LLMChain(
    llm=llm,
    prompt=prompt
)
