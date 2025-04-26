from pydantic import BaseModel

from datetime import datetime

class TableData(BaseModel):
    table_name: str
    table_define_sql: str
    table_field_info: str

class AliasData(BaseModel):
    id: int
    table_name: str
    table_alias: str
    level: str
    create_at: datetime

class TableAliasCreate(BaseModel):
    table_name: str
    table_alias: str

class TableAliasUpdate(BaseModel):
    id: int
    table_name: str
    table_alias: str

class RuleData(BaseModel):
    id: int
    step_type: str
    level: str
    content: str
    create_at: datetime

class RuleCreate(BaseModel):
    step_type: str
    content: str

class RuleUpdate(BaseModel):
    id: int
    step_type: str
    content: str