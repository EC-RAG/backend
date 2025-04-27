from db.vectordatabase import document_collection

def get_all_documents_slice()-> dict:
    try:
        all_documents = document_collection.get_all()
        return all_documents
    except Exception as e:
        print(e)
        return None
    
def get_all_documents():
    try:
        doc_metadatas = get_all_documents_slice().get("metadatas")
        doc_names = set(map(lambda x: x["title"], doc_metadatas))
        all_docs = [
            {
                "title": doc_name,
                "slice_cnt": len(list(filter(lambda x: x["title"] == doc_name, doc_metadatas)))
            } for doc_name in doc_names
        ]
        return all_docs
    except Exception as e:
        print(e)
        return None

def get_document_by_title(title: str) -> dict:
    try:
        documents = document_collection.get(where={"title": title})
        return documents
    except Exception as e:
        print(e)
        return None

def add_document(title: str, document: str) -> bool:
    try:
        document_collection.add(title=title, document=document)
        return True
    except Exception as e:
        print(e)
        return False

def delete_document(title: str):
    try:
        docs = get_document_by_title(title)
        assert docs is not None
        list(map(lambda x: document_collection.delete(x), docs['ids']))
    except Exception as e:
        print(e)
        return False
    
def query_document(query: str, top_k: int = 2) -> dict:
    try:
        docs = document_collection.query(query, top_k)
        return docs
    except Exception as e:
        print(e)
        return None