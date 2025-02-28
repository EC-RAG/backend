from langchain.agents import Tool

from db.base import SessionLocal

class MysqlTool(Tool):
    def __init__(self, *args, **kwargs):
        pass

    def _run(self, sql:str):
        try:
            db = SessionLocal()
            result = db.execute(sql)
            return result
        except Exception as e:
            return e
        finally:
            db.close()
    