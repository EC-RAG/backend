import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from db.sqlite import engine, TableInfo, session

# 数据概览（日表）
table = TableInfo(
    table_name='summary_data_day',
    table_define_sql='''
CREATE TABLE summary_data_day (
    s_name VARCHAR(255) NOT NULL,
    date DATETIME NOT NULL,
    live_duration DECIMAL(5,2),
    goods_num INT,
    transaction_amount DECIMAL(10,2),
    GMV_per_hour DECIMAL(10,2),
    GMV_vaild DECIMAL(10,2),
    GMV_vaild_per_hour DECIMAL(10,2),
    completed_orders INT,
    completed_items INT,
    completed_people INT,
    refund_number DECIMAL(10,2),
    refund_people INT,
    estimated_commission DECIMAL(10,2),
    completed_price_pre_item DECIMAL(10,2),
    presale_orders INT,
    presale_price DECIMAL(10,2),
    refund_rate DECIMAL(5,2),
    completed_order DECIMAL(10,2),
    refund_order DECIMAL(10,2),
    GMV_vaild_order DECIMAL(10,2),
    GMV_vaild_order_pre_hour DECIMAL(10,2),
    refund_rate_order DECIMAL(5,2),
    refund_number_order_before_send DECIMAL(10,2),
    vaild_worthnet_order DECIMAL(10,2),
    watch_people INT,
    refund_number_order_after_send DECIMAL(10,2),
    refund_rate_order_before_send DECIMAL(5,2),
    refund_rate_order_after_send DECIMAL(5,2),
    watch_times INT,
    highest_online INT,
    average_online INT,
    average_online_time DECIMAL(5,2),
    comment_times INT,
    faverate_times INT,
    share_times INT,
    follows INT,
    new_group_fans INT,
    unfollows INT,
    follows_rate_watch DECIMAL(5,2),
    follows_rate_order DECIMAL(5,2),
    goods_exposure INT,
    goods_click INT,
    goods_click_rate DECIMAL(5,2),
    watch_to_order DECIMAL(5,2),
    click_to_order DECIMAL(5,2),
    interactive_rate DECIMAL(5,2),
    ad_fee DECIMAL(10,2),
    PRIMARY KEY (s_name, date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
''',
    table_field_info='''
summary_data_day 是概览数据（日）的表，里面包含下面几个字段：
- 直播间名称 (s_name): 直播间名称 | varchar(255) | primary key
- 日期 (date): 记录日期 | datatime | primary key
- 直播时长(小时) (live_duration): 当日该直播间的直播时长 | float
- 带货商品数 (goods_num): 当日该直播间带货商品数 | int
- 成交金额 (transaction_amount): 当日该直播间成交金额 | float
- 时均GMV (GMV_per_hour): 时均商品交易总额 | float
- 有效GMV (GMV_vaild): 当日有效商品交易总额 | float
- 时均有效GMV (GMV_vaild_per_hour): 时均有效商品交易总额 | float
- 成交订单数 (completed_orders): 当日该直播间成交订单数 | int
- 成交件数 (completed_items): 当日该直播间成交商品件数 | int
- 成交人数 (completed_people): 当日该直播间成交人数 | int
- 直播间退款金额 (refund_number): 当日该直播间退款金额 | float
- 直播间订单退款人数 (refund_people): 当日该直播间订单退款人数 | int
- 预估佣金收入 (estimated_commission): 预估佣金收入 | float
- 成交件单价 (completed_price_pre_item): 成交件单价 | float
- 预售订单数 (presale_orders): 预售订单数 | int
- 预售创建金额 (presale_price): 预售创建金额 | float
- 退款率 (refund_rate): 退款率 | float
- 成交金额(订单) (completed_order): 成交金额 | float
- 退款金额(订单) (refund_order): 退款金额 | float
- 有效GMV(订单) (GMV_vaild_order): 有效商品交易总额 | float
- 时均有效GMV(订单) (GMV_vaild_order_pre_hour): 时均有效商品交易总额 | float
- 退款率(订单) (refund_rate_order): 退款率 | float
- 发货前退款金额(订单） (refund_number_order_before_send): 发货前退款金额 | float
- 有效投产净值(订单) (vaild_worthnet_order): 有效投产净值 | float
- 直播间观看人数 (watch_people): 直播间观看人数 | int
- 发货后退款金额(订单） (refund_number_order_after_send): 发货后退款金额 | float
- 发货前退款率(订单) (refund_rate_order_before_send): 发货前退款率 | float
- 发货后退款率(订单) (refund_rate_order_after_send): 发货后退款率 | float
- 直播间观看人次 (watch_times): 直播间观看人次 | int
- 最高在线人数 (highest_online): 最高在线人数 | int
- 平均在线人数 (average_online): 平均在线人数 | int
- 人均看播时长 (average_online_time): 人均看播时长 | float
- 评论次数 (comment_times): 评论次数 | int
- 点赞次数 (faverate_times): 点赞次数 | int
- 分享次数 (share_times): 分享次数 | int
- 新增粉丝数 (follows): 新增粉丝数 | int
- 新加团人数 (new_group_fans): 新加团人数 | int
- 取关粉丝数 (unfollows): 取关粉丝数 | int
- 看播粉丝占比 (follows_rate_watch): 观众中是粉丝的比例 | float
- 成交粉丝占比 (follows_rate_order): 成交订单的用户中是粉丝的占比 | float
- 商品曝光人数 (goods_exposure): 商品曝光人数 | int
- 商品点击人数 (goods_click): 商品点击人数 | int
- 商品点击率(人数) (goods_click_rate): 直播间点击商品人数占观看人数的百分比 | float
- 观看成交转化率(人数) (watch_to_order): 观看成交转化率 根据观看人数 | float
- 点击成交转化率(次数) (click_to_order): 点击成交转化率 根据观看次数 | float
- 直播间观看-互动率(人数) (interactive_rate): 直播间互动人数占观看人数的百分比 | float
- 投放消耗 (ad_fee): 广告投放消耗 | float
'''
)

session.add(table)
session.commit()