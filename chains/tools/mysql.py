from langchain.agents import tool

from db.mysql.base import SessionLocal

from sqlalchemy import text

@tool(description='执行sql语句')
def execute_sql(sql:str):
    try:
        db = SessionLocal()
        result = db.execute(text(sql))
        return result
    except Exception as e:
        return e
    finally:
        db.close()