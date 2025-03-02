from langchain.agents import tool

from db.base import SessionLocal

@tool(description='执行sql语句')
def execute_sql(sql:str):
    try:
        db = SessionLocal()
        result = db.execute(sql)
        return result
    except Exception as e:
        return e
    finally:
        db.close()