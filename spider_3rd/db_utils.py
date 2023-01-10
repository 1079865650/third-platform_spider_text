from sqlalchemy import create_engine,Column,Integer,TIMESTAMP,Float,String,Table,MetaData,and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def get_engine():
    engine = create_engine('postgresql+psycopg2://postgres:eya.psql.123456@eay-test-db-recovery-cluster.cluster-caa566iydlu9.rds.cn-northwest-1.amazonaws.com.cn:5432/bi',echo=False)#连接数据库
    return engine

