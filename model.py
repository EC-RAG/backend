from chains import table_name_chain, field_name_chain, sql_generate_chain
from chains.tools import table_name_tool
from chains.documents import database_document
from utils.table_info import get_table_info

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
    llm_response = sql_generate_chain.invoke({
        'query': query,
        'table_name': table_name,
        'table_def_sql': table_info['table_define_sql'],
        'table_field_info': table_info['table_field_info'],
    })
    return llm_response['text']
    