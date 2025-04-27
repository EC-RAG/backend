from typing import List
from fastapi import APIRouter, Depends, Query, Path, Response

from ..schemas.vdb_schema import *

from data.vector_data_manage import *

from utils.data import *

vdb_router = APIRouter(prefix="/vdb", tags=["vdb"])

def responsenize(data: dict) -> List[dict]:
    resp = dict_to_list(data, ['embeddings', 'metadatas', 'documents'])
    resp = [
        {
            'title': item['metadatas']['title'],
            'content': item['documents'],
            'index': item['metadatas']['index'],
            'embedding': item['embeddings']
        } for item in resp
    ]
    return resp

@vdb_router.get("/alldocslice", response_model=List[DocSliceResponse])
async def handle_get_all_docs():
    try:
        all_docs = get_all_documents_slice()
        all_docs = responsenize(all_docs)
    except Exception as e:
        return Response(content=e.__str__(), status_code=500)
    return all_docs

@vdb_router.get("/alldoc", response_model=List[DocResponse])
async def handle_get_all_docs():
    try:
        all_docs = get_all_documents()
    except Exception as e:
        return Response(content=e.__str__(), status_code=500)
    return all_docs

@vdb_router.get("/doc", response_model=List[DocSliceResponse])
async def handle_get_doc_by_title(title: str = Query(..., description="Document title to get")):
    try:
        documents = get_document_by_title(title)
        documents = responsenize(documents)
    except Exception as e:
        return Response(content=e.__str__(), status_code=500)
    return documents
    
@vdb_router.post("/adddoc", tags=["vdb"])
async def handle_add_doc(data: DocAddRequest):
    try:
        add_document(data.title, data.document)
    except Exception as e:
        return Response(content=e.__str__(), status_code=500)
    return True

@vdb_router.get("/rmdoc", tags=["vdb"])
async def handle_remove_doc(title: str = Query(..., description="Document title to remove")):
    try:
        delete_document(title)
    except Exception as e:
        return Response(content=e.__str__(), status_code=500)
    return True

@vdb_router.get("/querydoc", response_model=List[DocQueryResponse])
async def handle_query_doc(query: str = Query(..., description="Query string to search for")):
    try:
        documents = query_document(query)
        documents['metadatas'] = documents['metadatas'][0]
        documents['documents'] = documents['documents'][0]
        documents['distances'] = documents['distances'][0]
        resp = dict_to_list(documents, ['distances', 'metadatas', 'documents'])
        resp = [
            {
                'title': item['metadatas']['title'],
                'content': item['documents'],
                'index': item['metadatas']['index'],
                'distance': item['distances']
            } for item in resp
        ]
    except Exception as e:
        return Response(content=e.__str__(), status_code=500)
    return resp