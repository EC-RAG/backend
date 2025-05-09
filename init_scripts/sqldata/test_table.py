import pandas as pd

columns = [
    '店铺名','日期',
    'A类商品销售量', 'A类商品销售额','A类商品退款量','A类商品退款额', 'A类商品退款率',
    'B类商品销售量', 'B类商品销售额','B类商品退款量','B类商品退款额', 'B类商品退款率',
    'C类商品销售量', 'C类商品销售额','C类商品退款量','C类商品退款额', 'C类商品退款率',
    '总体销售量', '总体销售额','总体退款量','总体退款额', '总体退款率'
    ]

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from chains.tools.mysql import execute_sql

# 字段映射表
field_mapping = {
    '店铺名': 'shop_name',
    '日期': 'date',
    'A类商品销售量': 'A_sales_volume',
    'A类商品销售额': 'A_sales_amount',
    'A类商品退款量': 'A_refund_volume',
    'A类商品退款额': 'A_refund_amount',
    'A类商品退款率': 'A_refund_rate',
    'B类商品销售量': 'B_sales_volume',
    'B类商品销售额': 'B_sales_amount',
    'B类商品退款量': 'B_refund_volume',
    'B类商品退款额': 'B_refund_amount',
    'B类商品退款率': 'B_refund_rate',
    'C类商品销售量': 'C_sales_volume',
    'C类商品销售额': 'C_sales_amount',
    'C类商品退款量': 'C_refund_volume',
    'C类商品退款额': 'C_refund_amount',
    'C类商品退款率': 'C_refund_rate',
    '总体销售量': 'total_sales_volume',
    '总体销售额': 'total_sales_amount',
    '总体退款量': 'total_refund_volume',
    '总体退款额': 'total_refund_amount',
    '总体退款率': 'total_refund_rate'
}

# 表定义sql
create_table_sql = """
CREATE TABLE IF NOT EXISTS test_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    shop_name VARCHAR(255),
    date DATE,
    A_sales_volume INT,
    A_sales_amount DECIMAL(10, 2),
    A_refund_volume INT,
    A_refund_amount DECIMAL(10, 2),
    A_refund_rate DECIMAL(5, 2),
    B_sales_volume INT,
    B_sales_amount DECIMAL(10, 2),
    B_refund_volume INT,
    B_refund_amount DECIMAL(10, 2),
    B_refund_rate DECIMAL(5, 2),
    C_sales_volume INT,
    C_sales_amount DECIMAL(10, 2),
    C_refund_volume INT,
    C_refund_amount DECIMAL(10, 2),
    C_refund_rate DECIMAL(5, 2),
    total_sales_volume INT,
    total_sales_amount DECIMAL(10, 2),
    total_refund_volume INT,
    total_refund_amount DECIMAL(10, 2),
    total_refund_rate DECIMAL(5, 2)
);
"""

import random
from datetime import datetime, timedelta
start_date = datetime(2024, 4, 1)
end_date = datetime(2024, 4, 30)
date_list = [(start_date + timedelta(days=i)).date() for i in range((end_date - start_date).days + 1)]

# 店铺列表
shops = ['店铺A', '店铺B', '店铺C']

data = []
for shop in shops:
    for date in date_list:
        row = [shop, date]
        total_sales_volume = 0
        total_sales_amount = 0
        total_refund_volume = 0
        total_refund_amount = 0
        for _ in ['A', 'B', 'C']:
            sales_volume = random.randint(50, 200)
            sales_amount = round(sales_volume * random.uniform(10, 30), 2)
            refund_volume = random.randint(0, int(sales_volume * 0.2))
            refund_amount = round(refund_volume * random.uniform(10, 30), 2)
            refund_rate = round(refund_volume / sales_volume, 2) if sales_volume > 0 else 0

            row.extend([sales_volume, sales_amount, refund_volume, refund_amount, refund_rate])

            total_sales_volume += sales_volume
            total_sales_amount += sales_amount
            total_refund_volume += refund_volume
            total_refund_amount += refund_amount

        total_refund_rate = round(total_refund_volume / total_sales_volume, 2) if total_sales_volume > 0 else 0
        row.extend([total_sales_volume, round(total_sales_amount, 2),
                    total_refund_volume, round(total_refund_amount, 2),
                    total_refund_rate])
        data.append(row)

# 生成 DataFrame
df = pd.DataFrame(data, columns=columns)

# 替换列名
for col in df.columns:
    if col in field_mapping:
        df.rename(columns={col: field_mapping[col]}, inplace=True)

pd.set_option('display.max_columns', None)     # 显示所有列
pd.set_option('display.width', 120)            # 控制控制台输出宽度
pd.set_option('display.max_colwidth', 20)      # 每列最多显示字符数
pd.set_option('display.precision', 2)          # 控制小数精度

from db.mysql.base import engine

execute_sql(create_table_sql)
df.to_sql('test_table', con=engine, if_exists='replace', index=False)