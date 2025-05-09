from .llms.oprenai import gen_llm
from .graph_type import graph_type_chain
from .sql_generate import sql_generate_chain
from .table_name import table_name_chain
from .tools import execute_sql

from db.sqlite import session
from data.sql_data_manage import *
from data.vector_data_manage import *
from data import load_data_to_df
from utils import dicts_to_markdown_table
from loguru import logger

from langchain.callbacks.base import AsyncCallbackHandler

class LoggingCallbackHandler(AsyncCallbackHandler):
    async def on_llm_start(self, *args, **kwargs):
        logger.info(args[1][0])

    async def on_llm_end(self, response, **kwargs):
        generations = response.generations
        if generations and generations[0]:
            reply = generations[0][0].text
            logger.info(f"[LLM Response] >>>\n{reply}")

class RAGClient:
    def __init__(self, query:str):
        self.llm = gen_llm()
        self.table_name_chain = table_name_chain(self.llm)
        self.sql_generate_chain = sql_generate_chain(self.llm)
        self.graph_type_chain = graph_type_chain(self.llm)
        self.query = query

    async def get_table_name(self):
        tables = get_table_info(session)
        table_names = [table.get('table_name') for table in tables]
        table_names = ", ".join(table_names)

        table_aliases = get_table_alias(session)
        table_aliases = [f"原名：{alias.get('table_name')}，别名：{alias.get('table_alias')}" for alias in table_aliases]
        table_aliases = "\n".join(table_aliases)

        rules = get_prompt_rule(session, step_type="tablename")
        rules = [f"{id + 1}.{rule.get('content')}" for id, rule in enumerate(rules)]
        rules = "\n".join(rules)

        llm_response = await self.table_name_chain.arun({
                'query': self.query,
                'table_aliases': table_aliases,
                'table_names': table_names,
                'rules': rules
            },
            callbacks=[LoggingCallbackHandler()]
        )
        self.table_name = llm_response
        return self.table_name
    
    async def generate_sql(self):
        rules = get_prompt_rule(session, step_type="sql")
        rules = [f"{id}.{rule.get('content')}" for id, rule in enumerate(rules)]
        rules = "\n".join(rules)

        table_info = get_table_info(session, table_name=self.table_name)[0]
        assert table_info is not None, f"Table {self.table_name} not found in database."

        table_head = execute_sql(f'SELECT * FROM {self.table_name} LIMIT 3;')
        table_head = table_head.mappings().all()
        table_head = dicts_to_markdown_table(table_head)

        related_doc = query_document(self.query, 3)
        related_doc = '\n'.join(related_doc['documents'][0])

        llm_response = await self.sql_generate_chain.arun({
                'query': self.query,
                'table_name': self.table_name,
                'table_def_sql': table_info['table_define_sql'],
                'table_head': table_head,
                'table_field_info': table_info['table_field_info'],
                'related_doc': related_doc,
                'rules': rules
            },
            callbacks=[LoggingCallbackHandler()]
        )

        self.sql = llm_response
        return self.sql
    
    def load_data(self):
        try:
            self.data = load_data_to_df(self.sql)
            logger.info(f"data: {self.data}")
            return self.data
        except Exception as e:
            print(e)
            return None

    async def generate_graph(self):
        rules = get_prompt_rule(session, step_type="graph")
        rules = [f"{id}.{rule.get('content')}" for id, rule in enumerate(rules)]
        rules = "\n".join(rules)

        llm_response = await self.graph_type_chain.arun({
                'query': self.query,
                'data_schema': self.data.head(),
                'rules': rules
            },
            callbacks=[LoggingCallbackHandler()]
        ) 

        context = {
            'data': self.data,
            'fig': None
        }
        print('llm_response', llm_response)
        exec(llm_response, context)

        logger.info(f"graph: \n{context['fig']}")

        return context['fig'].to_plotly_json()