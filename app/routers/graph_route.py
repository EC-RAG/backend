from typing import List
from fastapi import APIRouter, Depends, Query, Path, Response, WebSocket, WebSocketDisconnect

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from model import generate_sql, get_table_name, load_data, generate_graph
from utils.data import convert_array_to_list
from utils.async_func import run_sync

graph_router = APIRouter(prefix="/graph")

# @graph_router.get("/get")
# def gen_graph(query: str = Query(..., description="Query string to search for"),):
    

#     query = '查询奥利奥官方旗舰店的日销售额'
#     table_name = get_table_name(query)
#     sql = generate_sql(query, table_name)
#     data = load_data(table_name, sql)
#     res = generate_graph(query, data)
#     res = convert_array_to_list(res)
#     return res

@graph_router.websocket("/ragstream")
async def gen_graph(ws: WebSocket):
    await ws.accept()
    try:
        query = await ws.receive_text()
        table_name = await get_table_name(query)
        await ws.send_json({"table_name": table_name})
        sql = await generate_sql(query, table_name)
        await ws.send_json({"sql": sql})
        data = load_data(table_name, sql)
        await ws.send_json({"data": data.head().to_json(orient="records", force_ascii=False)})
        res = await generate_graph(query, data)
        res = convert_array_to_list(res)
        await ws.send_json(res)
    except Exception as e:
        raise e
    finally:
        await ws.close()
