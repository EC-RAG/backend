from pydantic import BaseModel

class TableData(BaseModel):
    table_name: str
    table_define_sql: str
    table_field_info: str

class TableAlias(BaseModel):
    id: str
    embedding: list[float]
    document: str
    metadata: dict

class AliasQuery(BaseModel):
    query: str
    top_k: int

class TableAliasResponse(BaseModel):
    id: str
    distance: float
    document: str
    metadata: dict
