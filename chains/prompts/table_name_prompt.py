from langchain.prompts import PromptTemplate
from db.sqlite import session

from data.sql_data_manage import *
class CustomPromptTemplate(PromptTemplate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = session
    
    def format(self, **kwargs):
        tables = get_table_info(self.db)
        table_names = [table.table_name for table in tables]
        table_names = ", ".join(table_names)

        table_aliases = get_table_alias(self.db)
        table_aliases = [f"原名：{alias.table_name}，别名：{alias.table_alias}" for alias in table_aliases]
        table_aliases = "\n".join(table_aliases)

        rules = get_prompt_rule(self.db, step_type="tablename")
        rules = [f"{id}.{rule.content}" for id, rule in enumerate(rules)]
        rules = "\n".join(rules)

        return super().format(table_names=table_names, table_aliases=table_aliases, rules=rules, **kwargs)



table_name_prompt = CustomPromptTemplate(
    input_variables=["query"],
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