import sqlite3
# 连接到 SQLite 数据库（如果文件不存在，则创建）
conn = sqlite3.connect("server.db")
# 创建游标（Cursor）对象
cursor = conn.cursor()

# 如果表信息表不存在，则创建
cursor.execute('''
CREATE TABLE IF NOT EXISTS table_info (
    table_name TEXT PRIMARY KEY,
    table_define_sql TEXT NOT NULL,
    table_field_info TEXT NOT NULL
);
''')

conn.commit()