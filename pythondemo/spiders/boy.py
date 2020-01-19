# -*- coding: utf-8 -*-
import scrapy
# 导入item
from pythondemo.items import PythondemoItem

class BoySpider(scrapy.Spider):
    name = 'boy'
    allowed_domains = ['www.nanrentu.cc']
    start_urls = [
        'https://www.nanrentu.cc/sgtp/xxrsg.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_2.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_3.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_4.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_5.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_6.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_7.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_8.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_9.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_10.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_11.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_12.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_13.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_14.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_15.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_16.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_17.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_18.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_19.html',
        'https://www.nanrentu.cc/sgtp/xxrsg_20.html',

        'https://www.nanrentu.cc/sgtp/jrsg.html',
         'https://www.nanrentu.cc/sgtp/jrsg_2.html',
        'https://www.nanrentu.cc/sgtp/jrsg_3.html',
        'https://www.nanrentu.cc/sgtp/jrsg_5.html',
        'https://www.nanrentu.cc/sgtp/jrsg_6.html',
        'https://www.nanrentu.cc/sgtp/jrsg_7.html',
        'https://www.nanrentu.cc/sgtp/jrsg_8.html',
        'https://www.nanrentu.cc/sgtp/jrsg_9.html',
        'https://www.nanrentu.cc/sgtp/jrsg_10.html',
        'https://www.nanrentu.cc/sgtp/jrsg_11.html',
        'https://www.nanrentu.cc/sgtp/jrsg_12.html',
        'https://www.nanrentu.cc/sgtp/jrsg_13.html',
        'https://www.nanrentu.cc/sgtp/jrsg_14.html',
        'https://www.nanrentu.cc/sgtp/jrsg_15.html',
        'https://www.nanrentu.cc/sgtp/jrsg_16.html',
        'https://www.nanrentu.cc/sgtp/jrsg_17.html',
        'https://www.nanrentu.cc/sgtp/jrsg_18.html',
        'https://www.nanrentu.cc/sgtp/jrsg_19.html',
        'https://www.nanrentu.cc/sgtp/jrsg_20.html',
        'https://www.nanrentu.cc/sgtp/jrsg_21.html',
        'https://www.nanrentu.cc/sgtp/jrsg_22.html',
        'https://www.nanrentu.cc/sgtp/jrsg_23.html',
        'https://www.nanrentu.cc/sgtp/jrsg_24.html',
        'https://www.nanrentu.cc/sgtp/jrsg_25.html',
        'https://www.nanrentu.cc/sgtp/jrsg_26.html',
        'https://www.nanrentu.cc/sgtp/jrsg_27.html',
        'https://www.nanrentu.cc/sgtp/jrsg_28.html',
        'https://www.nanrentu.cc/sgtp/jrsg_29.html',

        'https://www.nanrentu.cc/sgtp/jrsg_30.html',
        'https://www.nanrentu.cc/sgtp/jrsg_31.html',
        'https://www.nanrentu.cc/sgtp/jrsg_32.html',
        'https://www.nanrentu.cc/sgtp/jrsg_33.html',
        'https://www.nanrentu.cc/sgtp/jrsg_34.html',
        'https://www.nanrentu.cc/sgtp/jrsg_35.html',
        'https://www.nanrentu.cc/sgtp/jrsg_36.html',
        'https://www.nanrentu.cc/sgtp/jrsg_37.html',

        'https://www.nanrentu.cc/sgtp/hgsg.html',
        'https://www.nanrentu.cc/sgtp/hgsg_2.html',

        'https://www.nanrentu.cc/sgtp/omsg.html',
        'https://www.nanrentu.cc/sgtp/omsg_2.html',
        'https://www.nanrentu.cc/sgtp/omsg_3.html',
        'https://www.nanrentu.cc/sgtp/omsg_4.html',
        'https://www.nanrentu.cc/sgtp/omsg_5.html',
        'https://www.nanrentu.cc/sgtp/omsg_6.html',
        'https://www.nanrentu.cc/sgtp/omsg_7.html',
        'https://www.nanrentu.cc/sgtp/omsg_8.html',
        'https://www.nanrentu.cc/sgtp/omsg_9.html',

        'https://www.nanrentu.cc/sgtp/omsg_10.html',
        'https://www.nanrentu.cc/sgtp/omsg_11.html',
        'https://www.nanrentu.cc/sgtp/omsg_12.html',
        'https://www.nanrentu.cc/sgtp/omsg_13.html',
        'https://www.nanrentu.cc/sgtp/omsg_14.html',
        'https://www.nanrentu.cc/sgtp/omsg_15.html',
        'https://www.nanrentu.cc/sgtp/omsg_16.html',
        'https://www.nanrentu.cc/sgtp/omsg_17.html',
        'https://www.nanrentu.cc/sgtp/omsg_18.html',
        'https://www.nanrentu.cc/sgtp/omsg_19.html',

        'https://www.nanrentu.cc/sgtp/omsg_20.html',
        'https://www.nanrentu.cc/sgtp/omsg_21.html',
        'https://www.nanrentu.cc/sgtp/omsg_22.html',
        'https://www.nanrentu.cc/sgtp/omsg_23.html',
        'https://www.nanrentu.cc/sgtp/omsg_24.html',
        'https://www.nanrentu.cc/sgtp/omsg_25.html',
        'https://www.nanrentu.cc/sgtp/omsg_26.html',
        'https://www.nanrentu.cc/sgtp/omsg_27.html',
        'https://www.nanrentu.cc/sgtp/omsg_28.html',
        'https://www.nanrentu.cc/sgtp/omsg_29.html',

        'https://www.nanrentu.cc/sgtp/omsg_30.html',
        'https://www.nanrentu.cc/sgtp/omsg_31.html',
        'https://www.nanrentu.cc/sgtp/omsg_32.html',
        'https://www.nanrentu.cc/sgtp/omsg_33.html',
        'https://www.nanrentu.cc/sgtp/omsg_34.html',
        'https://www.nanrentu.cc/sgtp/omsg_35.html',
        'https://www.nanrentu.cc/sgtp/omsg_36.html',
        'https://www.nanrentu.cc/sgtp/omsg_37.html',
        'https://www.nanrentu.cc/sgtp/omsg_38.html',
        'https://www.nanrentu.cc/sgtp/omsg_39.html',

        'https://www.nanrentu.cc/sgtp/omsg_40.html',
        'https://www.nanrentu.cc/sgtp/omsg_41.html',
        'https://www.nanrentu.cc/sgtp/omsg_42.html',
        'https://www.nanrentu.cc/sgtp/omsg_43.html',
        'https://www.nanrentu.cc/sgtp/omsg_44.html',
        'https://www.nanrentu.cc/sgtp/omsg_45.html',
        'https://www.nanrentu.cc/sgtp/omsg_46.html',
        'https://www.nanrentu.cc/sgtp/omsg_47.html',
        'https://www.nanrentu.cc/sgtp/omsg_48.html',
        'https://www.nanrentu.cc/sgtp/omsg_49.html',

        'https://www.nanrentu.cc/sgtp/omsg_50.html',
        'https://www.nanrentu.cc/sgtp/omsg_51.html',
        'https://www.nanrentu.cc/sgtp/omsg_52.html',
        'https://www.nanrentu.cc/sgtp/omsg_53.html',
        'https://www.nanrentu.cc/sgtp/omsg_54.html',
        'https://www.nanrentu.cc/sgtp/omsg_55.html',

        'https://www.nanrentu.cc/sgtp/sgshz.html',
        'https://www.nanrentu.cc/sgtp/sgshz_2.html',
        'https://www.nanrentu.cc/sgtp/sgshz_3.html',
        'https://www.nanrentu.cc/sgtp/sgshz_4.html',
        'https://www.nanrentu.cc/sgtp/sgshz_5.html',
        'https://www.nanrentu.cc/sgtp/sgshz_6.html'

    ]

    def parse(self, response):
        print(response.text)
        imglist = response.xpath("//div[@class='h-sgtp-box-m']//ul//li")
        for item in imglist:
            print(item)
            # 创建一个变量 item文件导进来
            img_itme = PythondemoItem()
            img_itme['imgsrc'] = item.xpath(".//img/@src").extract_first()
            #    把数据yield到管道中去
            yield img_itme

