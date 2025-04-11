from model import generate_sql, get_table_name, load_data, generate_graph
import json

from utils.data import convert_array_to_list

def mian():
    query = '查询奥利奥官方旗舰店的日销售额'
    table_name = get_table_name(query)
    sql = generate_sql(query, table_name)
    data = load_data(table_name, sql)
    res = generate_graph(query, data)
    # res = res.to_plotly_json()
    res = convert_array_to_list(res)
    res = str(res).replace("'", "\"").replace("None", "null").replace("True", "true").replace("False", "false")
    print(res)
    res = json.loads(res)
    print(res)

mian()
