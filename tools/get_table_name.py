from vectordatabase.vdb import client, embedding
from langchain.agents import tool

@tool(description='通过大模型提取表明，在向量数据库中查询')
def get_table_name(query:str):
    collection = client.get_or_create_collection('table_name')
    query_embedding = embedding(query)
    result = collection.query(query_embedding, n_results=1)
    return result['documents'][0][0]