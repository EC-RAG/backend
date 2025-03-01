from langchain.agents import tool

from db.base import SessionLocal

@tool(name='execute_sql', description='execute sql')
def execute_sql(sql:str):
    try:
        db = SessionLocal()
        result = db.execute(sql)
        return result
    except Exception as e:
        return e
    finally:
        db.close()