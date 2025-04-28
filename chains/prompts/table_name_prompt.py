from langchain.prompts import PromptTemplate

table_name_prompt = PromptTemplate(
    input_variables=["query",'table_aliases', 'rules', 'table_names'],
    template='''
    <system>
        你是一个语义搜索引擎，你的任务是提取用户查询语句中的表名。
    </system>

    <user>
        用户查询语句: {query}
    </user>

    <context>
        系统中目前有以下表:
        {table_names}
        其中可能的别名对应的表名有:
        {table_aliases}
    </context>

    <assistant>
        你能从用户的查询语句中提取出表名吗？如果能，请列出可能的表名。
    </assistant>

    <instruction>
        以下是需要注意的事项:
        {rules}
    </instruction>
    ''',
)