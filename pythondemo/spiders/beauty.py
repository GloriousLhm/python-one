# -*- coding: utf-8 -*-
import scrapy
# 导入item
from pythondemo.items import PythondemoItem

class BeautySpider(scrapy.Spider):
    name = 'beauty'
    allowed_domains = ['www.plmm.com.cn']
    start_urls = [
        'https://www.plmm.com.cn/xinggan/',
        'https://www.plmm.com.cn/xinggan/index_1.html',
        'https://www.plmm.com.cn/xinggan/index_2.html',
        'https://www.plmm.com.cn/xinggan/index_3.html',
        'https://www.plmm.com.cn/xinggan/index_4.html',
        'https://www.plmm.com.cn/xinggan/index_5.html',
        'https://www.plmm.com.cn/xinggan/index_6.html',
        'https://www.plmm.com.cn/xinggan/index_7.html',
        'https://www.plmm.com.cn/xinggan/index_8.html',
        'https://www.plmm.com.cn/xinggan/index_9.html',
        'https://www.plmm.com.cn/xinggan/index_10.html',
        'https://www.plmm.com.cn/xinggan/index_11.html',
        'https://www.plmm.com.cn/xinggan/index_12.html',
        'https://www.plmm.com.cn/xinggan/index_13.html',
        'https://www.plmm.com.cn/xinggan/index_14.html',
        'https://www.plmm.com.cn/xinggan/index_15.html',
        'https://www.plmm.com.cn/xinggan/index_16.html',
        'https://www.plmm.com.cn/xinggan/index_17.html',
        'https://www.plmm.com.cn/xinggan/index_18.html',
        'https://www.plmm.com.cn/xinggan/index_19.html',
        'https://www.plmm.com.cn/xinggan/index_20.html',
        'https://www.plmm.com.cn/xinggan/index_21.html',
        'https://www.plmm.com.cn/xinggan/index_22.html',
        'https://www.plmm.com.cn/xinggan/index_23.html',
        'https://www.plmm.com.cn/xinggan/index_24.html',
        'https://www.plmm.com.cn/xinggan/index_25.html',
        'https://www.plmm.com.cn/xinggan/index_26.html',
        'https://www.plmm.com.cn/xinggan/index_27.html',
        'https://www.plmm.com.cn/xinggan/index_28.html',
        'https://www.plmm.com.cn/xinggan/index_29.html',
        'https://www.plmm.com.cn/xinggan/index_30.html',
        'https://www.plmm.com.cn/xinggan/index_31.html',
        'https://www.plmm.com.cn/xinggan/index_32.html',
        'https://www.plmm.com.cn/xinggan/index_33.html',
        'https://www.plmm.com.cn/xinggan/index_34.html',
        'https://www.plmm.com.cn/xinggan/index_35.html',
        'https://www.plmm.com.cn/xinggan/index_36.html',
        'https://www.plmm.com.cn/xinggan/index_37.html',
        'https://www.plmm.com.cn/xinggan/index_38.html',
        'https://www.plmm.com.cn/xinggan/index_39.html',
        'https://www.plmm.com.cn/xinggan/index_40.html',
        'https://www.plmm.com.cn/xinggan/index_41.html',
        'https://www.plmm.com.cn/xinggan/index_42.html',
        'https://www.plmm.com.cn/xinggan/index_43.html',
        'https://www.plmm.com.cn/xinggan/index_44.html',
        'https://www.plmm.com.cn/xinggan/index_45.html',
        'https://www.plmm.com.cn/xinggan/index_46.html',
        'https://www.plmm.com.cn/xinggan/index_47.html',
        'https://www.plmm.com.cn/xinggan/index_48.html',
        'https://www.plmm.com.cn/xinggan/index_49.html',

        'https://www.plmm.com.cn/xinggan/index_50.html',
        'https://www.plmm.com.cn/xinggan/index_51.html',
        'https://www.plmm.com.cn/xinggan/index_52.html',
        'https://www.plmm.com.cn/xinggan/index_53.html',
        'https://www.plmm.com.cn/xinggan/index_54.html',
        'https://www.plmm.com.cn/xinggan/index_55.html',
        'https://www.plmm.com.cn/xinggan/index_56.html',
        'https://www.plmm.com.cn/xinggan/index_57.html',
        'https://www.plmm.com.cn/xinggan/index_58.html',
        'https://www.plmm.com.cn/xinggan/index_59.html',

        'https://www.plmm.com.cn/xinggan/index_60.html',
        'https://www.plmm.com.cn/xinggan/index_61.html',
        'https://www.plmm.com.cn/xinggan/index_62.html',
        'https://www.plmm.com.cn/xinggan/index_63.html',
        'https://www.plmm.com.cn/xinggan/index_64.html',
        'https://www.plmm.com.cn/xinggan/index_65.html',
        'https://www.plmm.com.cn/xinggan/index_66.html',
        'https://www.plmm.com.cn/xinggan/index_67.html',
        'https://www.plmm.com.cn/xinggan/index_68.html',
        'https://www.plmm.com.cn/xinggan/index_69.html',

        'https://www.plmm.com.cn/xinggan/index_70.html',
        'https://www.plmm.com.cn/xinggan/index_71.html',
        'https://www.plmm.com.cn/xinggan/index_72.html',
        'https://www.plmm.com.cn/xinggan/index_73.html',
        'https://www.plmm.com.cn/xinggan/index_74.html',
        'https://www.plmm.com.cn/xinggan/index_75.html',
        'https://www.plmm.com.cn/xinggan/index_76.html',
        'https://www.plmm.com.cn/xinggan/index_77.html',
        'https://www.plmm.com.cn/xinggan/index_78.html',
        'https://www.plmm.com.cn/xinggan/index_79.html',

        'https://www.plmm.com.cn/xinggan/index_80.html',
        'https://www.plmm.com.cn/xinggan/index_81.html',
        'https://www.plmm.com.cn/xinggan/index_82.html',
        'https://www.plmm.com.cn/xinggan/index_83.html',
        'https://www.plmm.com.cn/xinggan/index_84.html',
        'https://www.plmm.com.cn/xinggan/index_85.html',
        'https://www.plmm.com.cn/xinggan/index_86.html',
        'https://www.plmm.com.cn/xinggan/index_87.html',
        'https://www.plmm.com.cn/xinggan/index_88.html',
        'https://www.plmm.com.cn/xinggan/index_89.html',

        'https://www.plmm.com.cn/xinggan/index_90.html',
        'https://www.plmm.com.cn/xinggan/index_91.html'

    ]

    # 性感
    def parse(self, response):
        imglist = response.xpath("////div[@class='goods-item']")
        for item in imglist:
            print(item)
            # 创建一个变量 item文件导进来
            img_itme = PythondemoItem()
            img_itme['imgsrc'] = item.xpath(".//img/@src").extract_first()
            #    把数据yield到管道中去
            yield img_itme

        # pass
