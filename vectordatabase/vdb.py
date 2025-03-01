'''
vector database api
'''
import chromadb
from pathlib import Path


db_file = 'chromadb.db'

client = chromadb.PersistentClient(path=db_file)

