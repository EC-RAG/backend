# from model import generate_sql, get_table_name

# def mian():
#     query = '查询奥利奥官方旗舰店的日销售额'
#     table_name = get_table_name(query)
#     sql = generate_sql(query, table_name)
#     print(sql)

# mian()
import uvicorn

import os
os.environ["LANGCHAIN_API_DISABLED"] = "true"

from utils.load import check_frontend

# check_frontend()

from app.app import app

from fastapi.staticfiles import StaticFiles

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

if __name__ == '__main__':
    # 获取环境变量
    env = os.getenv("ENV", "development")  # 默认值为 "production"

    # 根据环境变量设置 reload 参数
    reload = env == "development"
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=reload, workers=None)
