# -*- coding: utf-8 -*-
import scrapy
# 导入item
from pythondemo.items import PythondemoItem

class EnglihshnameSpider(scrapy.Spider):
    name = 'englihshname'
    allowed_domains = ['ename.dict.cn']
    start_urls = [
        'http://ename.dict.cn/list/all/A',
        'http://ename.dict.cn/list/all/A/2',
        'http://ename.dict.cn/list/all/A/3',
        'http://ename.dict.cn/list/all/A/4',
        'http://ename.dict.cn/list/all/A/5',
        'http://ename.dict.cn/list/all/A/6',
        'http://ename.dict.cn/list/all/A/7',

        'http://ename.dict.cn/list/all/B',
        'http://ename.dict.cn/list/all/B/2',
        'http://ename.dict.cn/list/all/B/3',
        'http://ename.dict.cn/list/all/B/4',
        'http://ename.dict.cn/list/all/B/5',
        'http://ename.dict.cn/list/all/B/6',
        'http://ename.dict.cn/list/all/B/7',

        'http://ename.dict.cn/list/all/C',
        'http://ename.dict.cn/list/all/C/2',
        'http://ename.dict.cn/list/all/C/3',
        'http://ename.dict.cn/list/all/C/4',
        'http://ename.dict.cn/list/all/C/5',
        'http://ename.dict.cn/list/all/C/6',
        'http://ename.dict.cn/list/all/C/7',

        'http://ename.dict.cn/list/all/D',
        'http://ename.dict.cn/list/all/D/2',
        'http://ename.dict.cn/list/all/D/3',
        'http://ename.dict.cn/list/all/D/4',
        'http://ename.dict.cn/list/all/D/5',
        'http://ename.dict.cn/list/all/D/6',
        'http://ename.dict.cn/list/all/D/7',

        'http://ename.dict.cn/list/all/E',
        'http://ename.dict.cn/list/all/E/2',
        'http://ename.dict.cn/list/all/E/3',
        'http://ename.dict.cn/list/all/E/4',
        'http://ename.dict.cn/list/all/E/5',
        'http://ename.dict.cn/list/all/E/6',
        'http://ename.dict.cn/list/all/E/7',

        'http://ename.dict.cn/list/all/F',
        'http://ename.dict.cn/list/all/F/2',
        'http://ename.dict.cn/list/all/F/3',
        'http://ename.dict.cn/list/all/F/4',
        'http://ename.dict.cn/list/all/F/5',
        'http://ename.dict.cn/list/all/F/6',
        'http://ename.dict.cn/list/all/F/7',

        'http://ename.dict.cn/list/all/G',
        'http://ename.dict.cn/list/all/G/2',
        'http://ename.dict.cn/list/all/G/3',
        'http://ename.dict.cn/list/all/G/4',
        'http://ename.dict.cn/list/all/G/5',
        'http://ename.dict.cn/list/all/G/6',
        'http://ename.dict.cn/list/all/G/7',

        'http://ename.dict.cn/list/all/H',
        'http://ename.dict.cn/list/all/H/2',
        'http://ename.dict.cn/list/all/H/3',
        'http://ename.dict.cn/list/all/H/4',
        'http://ename.dict.cn/list/all/H/5',
        'http://ename.dict.cn/list/all/H/6',
        'http://ename.dict.cn/list/all/H/7',

        'http://ename.dict.cn/list/all/I',
        'http://ename.dict.cn/list/all/I/2',
        'http://ename.dict.cn/list/all/I/3',


        'http://ename.dict.cn/list/all/J',
        'http://ename.dict.cn/list/all/J/2',
        'http://ename.dict.cn/list/all/J/3',
        'http://ename.dict.cn/list/all/J/4',
        'http://ename.dict.cn/list/all/J/5',
        'http://ename.dict.cn/list/all/J/6',
        'http://ename.dict.cn/list/all/J/7',

        'http://ename.dict.cn/list/all/K',
        'http://ename.dict.cn/list/all/K/2',
        'http://ename.dict.cn/list/all/K/3',
        'http://ename.dict.cn/list/all/K/4',
        'http://ename.dict.cn/list/all/K/5',
        'http://ename.dict.cn/list/all/K/6',

        'http://ename.dict.cn/list/all/L',
        'http://ename.dict.cn/list/all/L/2',
        'http://ename.dict.cn/list/all/L/3',
        'http://ename.dict.cn/list/all/L/4',
        'http://ename.dict.cn/list/all/L/5',
        'http://ename.dict.cn/list/all/L/6',
        'http://ename.dict.cn/list/all/L/7',

        'http://ename.dict.cn/list/all/L',
        'http://ename.dict.cn/list/all/L/2',
        'http://ename.dict.cn/list/all/L/3',
        'http://ename.dict.cn/list/all/L/4',
        'http://ename.dict.cn/list/all/L/5',
        'http://ename.dict.cn/list/all/L/6',
        'http://ename.dict.cn/list/all/L/7',

        'http://ename.dict.cn/list/all/M',
        'http://ename.dict.cn/list/all/M/2',
        'http://ename.dict.cn/list/all/M/3',
        'http://ename.dict.cn/list/all/M/4',
        'http://ename.dict.cn/list/all/M/5',
        'http://ename.dict.cn/list/all/M/6',
        'http://ename.dict.cn/list/all/M/7',

        'http://ename.dict.cn/list/all/N',
        'http://ename.dict.cn/list/all/N/2',
        'http://ename.dict.cn/list/all/N/3',
        'http://ename.dict.cn/list/all/N/4',
        'http://ename.dict.cn/list/all/N/5',

        'http://ename.dict.cn/list/all/O',
        'http://ename.dict.cn/list/all/O/2',

        'http://ename.dict.cn/list/all/P',
        'http://ename.dict.cn/list/all/P/2',
        'http://ename.dict.cn/list/all/P/3',
        'http://ename.dict.cn/list/all/P/4',
        'http://ename.dict.cn/list/all/P/5',
        'http://ename.dict.cn/list/all/P/6',
        'http://ename.dict.cn/list/all/P/7',

        'http://ename.dict.cn/list/all/Q',

        'http://ename.dict.cn/list/all/R',
        'http://ename.dict.cn/list/all/R/2',
        'http://ename.dict.cn/list/all/R/3'
        'http://ename.dict.cn/list/all/R/4',
        'http://ename.dict.cn/list/all/R/5',
        'http://ename.dict.cn/list/all/R/6',
        'http://ename.dict.cn/list/all/R/7',

        'http://ename.dict.cn/list/all/S',
        'http://ename.dict.cn/list/all/S/2',
        'http://ename.dict.cn/list/all/S/3',
        'http://ename.dict.cn/list/all/S/4',
        'http://ename.dict.cn/list/all/S/5',
        'http://ename.dict.cn/list/all/S/6',
        'http://ename.dict.cn/list/all/S/7',

        'http://ename.dict.cn/list/all/T',
        'http://ename.dict.cn/list/all/T/2',
        'http://ename.dict.cn/list/all/T/3',
        'http://ename.dict.cn/list/all/T/4',
        'http://ename.dict.cn/list/all/T/5',

        'http://ename.dict.cn/list/all/U',

        'http://ename.dict.cn/list/all/V',
        'http://ename.dict.cn/list/all/V/2',
        'http://ename.dict.cn/list/all/V/3',

        'http://ename.dict.cn/list/all/W',
        'http://ename.dict.cn/list/all/W/2',
        'http://ename.dict.cn/list/all/W/3',
        'http://ename.dict.cn/list/all/W/4',
        'http://ename.dict.cn/list/all/W/5',
        'http://ename.dict.cn/list/all/W/6',
        'http://ename.dict.cn/list/all/W/7',

        'http://ename.dict.cn/list/all/X',

        'http://ename.dict.cn/list/all/Y',
        'http://ename.dict.cn/list/all/Z',

    ]

    def parse(self, response):
        print(response.text)
        namelist =  response.xpath("//table/tr")
        for item in namelist:
            print(item)
            print(2222)
            # 创建一个变量 item文件导进来
            enname_itme = PythondemoItem()
            enname_itme['firstname'] = item.xpath("./td/a/text()").extract_first()
            print(enname_itme)
            #    把数据yield到管道中去
            yield enname_itme