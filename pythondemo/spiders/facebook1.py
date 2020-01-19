# -*- coding: utf-8 -*-
import scrapy
# 导入item
from pythondemo.items import PythondemoItem


class Facebook1Spider(scrapy.Spider):
    name = 'facebook1'
    allowed_domains = ['www.facebook.com']
    start_urls = ['https://www.facebook.com/groups/hoathienquyet.vn/members/']

    def parse(self, response):
        print(response.text())
