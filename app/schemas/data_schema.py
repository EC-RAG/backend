from pydantic import BaseModel

class TableData(BaseModel):
    table_name: str
    table_define_sql: str
    table_field_info: str

class TableAlias(BaseModel):
    id: str
    table_name: str
    table_alias: str
    level: str
    create_at: str

class TableAliasCreate(BaseModel):
    table_name: str
    table_alias: str

class RuleData(BaseModel):
    id: int
    step_type: str
    level: str
    content: str
    create_at: str

class RuleCreate(BaseModel):
    step_type: str
    content: str

class RuleUpdate(BaseModel):
    id: int
    step_type: str
    content: str