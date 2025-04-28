import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from db.sqlite import session
from data.sql_data_manage import create_table_alias

create_table_alias_system = lambda table_name, alias: create_table_alias(session, table_name=table_name, table_alias=alias, level='system')

alias_list = [
    ('summary_data_day', '日表'),
    ('summary_data_day', '数据日表')
]

list(map(lambda alias: create_table_alias_system(alias[0], alias[1]), alias_list))