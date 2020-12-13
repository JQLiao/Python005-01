import pymysql
from dbconfig import read_db_conf
from sqlalchemy import  create_engine,Table,Column,Integer,String,MetaData,ForeignKey,desc,DateTime,DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# 读取数据库配置
dbserver = read_db_conf()
host = dbserver["host"]
database = dbserver["database"]
user = dbserver["user"]
password = dbserver["password"]

Base = declarative_base()

class User(Base):
    """用户表"""
    __tablename__ = "user"
    id = Column(Integer(), primary_key=True)
    user_name = Column(String(15), unique=True)
    created_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        result = '{"user_id":%s, "user_name":%s}' % (self.user_id, self.user_name)
        return result

class Account(Base):
    """资产表"""
    __tablename__ = "account"
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer())
    user_asset = Column(DECIMAL(10,2))
    created_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        result = '{"user_id":%s, "user_asset":%s}' % (self.user_id, self.user_asset)
        return result

class AccountFlow(Base):
    """审计表"""
    __tablename__ = "account_flow"
    id = Column(Integer(), primary_key=True)
    from_id = Column(Integer())
    to_id = Column(Integer())
    deal_money = Column(DECIMAL(10,2))
    created_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        result = '{"from_id":%s, "to_id":%s, "deal_money":%s}' % (self.user_id, self.user_asset, self.deal_money)
        return  result

#建立连接
dburl = "mysql+pymysql://%s:%s@%s:3306/%s?charset=utf8mb4" %(user,password,host,database)
engine = create_engine(dburl, echo=True, encoding="utf-8")

Base.metadata.create_all(engine)

#增加测试数据
SessionClass = sessionmaker(bind=engine)
session = SessionClass()
user_obj = [User(user_name="张三"), User(user_name="李四")]
session.add_all(user_obj)
account_obj = [Account(user_id=1,user_asset=150), Account(user_id=2,user_asset=300)]
session.add_all(account_obj)
session.commit()

with engine.begin() as conn:
    zhangsan_count = session.query(Account).outerjoin(User, Account.user_id==User.id).filter(User.user_name == "张三").first()
    lisi_count = session.query(Account).outerjoin(User, Account.user_id==User.id).filter(User.user_name == "李四").first()
  
    if float(zhangsan_count.user_asset) >= 100:
        sql = "UPDATE account SET user_asset=%s, update_time=%s WHERE user_id=%s"
        #张三账户减100
        zs_value = (float(zhangsan_count.user_asset)-100, str(datetime.now()), int(zhangsan_count.user_id))
        conn.execute(sql,zs_value)
       
        #李四账户增100
        ls_value = (float(lisi_count.user_asset)+100, str(datetime.now()), int(lisi_count.user_id))
        conn.execute(sql,ls_value)

        #审计表记录交易
        sql = "INSERT INTO account_flow(from_id, to_id, deal_money, created_time, update_time) VALUES(%s,%s,%s,%s,%s)" 
        value = (int(zhangsan_count.user_id),int(lisi_count.user_id),100,str(datetime.now()),str(datetime.now()))
        conn.execute(sql,value)
    else:
        print("余额不足，交易失败")
        conn.execute("UPDATE account SET user_asset=%s WHERE user_id=%s" %(float(zhangsan_count.user_asset)+200, int(zhangsan_count.user_id)))