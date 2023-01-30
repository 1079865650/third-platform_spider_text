# _*_ coding : utf-8 _*_
# @Time : 2023-01-19 11:45
# @Author : wws
# @File : test
# @Project : third-platform_spider_text
from db_utils import get_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from spider_3rd.items import TaskTemplate


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
    engine = get_engine
    session = sessionmaker(bind=engine)
    sess = session()
    Base = declarative_base()
    CategoryTask = type('task', (Base, TaskTemplate), {'__tablename__': 'sp_plat_site_task'})
    categorytasks = sess.query(CategoryTask.id, CategoryTask.category_link, CategoryTask.task_code
                               , CategoryTask.plat, CategoryTask.site, CategoryTask.link_maxpage)\
        .filter(CategoryTask.plat == 'Conforama').distinct()
    sess.query()
    print(type(categorytasks))

