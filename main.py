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

from loguru import logger
from datetime import datetime

logger.remove()
logger.add(
    f"logs/runtime_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log",    # 文件路径，可以使用时间等动态字段
    rotation="500 MB",            # 自动切割：文件超过 500MB 自动新建
    retention="10 days",          # 日志保留时间：超过 10 天自动删除
    compression="zip",            # 自动压缩旧日志
    level="INFO",                 # 日志等级过滤
    encoding="utf-8",             # 文件编码
    enqueue=True,                 # 多线程/多进程安全
    backtrace=True,               # 显示更完整的错误堆栈
    diagnose=True                 # 显示变量的详细值（建议开发时开启）
)

if __name__ == '__main__':
    # 获取环境变量
    env = os.getenv("ENV", "development")  # 默认值为 "production"

    # 根据环境变量设置 reload 参数
    reload = env == "development"
    uvicorn.run('main:app', host="0.0.0.0", port=8188, reload=reload, workers=None)
