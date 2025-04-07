from typing import List
from fastapi import APIRouter, Depends, Query, Path, Response

from ..schemas.data_schema import TableData, TableAlias, AliasQuery, TableAliasResponse

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from data.table_manage import get_all_table, add_table_info, remove_table_info, update_table_info, get_all_table_alias_in_vdb, \
    get_all_table_invdb, get_table_alias, table_name_collection

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

@data_router.get("/allalias", response_model=List[TableAlias], tags=["data"])
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

@data_router.get("/gettablealias", response_model=List[TableAlias], tags=["data"])
async def table_alias(table_name: str = Query(..., description="Table name to get alias")):
    try:
        table_alias = get_table_alias(table_name)
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return table_alias

@data_router.get("/rmalias", tags=["data"])
async def remove_alias(table_name: str = Query(..., description="Table name to remove alias")):
    try:
        table_name_collection.delete(table_name)
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return True

@data_router.get("/addalias", tags=["data"])
async def add_alias(table_name: str = Query(..., description="Table name to add alias"),
                    table_alias: str = Query(..., description="Table alias")):
    try:
        table_name_collection.add(table_name, table_alias)
    except Exception as e:
        return Response(content=e.__str__, status_code=500)
    return True

@data_router.get("/aliasquery", response_model=List[TableAliasResponse],tags=["data"])
async def alias_query(query: str = Query(..., description="Query to search for table alias"),
                      top_k: int = Query(2, description="Number of top results to return")):
    query_result = table_name_collection.query(query, n_results=top_k)
    items = []
    for i in range(len(query_result['ids'][0])):
        item = {
            'id': query_result['ids'][0][i],
            'distance': query_result['distances'][0][i],
            'document': query_result['documents'][0][i],
            'metadata': query_result['metadatas'][0][i],
        }
        print(item)
    return items