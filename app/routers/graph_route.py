from typing import List
from fastapi import APIRouter, Depends, Query, Path, Response, WebSocket, WebSocketDisconnect

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from chains.model import RAGClient
from utils.data import convert_array_to_list

graph_router = APIRouter(prefix="/graph")

@graph_router.websocket("/ragstream")
async def gen_graph(ws: WebSocket):
    await ws.accept()
    try:
        query = await ws.receive_text()
        client = RAGClient(query=query)
        table_name = await client.get_table_name()
        await ws.send_json({"type":'table_name',"data": table_name})
        sql = await client.generate_sql()
        await ws.send_json({"type":'sql',"data": sql})
        data = client.load_data()
        print(convert_array_to_list(data.head().to_dict()))
        await ws.send_json({"type":'data',"data": {"data": convert_array_to_list(data.head().to_dict())}})
        res = await client.generate_graph()
        res = convert_array_to_list(res)
        await ws.send_json({"type": 'graph', "data": res})
    except Exception as e:
        raise e
    finally:
        await ws.close()
