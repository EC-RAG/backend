from tools.mysql import MysqlTool

from sqlalchemy import text

test = MysqlTool()

query = text('select * from summary_data_day')

for row in test._run(query):
    print(row)