import pymysql
from dbconfig import read_db_conf
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey,desc,func,Enum,Date,func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime 
from sqlalchemy.orm import sessionmaker

# 读取数据库配置
dbserver = read_db_conf()
db = pymysql.connect(**dbserver)

host = dbserver["host"]
database = dbserver["database"]
user = dbserver["user"]
password = dbserver["password"]


Base = declarative_base()
class Person(Base):
    __tablename__ = "person"
    user_id = Column(Integer(), primary_key=True)
    user_name = Column(String(15),unique=True)
    user_age = Column(Integer())
    user_bir = Column(Date())
    user_sex = Column(Enum("男","女"))
    user_edu = Column(String(15))
    created_on = Column(DateTime, nullable=False, default=datetime.now)
    updated_on = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)


dburl = "mysql+pymysql://%s:%s@%s:3306/%s?charset=utf8mb4" %(user,password,host,database)
engine = create_engine(dburl, echo=True, encoding="utf-8")

Base.metadata.create_all(engine)

try:
    with db.cursor() as cursor:
        sql = 'INSERT INTO person(user_id, user_name, user_age, user_bir, user_sex, user_edu, created_on, updated_on) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        values = (
            (1, "danny", 20, "2000-10-20", "男", "本科", str(datetime.now()) , str(datetime.now())),
            (2, "elsa", 30, "1990-04-11", "男", "大专", str(datetime.now()) , str(datetime.now())),
            (3, "fanny", 25, "1995-12-11", "女", "硕士", str(datetime.now()) , str(datetime.now())),
        )
        cursor.executemany(sql, values)
        # sql = 'INSERT INTO book (id, name) VALUES (%s, %s)'
        # values = (
        #     (1004, "百年孤独"),
        #     (1005, "飘"),
        # )
    db.commit()

except Exception as e:
    print(f'fetch error: {e}')

finally:
    db.close()
   