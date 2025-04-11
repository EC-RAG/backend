from typing import List
from fastapi import APIRouter, Depends, Query, Path, Response

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from model import generate_sql, get_table_name, load_data, generate_graph
from utils.data import convert_array_to_list

graph_router = APIRouter(prefix="/graph")

@graph_router.get("/get")
def gen_graph(query: str = Query(..., description="Query string to search for"),):
    

    query = '查询奥利奥官方旗舰店的日销售额'
    table_name = get_table_name(query)
    sql = generate_sql(query, table_name)
    data = load_data(table_name, sql)
    res = generate_graph(query, data)
    res = convert_array_to_list(res)
    return res