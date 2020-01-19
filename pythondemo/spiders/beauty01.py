# -*- coding: utf-8 -*-
import scrapy
# 导入item
from pythondemo.items import PythondemoItem

class BeautySpider(scrapy.Spider):
    name = 'beauty01'
    allowed_domains = ['www.plmm.com.cn']
    start_urls = [
        'https://www.plmm.com.cn/qingchun/',
        'https://www.plmm.com.cn/qingchun/index_2.html',
        'https://www.plmm.com.cn/qingchun/index_3.html',
        'https://www.plmm.com.cn/qingchun/index_4.html',
        'https://www.plmm.com.cn/xiaohua/',
        'https://www.plmm.com.cn/xiaohua/index_2.html',
        'https://www.plmm.com.cn/xiaohua/index_3.html',
        'https://www.plmm.com.cn/chemo/',
        'https://www.plmm.com.cn/qipao/',
        'https://www.plmm.com.cn/qipao/index_2.html',
        'https://www.plmm.com.cn/qipao/index_3.html',
        'https://www.plmm.com.cn/qipao/index_4.html',
        'https://www.plmm.com.cn/qipao/index_5.html',
        'https://www.plmm.com.cn/qipao/index_6.html',
        'https://www.plmm.com.cn/qipao/index_7.html'
    ]

    # 性感
    def parse(self, response):
        print(response.text)
        imglist = response.xpath("////div[@class='goods-item']")
        for item in imglist:
            print(item)
            # 创建一个变量 item文件导进来
            img_itme = PythondemoItem()
            img_itme['imgsrc'] = item.xpath(".//img/@src").extract_first()
            #    把数据yield到管道中去
            yield img_itme

        # pass
