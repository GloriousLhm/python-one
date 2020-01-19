# -*- coding: utf-8 -*-
import scrapy
# 导入item
from pythondemo.items import PythondemoItem



class Beauty06Spider(scrapy.Spider):
    name = 'beauty06'
    allowed_domains = ['www.win4000.com']
    start_urls = [
        'http://www.win4000.com/meinvtag752_1.html',
        'http://www.win4000.com/meinvtag752_2.html',
        'http://www.win4000.com/meinvtag752_3.html',
        'http://www.win4000.com/meinvtag752_4.html',
        'http://www.win4000.com/meinvtag752_5.html'
    ]

    def parse(self, response):
        print(111)
        imglist = response.xpath("//div[@class='Left_bar']//ul/li")
        for item in imglist:
            print(item)
            # 创建一个变量 item文件导进来
            img_itme = PythondemoItem()
            img_itme['imgsrc'] = item.xpath(".//img/@data-original").extract_first()
            #    把数据yield到管道中去
            yield img_itme
