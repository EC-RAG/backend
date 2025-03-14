from db.sqlite import conn

cursor = conn.cursor()

def get_table_info(table_name:str):
    try:
        cursor.execute(f"SELECT * FROM table_info WHERE table_name = '{table_name}'")
        table_info = cursor.fetchone()
    except Exception as e:
        print(e)
    return table_info

def add_table_info(table_name:str, table_define_sql:str, table_field_info:str)->bool:
    try:
        cursor.execute(f"INSERT INTO table_info (table_name, table_define_sql, table_field_info) VALUES ('{table_name}', '{table_define_sql}', '{table_field_info}')")
        conn.commit()
    except Exception as e:
        print(e)
        return False
    return True