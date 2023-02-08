# _*_ coding : utf-8 _*_
# @Time : 2023-01-19 11:45
# @Author : wws
# @File : test
# @Project : third-platform_spider_text
import datetime

from db_utils import get_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from parse_utils import *
from datetime import datetime


@staticmethod
def get_href(string):
    return str(string).split('id=')[1]

if __name__ == '__main__':
    # print(get_href(href))
    # href = 'https://www.manomano.fr/p/chaise-futurefurniture-ensemble-de-2-chaises-de-salle-a-manger-chaise-de-salle-a-manger-ensemble-de-2-chaises-de-salle-a-manger-chaises-de-salle-a-manger-velours-41029198?product_id=40524035'
    # str = 'https://www.manomano.fr/transat-2728'
    # site = 'Mano.fr'
    # site_category = site[5:7]
    # href_split = href[-8:]
    # print(href_split)
    # engine = get_engine
    # session = sessionmaker(bind=engine)
    # sess = session()
    # Base = declarative_base()
    # CategoryTask = type('task', (Base, TaskTemplate), {'__tablename__': 'sp_plat_site_task'})
    # categorytasks = sess.query(CategoryTask.id, CategoryTask.category_link, CategoryTask.task_code
    #                            , CategoryTask.plat, CategoryTask.site, CategoryTask.link_maxpage)\
    #     .filter(CategoryTask.plat == 'Conforama').distinct()
    # sess.query()
    # # str = '2023-01-19 13:50:01.959412'
    # date = datetime.now().strftime("%Y-%m-%d")
    # # a = 2
    # # if a ==1 or a==2:
    # #     print("没问题")
    # str1 = 'Aaa'
    # # str2 = '4/5'
    # # if '/' in str2:
    # #     str2 = str2[:1]
    # #     print(str2)
    # a = "123123456."
    # c = "123123456.123"

    # index = a.index('1')
    # b = a.find('1',3,-1)
    # print(b)
    # print(index)
    # print(type(index))
    # index = a.index('.')
    # length = len(c)-1
    # price = add_decimal(c)
    # print(price)
    # print(type(price))
    # str = 'Mano.fr'
    #     # str11 = 'Mano.es'
    #     # if '' in str or 'es' in str11:
    #     #     print("没问题")
    # time = datetime.now().strftime("%Y-%m-%d")  # <class 'str'>
    # time = datetime.now()  # <class 'datetime.datetime'>
    # print(time)
    # print(type(time))
    # item = {}
    # item['asin'] = "asin"
    # item['create_time'] = datetime.now()
    # item['plat'] = "plat"
    # item['site'] = 'site'
    # print(item)
    # print(type(item))
    # item_test = item.copy()
    # print(item_test)
    #
    # list1 = []
    # list1 = [1,23,4,5,'321312',321321,5*8]
    # print(list1)
    # list2 = list1.copy()
    # print(list2)
    # print(type(list2))


# count = 1
# def judge(self):
#     global count
#     count = 2
#     print("方法里========"+str(count))
# print(type(count))
# print("方法外======="+str(count))
# def judge1():
#     print("方法2里========"+str(count))
#
# # judge()
# # judge1()
# print("最新版本")
    s = '  sad  sad wqe'
    print(s.replace(' ',''))

