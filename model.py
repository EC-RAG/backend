from chains import table_name_chain, field_name_chain, sql_generate_chain
from chains.tools import table_name_tool
from chains.documents import database_document
from chains.tools import execute_sql
from utils.table_info import get_table_info
from utils import dicts_to_markdown_table

def get_table_name(query:str):
    llm_response = table_name_chain.invoke({
        'query': query
    })

    vague_table_name = llm_response['text']
    table_name = table_name_tool.invoke(vague_table_name)
    return table_name

def get_filed_name(query:str, table_name:str):
    table_info = database_document[table_name]
    llm_response = field_name_chain.invoke({
        'query': query,
        'name': table_info['name'],
        'text': table_info['text'],
        'important': table_info['important'],
        'knowledge': table_info['knowledge']
    })

    return llm_response['text']
    

def generate_sql(query:str, table_name:str):
    table_info = get_table_info(table_name)

    # 表头 + 前三行
    table_head = execute_sql(f'SELECT * FROM {table_name} LIMIT 3;')
    table_head = table_head.mappings().all()
    table_head = dicts_to_markdown_table(table_head)

    llm_response = sql_generate_chain.invoke({
        'query': query,
        'table_name': table_name,
        'table_def_sql': table_info['table_define_sql'],
        'table_head': table_head,
        'table_field_info': table_info['table_field_info'],
    })
    return llm_response['text']
    