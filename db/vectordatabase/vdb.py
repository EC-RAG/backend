'''
vector database api
'''
import chromadb
from pathlib import Path
from typing import Callable

from utils.config import config

from .embedding import embedding


db_file = config['database']['chromadb']['name']

client = chromadb.PersistentClient(path=db_file)

class Item:
    def __init__(self,ids:str ,documents:str ,embedding:Callable=embedding):
        self.ids = ids
        self.documents = documents
        self.embedding = embedding(ids)

    def to_dict(self):
        return {
            'ids': self.ids,
            'documents': self.documents,
            'embeddings': self.embedding
        }