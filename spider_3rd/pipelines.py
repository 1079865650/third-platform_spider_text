# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class Spider3RdPipeline:
    def process_item(self, item, spider):
        return item

# -*- coding: utf-8 -*-

from sqlalchemy import create_engine,Column,Integer,TIMESTAMP,Float,String,Table,MetaData,and_ 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 
from datetime import datetime 

from .items import TaskTemplate,AsinTaskTemplate,AsinAttrTemplate,AsinRankTemplate
from .db_utils import * 

class TaskSpidersPipeline(object):

    def __init__(self):#执行爬虫时
        self.engine = get_engine()#连接数据库
        self.session=sessionmaker(bind=self.engine)
        self.sess=self.session()
        Base = declarative_base()
        Base.metadata.schema = 'spider'
        #动态创建orm类,必须继承Base, 这个表名是固定的,如果需要为每个爬虫创建一个表,请使用process_item中的
        self.Task = type('task',(Base,TaskTemplate),{'__tablename__':'sp_plat_site_task'})
        self.Asin = type('asin',(Base,AsinTaskTemplate),{'__tablename__':'sp_plat_site_asin_info_task'})

    def process_item(self,item,spider):#爬取过程中执行的函数

        if item['type'] == 'category_task':
            # print(item['data']['task_code'])
            self.sess.query(self.Task).filter(self.Task.id == item['data']['id']).update({"status": 'crawled','c_page':item['data']['page'],'update_time':datetime.now()})
            self.sess.commit()
            return item
        elif item['type'] == 'asin_task_add':
            for i in item['data']:
                self.sess.add(self.Asin(**i))
            self.sess.commit()
            return item
        else:
            return item

    def close_spider(self, spider):#关闭爬虫时
        self.sess.close()

class AsinSpidersPipeline(object):

    def __init__(self):#执行爬虫时
        self.engine = get_engine()#连接数据库
        self.session=sessionmaker(bind=self.engine)
        self.sess=self.session()
        Base = declarative_base()
        Base.metadata.schema = 'spider'
        #动态创建orm类,必须继承Base, 这个表名是固定的,如果需要为每个爬虫创建一个表,请使用process_item中的
        self.Asin = type('asin',(Base,AsinTaskTemplate),{'__tablename__':'sp_plat_site_asin_info_task'})
        self.AsinAttr = type('asin_attr',(Base,AsinAttrTemplate),{'__tablename__':'sp_plat_site_asin_attr'})
        self.AsinRankCD = type('asin_rank',(Base,AsinRankTemplate),{'__tablename__':'sp_plat_site_asin_rank_cd'})
        self.AsinRankMano = type('asin_rank',(Base,AsinRankTemplate),{'__tablename__':'sp_plat_site_asin_rank_mano'})
        self.AsinRankConforame = type('asin_rank',(Base,AsinRankTemplate),{'__tablename__':'sp_plat_site_asin_rank_conforama'})

    def process_item(self,item,spider):#爬取过程中执行的函数

        # 更新抓取asin状态
        if item['type'] == 'asin_task':
            self.sess.query(self.Asin).filter(and_(self.Asin.id == item['data']['id'])).update({"status": 'crawled','update_time':datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            self.sess.commit()
            return item

        # 删除老属性 新增新属性
        elif item['type'] == 'asin_attr':
            # 删除新增
            self.sess.query(self.AsinAttr).filter(and_(self.AsinAttr.site == item['data']['site'],self.AsinAttr.asin == item['data']['asin'])).delete()
            self.sess.add(self.AsinAttr(**item['data']))
            self.sess.commit()
            return item
        
        # 插入新的时序数据
        elif item['type'] == 'asin_rank':
            for i in item['data']:
                if i['plat'] == 'CD':
                    self.sess.add(self.AsinRankCD(**i))
                    self.sess.commit()
                if i['plat'] == 'Conforama':
                    # 判断asin_rank 是列表页抓取还是详情页抓取  详情页有price,rating 列表页没有
                    if 'price' in i and 'rating' in i:
                        # 给price一个默认值
                        if i["price"] == None:
                            i["price"] = '0'
                            # 从asin_rank中修改表数据  列表页已经写入了一部分数据
                        self.sess.query(self.AsinRankConforame).filter(and_(self.AsinRankConforame.plat == i['plat'],
                                                                            self.AsinRankConforame.asin == i['asin'],
                                                                            self.AsinRankConforame.create_time > datetime.now().strftime("%Y-%m-%d")
                                                                            )) \
                            .update({"price": i['price'], "rating": i['rating'], "reviews": i['reviews']})
                        # self.sess.add(self.AsinRankConforame(**i))
                        self.sess.commit()
                    else:
                        self.sess.add(self.AsinRankConforame(**i))
                        self.sess.commit()
                if i['plat'] == 'Mano':
                    # print("item==============")
                    # print(i)
                    self.sess.add(self.AsinRankMano(**i))
                    self.sess.commit()
            return item
        else:
            return item

    def close_spider(self, spider):#关闭爬虫时
        self.sess.close()
