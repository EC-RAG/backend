from chains import table_name_chain, sql_generate_chain, graph_type_chain
from chains.tools import table_name_tool
from chains.tools import execute_sql
from utils import dicts_to_markdown_table
from data.sql_data_manage import get_table_info
from db.sqlite import session

from data import load_data_to_df

import pandas as pd

async def get_table_name(query:str):
    llm_response = await table_name_chain.arun({
        'query': query
    })
    vague_table_name = llm_response
    table_name = table_name_tool.invoke(vague_table_name)
    return table_name

async def generate_sql(query:str, table_name:str):
    table_info = get_table_info(session, table_name)

    # 表头 + 前三行
    table_head = execute_sql(f'SELECT * FROM {table_name} LIMIT 3;')
    table_head = table_head.mappings().all()
    table_head = dicts_to_markdown_table(table_head)

    llm_response = await sql_generate_chain.arun({
        'query': query,
        'table_name': table_name,
        'table_def_sql': table_info['table_define_sql'],
        'table_head': table_head,
        'table_field_info': table_info['table_field_info'],
    })
    return llm_response


def load_data(table_name:str, sql:str):
    try:
        data = load_data_to_df(sql)
        return data
    except Exception as e:
        print(e)
        return None
    
async def generate_graph(query:str, data:pd.DataFrame):
    llm_response = await graph_type_chain.arun({
        'query': query,
        'data_schema': data.head()
    })
    context = {
        'data':data,
        'fig': None
    }
    print('llm_response', llm_response)
    exec(llm_response, context)
    return context['fig'].to_plotly_json()