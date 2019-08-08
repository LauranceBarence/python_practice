from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DECIMAL
from sqlalchemy import DateTime

# 连接信息
engine = create_engine("mysql+pymysql://root:Mysql123$@localhost:3306/my_db", encoding="utf-8", echo=True,
                       max_overflow=5)
SESSION = sessionmaker(bind=engine)
#  表信息
base = declarative_base()


class Job(base):
    __tablename__ = 'jobs'
    # 字段信息
    id = Column(Integer, primary_key=True, autoincrement=True, doc='主键')
    job_sn = Column(String(255), nullable=False)
    job_name = Column(String(length=255), nullable=False)
    longitude = Column(String(length=255))
    latitude = Column(String(length=255))
    work_year = Column(String(length=255))
    education = Column(String(length=255))
    type = Column(String(length=255))
    company_id = Column(String(length=255), nullable=False)
    company_type = Column(String(length=255))
    company_size = Column(String(length=255))
    company_bussiness = Column(String(length=255))
    city = Column(String(length=255), nullable=False)
    job_tags = Column(String(length=255))
    company_abbreviation = Column(String(length=255))
    company_name = Column(String(length=255), nullable=False)
    company_bonus = Column(String(length=255))
    wealthy = Column(String(255), nullable=False)
    create_time = Column(DateTime)
    crawl_time = Column(DateTime)

# # 创建表
# if __name__ == '__main__':
#     # print(TableJob.metadata)
#     Job.metadata.create_all(engine)
