from .vdb import client, Item, BaseCollection
from utils.data import text_split

create_collection_class = lambda name, elements: type(f"{name}Collection", (BaseCollection,), {
    "__init__": lambda self, client: BaseCollection.__init__(self, name, client),
    **elements
})

table_name_collection:BaseCollection = create_collection_class(
    "table_name",
    {
        "add": lambda self, ids, document: self._add(Item(ids, document, metadata={"type": "table_name", "table": document})),
        "get_all": lambda self, table_name, **kwargs: self.get(where={"table": table_name}, **kwargs)
    }
)(client)

document_collection:BaseCollection = create_collection_class(
    "document",
    {
        "add": lambda self, title, document: list(map(
            lambda x: self._add(Item(title + str(x[0]), x[1], metadata={"type": "document", "title": title, "index": x[0]})), 
            enumerate(text_split(document))
        )),
        "get_all": lambda self, **kwargs: self.get(where={"type": 'document'}, **kwargs),
    }
)(client)