# -*- coding: utf-8 -*-
import scrapy
from pythondemo.items import PythondemoItem
class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/']
    print('hello maoyan')

    def parse(self, response):
        print(response.text)
        print('111')
        print('222')


