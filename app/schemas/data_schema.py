from pydantic import BaseModel

class TableData(BaseModel):
    table_name: str
    table_define_sql: str
    table_field_info: str