from db.sqlite import conn

# cursor = conn.cursor()

def get_table_info(table_name:str):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM table_info WHERE table_name = '{table_name}'")
        table_info = cursor.fetchone()
        table_info = dict(zip(['table_name', 'table_define_sql', 'table_field_info'], table_info))
    except Exception as e:
        raise e
    finally:
        cursor.close()
    return table_info
