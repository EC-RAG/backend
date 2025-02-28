from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime

from db.base import Base

class Summary_Data_Day(Base):
    __tablename__ = 'summary_data_day'
    
    s_name = Column(String(255), primary_key=True)
    date = Column(DateTime, primary_key=True)
    live_duration = Column(Numeric(5, 2))
    goods_num = Column(Integer)
    transaction_amount = Column(Numeric(10, 2))
    GMV_per_hour = Column(Numeric(10, 2))
    GMV_vaild = Column(Numeric(10, 2))
    GMV_vaild_per_hour = Column(Numeric(10, 2))
    completed_orders = Column(Integer)
    completed_items = Column(Integer)
    completed_people = Column(Integer)
    refund_number = Column(Numeric(10, 2))
    refund_people = Column(Integer)
    estimated_commission = Column(Numeric(10, 2))
    completed_price_pre_item = Column(Numeric(10, 2))
    presale_orders = Column(Integer)
    presale_price = Column(Numeric(10, 2))
    refund_rate = Column(Numeric(5, 2))
    completed_order = Column(Numeric(10, 2))
    refund_order = Column(Numeric(10, 2))
    GMV_vaild_order = Column(Numeric(10, 2))
    GMV_vaild_order_pre_hour = Column(Numeric(10, 2))
    refund_rate_order = Column(Numeric(5, 2))
    refund_number_order_before_send = Column(Numeric(10, 2))
    vaild_worthnet_order = Column(Numeric(10, 2))
    watch_people = Column(Integer) 
    refund_number_order_after_send = Column(Numeric(10, 2))
    refund_rate_order_before_send = Column(Numeric(5, 2))
    refund_rate_order_after_send = Column(Numeric(5, 2))
    watch_times = Column(Integer)  # 观看人次
    highest_online = Column(Integer)  # 最高在线人数
    average_online = Column(Integer)  # 平均在线人数
    average_online_time = Column(Numeric(5, 2))  # 平均在线时长
    comment_times = Column(Integer)  # 评论次数
    faverate_times = Column(Integer)  # 点赞次数
    share_times = Column(Integer)  # 分享次数
    follows = Column(Integer)  # 新增粉丝数
    new_group_fans = Column(Integer)  # 新加团人数
    unfollows = Column(Integer)  # 取关人数
    follows_rate_watch = Column(Numeric(5, 2))  # 看播粉丝占比
    follows_rate_order = Column(Numeric(5, 2))  # 成交粉丝占比
    goods_exposure = Column(Integer)  # 商品曝光量
    goods_click = Column(Integer)  # 商品点击量
    goods_click_rate = Column(Numeric(5, 2))  # 商品点击率
    watch_to_order = Column(Numeric(5, 2))  # 观看成交转化率
    click_to_order = Column(Numeric(5, 2))  # 点击成交转化率
    interactive_rate = Column(Numeric(5, 2))  # 互动率
    ad_fee = Column(Numeric(10, 2))  # 广告费用