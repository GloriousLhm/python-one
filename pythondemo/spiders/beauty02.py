# -*- coding: utf-8 -*-
import scrapy
# 导入item
from pythondemo.items import PythondemoItem

class Beauty02Spider(scrapy.Spider):
    name = 'beauty02'
    allowed_domains = ['pic.netbian.com']
    start_urls = [
        'http://pic.netbian.com/4kmeinv',
        'http://pic.netbian.com/4kmeinv/index_2.html',
        'http://pic.netbian.com/4kmeinv/index_3.html',
        'http://pic.netbian.com/4kmeinv/index_4.html',
        'http://pic.netbian.com/4kmeinv/index_5.html',
        'http://pic.netbian.com/4kmeinv/index_6.html',
        'http://pic.netbian.com/4kmeinv/index_7.html',
        'http://pic.netbian.com/4kmeinv/index_8.html',
        'http://pic.netbian.com/4kmeinv/index_9.html',
        'http://pic.netbian.com/4kmeinv/index_10.html',
        'http://pic.netbian.com/4kmeinv/index_12.html',
        'http://pic.netbian.com/4kmeinv/index_13.html',
        'http://pic.netbian.com/4kmeinv/index_14.html',
        'http://pic.netbian.com/4kmeinv/index_15.html',
        'http://pic.netbian.com/4kmeinv/index_16.html',
        'http://pic.netbian.com/4kmeinv/index_17.html',
        'http://pic.netbian.com/4kmeinv/index_18.html',
        'http://pic.netbian.com/4kmeinv/index_19.html'

        'http://pic.netbian.com/4kmeinv/index_20.html',
        'http://pic.netbian.com/4kmeinv/index_22.html',
        'http://pic.netbian.com/4kmeinv/index_23.html',
        'http://pic.netbian.com/4kmeinv/index_24.html',
        'http://pic.netbian.com/4kmeinv/index_25.html',
        'http://pic.netbian.com/4kmeinv/index_26.html',
        'http://pic.netbian.com/4kmeinv/index_27.html',
        'http://pic.netbian.com/4kmeinv/index_28.html',
        'http://pic.netbian.com/4kmeinv/index_29.html',

        'http://pic.netbian.com/4kmeinv/index_30.html',
        'http://pic.netbian.com/4kmeinv/index_32.html',
        'http://pic.netbian.com/4kmeinv/index_33.html',
        'http://pic.netbian.com/4kmeinv/index_34.html',
        'http://pic.netbian.com/4kmeinv/index_35.html',
        'http://pic.netbian.com/4kmeinv/index_36.html',
        'http://pic.netbian.com/4kmeinv/index_37.html',
        'http://pic.netbian.com/4kmeinv/index_38.html',
        'http://pic.netbian.com/4kmeinv/index_39.html',

        'http://pic.netbian.com/4kmeinv/index_40.html',
        'http://pic.netbian.com/4kmeinv/index_42.html',
        'http://pic.netbian.com/4kmeinv/index_43.html',
        'http://pic.netbian.com/4kmeinv/index_44.html',
        'http://pic.netbian.com/4kmeinv/index_45.html',
        'http://pic.netbian.com/4kmeinv/index_46.html',
        'http://pic.netbian.com/4kmeinv/index_47.html',
        'http://pic.netbian.com/4kmeinv/index_48.html',
        'http://pic.netbian.com/4kmeinv/index_49.html',

        'http://pic.netbian.com/4kmeinv/index_50.html',
        'http://pic.netbian.com/4kmeinv/index_52.html',
        'http://pic.netbian.com/4kmeinv/index_53.html',
        'http://pic.netbian.com/4kmeinv/index_54.html',
        'http://pic.netbian.com/4kmeinv/index_55.html',
        'http://pic.netbian.com/4kmeinv/index_56.html',
        'http://pic.netbian.com/4kmeinv/index_57.html',
        'http://pic.netbian.com/4kmeinv/index_58.html',
        'http://pic.netbian.com/4kmeinv/index_59.html',

        'http://pic.netbian.com/4kmeinv/index_60.html',
        'http://pic.netbian.com/4kmeinv/index_62.html',
        'http://pic.netbian.com/4kmeinv/index_63.html',
        'http://pic.netbian.com/4kmeinv/index_64.html',
        'http://pic.netbian.com/4kmeinv/index_65.html',
        'http://pic.netbian.com/4kmeinv/index_66.html',
        'http://pic.netbian.com/4kmeinv/index_67.html',
        'http://pic.netbian.com/4kmeinv/index_68.html',
        'http://pic.netbian.com/4kmeinv/index_69.html',

        'http://pic.netbian.com/4kmeinv/index_70.html',

    ]

    def parse(self, response):
        imglist = response.xpath("//div[@class='slist']/ul/li")
        for item in imglist:
            print(item)
            # 创建一个变量 item文件导进来
            img_itme = PythondemoItem()
            img_itme['imgsrc'] = item.xpath(".//img/@src").extract_first()
            #    把数据yield到管道中去
            yield img_itme
