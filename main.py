# from model import generate_sql, get_table_name

# def mian():
#     query = '查询奥利奥官方旗舰店的日销售额'
#     table_name = get_table_name(query)
#     sql = generate_sql(query, table_name)
#     print(sql)

# mian()
import uvicorn

from app.app import app

if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True, workers=1)