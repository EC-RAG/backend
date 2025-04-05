import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..")))

from db.vectordatabase import table_name_collection, embedding

datas = [
    {'ids': '概览数据（日）', 'document': 'summary_data_day'},
    {'ids': '概览数据日表', 'document': 'summary_data_day'},
    {'ids': '概览数据(月)', 'document': 'summary_data_month'},
    {'ids': '概览数据月表', 'document': 'summary_data_month'},
]

# for data in datas:
#     table_name_collection.add(**data)


# print(table_name_collection.get(ids=["概览数据（日）"]))
print(table_name_collection.get_all("summary_data_day"))
# print(embedding.embedding("概览数据（日）"))
# query = '概览数据月'
# query_embedding = embedding.embedding(query)
# result = table_name_collection.query(query_embedding, n_results=3)
# print(result)