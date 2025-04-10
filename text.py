from model import generate_sql, get_table_name, load_data, generate_graph

def mian():
    query = '查询奥利奥官方旗舰店的日销售额'
    table_name = get_table_name(query)
    sql = generate_sql(query, table_name)
    data = load_data(table_name, sql)
    res = generate_graph(query, data)
    print(res)

mian()
