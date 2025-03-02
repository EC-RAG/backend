from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains.llm import LLMChain

llm = ChatOpenAI(
    base_url='https://api.deepseek.com/v1',
    api_key = 'sk-4ebf64a872724ab19c6ae5f0c6707af7',
    model='deepseek-chat'
)

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
