import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from db.sqlite import session
from data.sql_data_manage import create_prompt_rule

create_prompt_rule_system = lambda rule, step: create_prompt_rule(session, step_type=step, level='system', content=rule)


table_name_rules = [
    '输出的表名必须是系统中存在的表名，不能是其他表名',
    '输出只能是表名，不需要其他内容',
]

sql_rules = [
    '括号中带订单的数据是指订单数据，默认选择订单数据，订单数据和非订单数据只需要选择一个',
    '无论如何都要保证选择直播间名称和日期两个字段',
    '根据用户查询的需求，选择对应的字段，尽可能选取相关的字段，但是不要选取无关的字段，对于大多数查询，只需要选择一个最相关的字段即可',
    '一般来说一个查询只会用到不多于5个字段，所以不要选择太多的字段',
    '请注意避免重复选择相同的字段',
    '请只生成SQL语句，不要添加其他的内容，也不要添加注释，也不需要markdown的格式标记',
    '使用as关键字来给字段添加中文名，每个字段都需要',
    'sql语句尽量换行，保持格式整齐'
]

graph_rules = [
    '已知数据以dataframe的格式存储在变量data中',
    '使用Plotly Express库进行可视化',
    '回答中只需要给出代码，无需解释，也不需要markdown格式标记',
    '生成的图表对象名为fig，无需调用show()方法',
    '请导入必要的库',
    '如果是数值类数据，请确保横纵坐标按序列排列'
]

list(map(lambda rule: create_prompt_rule_system(rule, step='tablename'), table_name_rules))
list(map(lambda rule: create_prompt_rule_system(rule, step='sql'), sql_rules))
list(map(lambda rule: create_prompt_rule_system(rule, step='graph'), graph_rules))