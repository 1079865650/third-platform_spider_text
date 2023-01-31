# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

import time
import undetected_chromedriver as uc
from scrapy.http.response.html import HtmlResponse
import os

import subprocess

class Spider3RdSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class Spider3RdDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def __init__(self):  # 用于初始化类

        chrome_options = uc.ChromeOptions()
        # chrome_options.add_argument('--blink-settings=imagesEnabled=false')
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument(f"--proxy-server=http://192.168.100.24:60021")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument('--no-first-run')
        chrome_options.add_argument('--no-service-autorun')
        chrome_options.add_argument('--no-default-browser-check')
        chrome_options.add_argument('--password-store=basic')
        chrome_options.add_argument('--no-sandbox')

        # os.system("start C://Program Files//Google//Chrome//Application//chrome.exe --remote-debugging-port=9222")
        # subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="F:\MyChromeDevUserData"')
        # time.sleep(3)
        # chrome_options=Options()
        chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
        # driver_path = r'F:\dependency\chromedriver_win32 (78.0.3904.105)\chromedriver.exe'            #把浏览器驱动器放在任意位置都可以
        driver_path = r'F:\dependency\chromedriver_win32 (109.0.5414.74)\chromedriver.exe'            #把浏览器驱动器放在任意位置都可以
        browser_executable_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        self.driver = uc.Chrome(driver_executable_path=driver_path,options = chrome_options,browser_executable_path=browser_executable_path)

        # self.driver = webdriver.Chrome(executable_path=driver_path)
        # self.driver = webdriver.Chrome(executable_path=driver_path,options=chrome_options);

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        
        # 我们需要拦截请求，由selenium发起请求，将获取的数据封装成一个response对象。
        self.driver.get(request.url)
        # if str(request.url).__contains__('objectID'):
        #     time.sleep(3)
        # else:
        #     time.sleep(6)
        time.sleep(5)
        # self.driver.implicitly_wait(30);
        # js = "var q=document.documentElement.scrollTop=2000"
        # self.driver.execute_script(js)
        # time.sleep(10)
        # js = "var q=document.documentElement.scrollTop=4500"
        # self.driver.execute_script(js)
        # time.sleep(10)
        # js = "var q=document.documentElement.scrollTop=6000"
        # self.driver.execute_script(js)
        # time.sleep(10)
        response = HtmlResponse(request.url,body=self.driver.page_source,request=request,encoding='utf-8')

        return response

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
