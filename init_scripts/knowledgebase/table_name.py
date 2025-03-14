import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db.vectordatabase.vdb import client, Item, embedding

collection = client.get_or_create_collection('table_name')

datas = [
    Item(ids='概览数据（日）', documents='summary_data_day'),
    Item(ids='概览数据日表', documents='summary_data_day'),
    Item(ids='概览数据(月)', documents='summary_data_month'),
    Item(ids='概览数据月表', documents='summary_data_month'),
]

for data in datas:
    collection.add(**data.to_dict())

# try
query = '概览数据(月)'
query_embedding = embedding(query)
result = collection.query(query_embedding, n_results=1)
print(result)
