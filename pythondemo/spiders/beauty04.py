# -*- coding: utf-8 -*-
import scrapy
# 导入item
from pythondemo.items import PythondemoItem

class Beauty04Spider(scrapy.Spider):
    name = 'beauty04'
    allowed_domains = ['www.umei.cc']
    start_urls = [
        'http://www.umei.cc/tags/changtui_1.htm',
        'http://www.umei.cc/tags/changtui_2.htm',
        'http://www.umei.cc/tags/changtui_3.htm',
        'http://www.umei.cc/tags/changtui_4.htm',
        'http://www.umei.cc/tags/changtui_5.htm',
        'http://www.umei.cc/tags/changtui_6.htm',
        'http://www.umei.cc/tags/changtui_7.htm',
        'http://www.umei.cc/tags/changtui_8.htm',
        'http://www.umei.cc/tags/changtui_9.htm',
        'http://www.umei.cc/tags/changtui_10.htm',
        'http://www.umei.cc/tags/changtui_11.htm',
        'http://www.umei.cc/tags/changtui_12.htm',
        'http://www.umei.cc/tags/changtui_13.htm',
        'http://www.umei.cc/tags/changtui_14.htm',





    ]

    def parse(self, response):
        print(111)
        imglist = response.xpath("//div[@class='TypeList']/ul/li")
        for item in imglist:
            print(item)
            # 创建一个变量 item文件导进来
            img_itme = PythondemoItem()
            img_itme['imgsrc'] = item.xpath(".//img/@src").extract_first()
            #    把数据yield到管道中去
            yield img_itme

