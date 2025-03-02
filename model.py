from chains import table_name_chain
from tools import table_name_tool

def get_table_name(query:str):
    llm_response = table_name_chain.invoke({
        'query': query
    })

    vague_table_name = llm_response['text']
    table_name = table_name_tool.invoke(vague_table_name)
    return table_name

print(get_table_name('从数据日表中提取主播粉丝数'))