from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

# 连接信息
engine = create_engine("mysql+pymysql://root:Mysql123$@localhost:3306/my_db", encoding="utf-8", echo=True,
                       max_overflow=5)

#  表信息
base = declarative_base()


class TableJob(base):
    __tablename__ = 'job_test'
    # 字段信息
    id = Column(Integer, primary_key=True, autoincrement=True, doc='主键')
    position_id = Column(Integer, nullable=True)
    position_name = Column(String(length=255))


# 创建表
if __name__ == '__main__':
    # print(TableJob.metadata)
    TableJob.metadata.create_all(engine)
