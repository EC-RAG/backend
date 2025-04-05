from .vdb import client, Item, BaseCollection

create_collection_class = lambda name, elements: type(f"{name}Collection", (BaseCollection,), {
    "__init__": lambda self, client: BaseCollection.__init__(self, name, client),
    **elements
})

table_name_collection:BaseCollection = create_collection_class(
    "table_name",
    {
        "add": lambda self, ids, document: self._add(Item(ids, document, metadata={"type": "table_name", "table": document})),
    }
)(client)