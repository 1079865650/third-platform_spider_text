# _*_ coding : utf-8 _*_
# @Time : 2023-01-16 14:14
# @Author : wws
# @File : main
# @Project : third-platform_spider


from scrapy.cmdline import execute
import os
import sys
if __name__ == '__main__':

    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(['scrapy','crawl','spider_conforama_category'])
