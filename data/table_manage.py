# tool func for table meatadata management

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db.vectordatabase import table_name_collection
from db.sqlite import conn

def get_all_table():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM table_info")
        all_table = cursor.fetchall()
        all_table = [dict(zip(['table_name', 'table_define_sql', 'table_field_info'], table)) for table in all_table]
    except Exception as e:
        print(e)
    finally:
        cursor.close()
    return all_table
    
def get_table_info(table_name:str):
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM table_info WHERE table_name = '{table_name}'")
        table_info = cursor.fetchone()
        table_info = dict(zip(['table_name', 'table_define_sql', 'table_field_info'], table_info))
    except Exception as e:
        print(e)
    finally:
        cursor.close()
    return table_info

def add_table_info(table_name:str, table_define_sql:str, table_field_info:str)->bool:
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO table_info (table_name, table_define_sql, table_field_info) VALUES ('{table_name}', '{table_define_sql}', '{table_field_info}')")
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
    return True

def remove_table_info(table_name:str)->bool:
    try:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM table_info WHERE table_name = '{table_name}'")
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
    return True

def get_table_alias(table_name:str):
    try:
        table_alias = table_name_collection.get_all(table_name)
    except Exception as e:
        print(e)
    finally:
        table_name_collection.close()
    return table_alias

def update_table_info(table_name:str, table_define_sql:str, table_field_info:str)->bool:
    try:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE table_info SET table_define_sql = '{table_define_sql}', table_field_info = '{table_field_info}' WHERE table_name = '{table_name}'")
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
    return True