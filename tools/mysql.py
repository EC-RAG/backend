from langchain.agents import Tool

from db.base import SessionLocal

class mysql(Tool):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self, *args, **kwargs):
        return super().run(*args, **kwargs)