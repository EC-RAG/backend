import os
import enum
from datetime import datetime

from sqlalchemy import create_engine, Column, String, Text, DateTime, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.types import Enum

from utils.config import config

# 创建数据库引擎
db_path = os.path.join(config['data_path'], 'server.db')
engine = create_engine(f"sqlite:///{db_path}", echo=True)

# 创建基础类
Base = declarative_base()

class Serialize:
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# 定义 TableInfo 模型
class TableInfo(Base, Serialize):
    __tablename__ = 'table_info'

    table_name = Column(String, primary_key=True)  # 表名
    table_define_sql = Column(Text, nullable=False)  # 表定义 SQL
    table_field_info = Column(Text, nullable=False)  # 表字段信息
    create_at = Column(DateTime, default=datetime.utcnow, nullable=False)  # 创建时间

    aliases = relationship("TableAlias", back_populates="table")

class RecordLevel(enum.Enum):
    system = "system"
    user = "user"

class TableAlias(Base, Serialize):
    __tablename__ = 'table_alias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    table_name = Column(String, ForeignKey('table_info.table_name'))  # 表名
    table_alias = Column(String, nullable=False)  # 表别名
    level = Column(Enum(RecordLevel, name='level_enum', native_enum=False), nullable=False) # 记录级别 system/user
    create_at = Column(DateTime, default=datetime.utcnow, nullable=False)  # 创建时间

    table = relationship("TableInfo", back_populates="aliases")

class StepType(enum.Enum):
    tablename = "tablename"
    sql = "sql"
    graph = "graph"

class PromptRule(Base, Serialize):
    __tablename__ = 'prompt_rule'

    id = Column(Integer, primary_key=True, autoincrement=True) # 主键
    step_type = Column(Enum(StepType, name='step_type_enum', native_enum=False), nullable=False)  # 步骤类型
    level = Column(Enum(RecordLevel, name='level_enum', native_enum=False), nullable=False)  # 记录级别 system/user
    content = Column(Text, nullable=False)  # 内容
    create_at = Column(DateTime, default=datetime.utcnow, nullable=False)  # 创建时间

Base.metadata.create_all(engine)

# 创建会话工厂
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()