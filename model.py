from chains import table_name_chain, field_name_chain
from tools import table_name_tool
from chains.documents import database_document

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
    
