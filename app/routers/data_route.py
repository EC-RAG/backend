from typing import List
from fastapi import APIRouter, Depends, Query, Path, Response

from ..schemas.data_schema import TableData

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from data.table_manage import get_all_table, add_table_info, remove_table_info, update_table_info, get_all_table_alias_in_vdb, get_all_table_invdb

data_router = APIRouter(prefix="/data")

@data_router.get("/all", response_model=List[TableData], tags=["data"])
async def get_all_tables():
    return get_all_table()

@data_router.post("/addtable", tags=["data"])
async def add_table(data: TableData):
    try:
        add_table_info(data.table_name, data.table_define_sql, data.table_field_info)
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return True

@data_router.get("/rmtable", tags=["data"])
async def remove_table(table_name: str = Query(..., description="Table name to remove")):
    try:
        remove_table_info(table_name)
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return True

@data_router.post("/edittable", tags=["data"])
async def update_table(data: TableData):
    try:
        update_table_info(data.table_name, data.table_define_sql, data.table_field_info)
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return True

@data_router.get("/gettable", tags=["data"])
async def get_table(table_name: str = Query(..., description="Table name to get")):
    try:
        table_info = get_all_table()
        target_tables = []
        for table in table_info:
            if table_name in table['table_name']:
                target_tables.append(table)
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return target_tables

@data_router.get("/gettablefield", tags=["data"])
async def get_table_field():
    try:
        table_alias = get_all_table_alias_in_vdb()
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return table_alias

@data_router.get("/gettabletags", response_model=list[str], tags=["data"])
async def get_table_tags():
    try:
        tags = get_all_table_invdb()
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return tags