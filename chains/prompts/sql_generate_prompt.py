from langchain.prompts import PromptTemplate

sql_generate_prompt = PromptTemplate(
    input_variables=['query', 'table_name', 'table_def_sql', 'table_field_info', 'related_doc', 'rules'],
    template='''
    <system>
        你是一个数据库专家，你的任务是生成SQL查询语句。
    </system>

    <context>
        表名：{table_name}
        表的定义为：
        {table_def_sql}
        表部分内容如下:
        {table_head}
        其中部分名词解释如下：
        {table_field_info}
        相关的文档如下：
        {related_doc}
    </context>

    <user>
        用户的查询语句为：{query}
    </user>

    <assistant>
        你能从用户的查询语句中生成SQL查询语句吗？如果能，请生成SQL查询语句。
    </assistant>

    <instruction>
        以下是需要注意的事项:
        {rules}
    </instruction>
    '''
)