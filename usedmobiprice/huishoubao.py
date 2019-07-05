import requests
import json
import jsonpath
import pymongo
import time
import random

from itertools import product
from lxml import etree

class HSBSpider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        }
        self.start_url = 'http://www.huishoubao.com/'

    def start_request(self):
        shouji_url = start_url + 'products/1'
        response = requests.get(shouji_url, headers=self.headers)
        return response

    def parse_category(self, respone):
        html = etree.HTML(respone.text)
        category_urls = html.xpath(r'//div[@class="product-class-main"]/div[2]//ul/li/a/@href')
        return category_urls

    def send_request(self, url):
        response = requests.get(url, headers=self.headers)
        return response

    def parse_brand(self, resposne):
        html = etree.HTML(resposne.text)
        phone_items = html.xpath(r'//div[@class="product-list-wrapper"]/ul/li/a')
        # import ipdb; ipdb.set_trace()
        for phone_item in phone_items:
            phone_name = phone_item.find('p').text
            phone_price = phone_item.find('div[2]').find('em').text
            print(phone_name, phone_price)

def schedule():
    worker=HSBSpider()
    
    # 解析手机主页
    r = worker.start_request()
    # 解析各品牌的url
    category_urls = worker.parse_category(r)
    print(category_urls)

    # category_urls = ['/shouji/b52', '/shouji/b9', '/shouji/b484', '/shouji/b16', '/shouji/b4', '/shouji/b184', '/shouji/b7', '/shouji/b24', '/shouji/b365', '/shouji/b356', '/shouji/b278', '/shouji/b357', '/shouji/b18', '/shouji/b17', '/shouji/b342', '/shouji/b25', '/shouji/b1', '/shouji/b8', '/shouji/b21', '/shouji/b14', '/shouji/b103', '/shouji/b20', '/shouji/b15', '/shouji/b12', '/shouji/b10', '/shouji/b11', '/shouji/b358', '/shouji/b51', '/shouji/b391', '/shouji/b460', '/shouji/b463', '/shouji/b478', '/shouji/b479', '/shouji/b3', '/shouji/b19', '/shouji/b266', '/shouji/b485', '/shouji/b405', '/shouji/b403', '/shouji/b104', '/shouji/b116', '/shouji/b112', '/shouji/b102', '/shouji/b273', '/shouji/b481', '/shouji/b272']
    # category_urls = ['/shouji/b52']
    # for category_url in category_urls:
    #     category_url = worker.start_url + category_url
    #     r = worker.send_request(category_url)
    #     worker.parse_brand(r)


if __name__ == '__main__':
    schedule()
