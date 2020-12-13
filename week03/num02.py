import pymysql
from dbconfig import read_db_conf
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey,desc,func,Enum,Date
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
    user_age = Column(Date())
    user_sex = Column(Enum("男","女"))
    user_edu = Column(String(15))
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return "Person(user_id = '{self.user_id}',\
                       user_name ='{self.user_name}',\
                       user_age = '{self.user_age}',\
                       user_sex = '{self.user_sex}',\
                       user_edu = '{self.user_edu}',\
                       created_on = '{self.created_on}',\
                       updated_on = '{self.updated_on}'\
                       )".format(self=self)

dburl = "mysql+pymysql://%s:%s@%s:3306/%s?charset=utf8mb4" %(user,password,host,database)
engine = create_engine(dburl, echo=True, encoding="utf-8")

Base.metadata.create_all(engine)

'''方式一'''
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

person_demo=[Person(user_name="danny", user_age=20, user_bir="2000-10-20", user_sex="男", user_edu="本科"),\
             Person(user_name="elsa",  user_age=30, user_bir="1990-04-11", user_sex="男", user_edu="大专"),\
             Person(user_name="fanny",  user_age=25, user_bir="1995-12-11", user_sex="女", user_edu="硕士")]
session.add_all(person_demo)
session.commit()

# 查询结果
for result in session.query(Person):
    print(result)



'''方式二'''
try:
    with db.cursor() as cursor:
        sql = 'INSERT INTO person(user_name, user_age, user_bir, user_sex, user_edu, created_on, updated_on) VALUES(%s,%s,%s,%s,%s,%s,%s)'
        values = (
            ("Jack", 20, "2000-10-20", "男", "本科", str(datetime.now()) , str(datetime.now())),
            ("John", 30, "1990-04-11", "男", "大专", str(datetime.now()) , str(datetime.now())),
            ("kitty", 25, "1995-12-11", "女", "硕士", str(datetime.now()) , str(datetime.now())),
        )
        cursor.executemany(sql, values)
        db.commit()

        sql = 'SELECT * FROM person ORDER BY user_id DESC LIMIT 3'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(f"result:{result}")

    
except Exception as e:
    print(f'fetch error: {e}')

finally:
    db.close()
   