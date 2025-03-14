import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from db.mysql.base import SessionLocal, Base, engine
from models.model import Summary_Data_Day
import pandas as pd

db = SessionLocal()

def get_csv(file_name:str):
    '''
    file_name: str  文件名
    '''
    PATH = os.path.join('init_scripts', 'sqldata','data', file_name)
    with open(PATH, 'r', encoding='utf-8') as f:
        data = pd.read_csv(f)
    return data

def trans_summary_day(source_data:pd.DataFrame)->pd.DataFrame:
    '''
    source_data: pd.DataFrame  概览数据（日） 原始数据
    '''
    reflect_dict = {
        '直播间名称': 's_name',
        '日期': 'date',
        '直播时长(小时)': 'live_duration',
        '带货商品数': 'goods_num',
        '成交金额': 'transaction_amount',
        '时均GMV': 'GMV_per_hour',
        '有效GMV': 'GMV_vaild',
        '时均有效GMV': 'GMV_vaild_per_hour',
        '成交订单数': 'completed_orders',
        '成交件数': 'completed_items',
        '成交人数': 'completed_people',
        '直播间退款金额': 'refund_number',
        '直播间订单退款人数': 'refund_people',
        '预估佣金收入': 'estimated_commission',
        '成交件单价': 'completed_price_pre_item',
        '预售订单数': 'presale_orders',
        '预售创建金额': 'presale_price',
        '退款率': 'refund_rate',
        '成交金额(订单)': 'completed_order',
        '退款金额(订单)': 'refund_order',
        '有效GMV(订单)': 'GMV_vaild_order',
        '时均有效GMV(订单)': 'GMV_vaild_order_pre_hour',
        '退款率(订单)': 'refund_rate_order',
        '发货前退款金额(订单）': 'refund_number_order_before_send',
        '有效投产净值(订单)': 'vaild_worthnet_order',
        '直播间观看人数': 'watch_people',
        '发货后退款金额(订单）': 'refund_number_order_after_send',
        '发货前退款率(订单)': 'refund_rate_order_before_send',
        '发货后退款率(订单)': 'refund_rate_order_after_send',
        '直播间观看人次': 'watch_times',
        '最高在线人数': 'highest_online',
        '平均在线人数': 'average_online',
        '人均看播时长': 'average_online_time',
        '评论次数': 'comment_times',
        '点赞次数': 'faverate_times',
        '分享次数': 'share_times',
        '新增粉丝数': 'follows',
        '新加团人数': 'new_group_fans',
        '取关粉丝数': 'unfollows',
        '看播粉丝占比': 'follows_rate_watch',
        '成交粉丝占比': 'follows_rate_order',
        '商品曝光人数': 'goods_exposure',
        '商品点击人数': 'goods_click',
        '商品点击率(人数)': 'goods_click_rate',
        '观看成交转化率(人数)': 'watch_to_order',
        '点击成交转化率(次数)': 'click_to_order',
        '直播间观看-互动率(人数)': 'interactive_rate',
        '投放消耗': 'ad_fee'
    }
    data = source_data[reflect_dict.keys()]
    data = data.rename(columns=reflect_dict)
    return data

def summary_day_to_db(data:pd.DataFrame):
    '''
    data: pd.DataFrame  概览数据（日） 数据
    '''
    Base.metadata.create_all(bind=engine)
    data.to_sql('summary_data_day', con=engine, if_exists='replace', index=False)


if __name__ == '__main__':
    source_data = get_csv('summary_data_day.csv')
    data = trans_summary_day(source_data)
    summary_day_to_db(data) 