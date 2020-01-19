# -*- coding: utf-8 -*-
import scrapy
# 导入item
from pythondemo.items import PythondemoItem

class Beauty02Spider(scrapy.Spider):
    name = 'beauty05'
    allowed_domains = ['pic.netbian.com']
    start_urls = [
        'http://pic.netbian.com/4kmeinv/index_72.html',
        'http://pic.netbian.com/4kmeinv/index_73.html',
        'http://pic.netbian.com/4kmeinv/index_74.html',
        'http://pic.netbian.com/4kmeinv/index_75.html',
        'http://pic.netbian.com/4kmeinv/index_76.html',
        'http://pic.netbian.com/4kmeinv/index_77.html',
        'http://pic.netbian.com/4kmeinv/index_78.html',
        'http://pic.netbian.com/4kmeinv/index_79.html',

        'http://pic.netbian.com/4kmeinv/index_80.html',
        'http://pic.netbian.com/4kmeinv/index_82.html',
        'http://pic.netbian.com/4kmeinv/index_83.html',
        'http://pic.netbian.com/4kmeinv/index_84.html',
        'http://pic.netbian.com/4kmeinv/index_85.html',
        'http://pic.netbian.com/4kmeinv/index_86.html',
        'http://pic.netbian.com/4kmeinv/index_87.html',
        'http://pic.netbian.com/4kmeinv/index_88.html',
        'http://pic.netbian.com/4kmeinv/index_89.html',

        'http://pic.netbian.com/4kmeinv/index_90.html',
        'http://pic.netbian.com/4kmeinv/index_92.html',
        'http://pic.netbian.com/4kmeinv/index_93.html',
        'http://pic.netbian.com/4kmeinv/index_94.html',
        'http://pic.netbian.com/4kmeinv/index_95.html',
        'http://pic.netbian.com/4kmeinv/index_96.html',
        'http://pic.netbian.com/4kmeinv/index_97.html',
        'http://pic.netbian.com/4kmeinv/index_98.html',
        'http://pic.netbian.com/4kmeinv/index_99.html',

        'http://pic.netbian.com/4kmeinv/index_100.html',
        'http://pic.netbian.com/4kmeinv/index_102.html',
        'http://pic.netbian.com/4kmeinv/index_103.html',
        'http://pic.netbian.com/4kmeinv/index_104.html',
        'http://pic.netbian.com/4kmeinv/index_105.html',
        'http://pic.netbian.com/4kmeinv/index_106.html',
        'http://pic.netbian.com/4kmeinv/index_107.html',
        'http://pic.netbian.com/4kmeinv/index_108.html',
        'http://pic.netbian.com/4kmeinv/index_109.html',

        'http://pic.netbian.com/4kmeinv/index_110.html',
        'http://pic.netbian.com/4kmeinv/index_112.html',
        'http://pic.netbian.com/4kmeinv/index_113.html',
        'http://pic.netbian.com/4kmeinv/index_114.html',
        'http://pic.netbian.com/4kmeinv/index_115.html',
        'http://pic.netbian.com/4kmeinv/index_116.html',
        'http://pic.netbian.com/4kmeinv/index_117.html',
        'http://pic.netbian.com/4kmeinv/index_118.html',
        'http://pic.netbian.com/4kmeinv/index_119.html',

        'http://pic.netbian.com/4kmeinv/index_120.html',
        'http://pic.netbian.com/4kmeinv/index_122.html',
        'http://pic.netbian.com/4kmeinv/index_123.html',
        'http://pic.netbian.com/4kmeinv/index_124.html',
        'http://pic.netbian.com/4kmeinv/index_125.html',
        'http://pic.netbian.com/4kmeinv/index_126.html',
        'http://pic.netbian.com/4kmeinv/index_127.html',
        'http://pic.netbian.com/4kmeinv/index_128.html',
        'http://pic.netbian.com/4kmeinv/index_129.html',

        'http://pic.netbian.com/4kmeinv/index_130.html',
        'http://pic.netbian.com/4kmeinv/index_132.html',
        'http://pic.netbian.com/4kmeinv/index_133.html',
        'http://pic.netbian.com/4kmeinv/index_134.html',
        'http://pic.netbian.com/4kmeinv/index_135.html',
        'http://pic.netbian.com/4kmeinv/index_136.html',
        'http://pic.netbian.com/4kmeinv/index_137.html',
        'http://pic.netbian.com/4kmeinv/index_138.html',
        'http://pic.netbian.com/4kmeinv/index_139.html',

        'http://pic.netbian.com/4kmeinv/index_140.html',
        'http://pic.netbian.com/4kmeinv/index_142.html',
        'http://pic.netbian.com/4kmeinv/index_143.html',
        'http://pic.netbian.com/4kmeinv/index_144.html',
        'http://pic.netbian.com/4kmeinv/index_145.html',
        'http://pic.netbian.com/4kmeinv/index_146.html',
        'http://pic.netbian.com/4kmeinv/index_147.html',
        'http://pic.netbian.com/4kmeinv/index_148.html',
        'http://pic.netbian.com/4kmeinv/index_149.html',

        'http://pic.netbian.com/4kmeinv/index_150.html',
        'http://pic.netbian.com/4kmeinv/index_152.html',
        'http://pic.netbian.com/4kmeinv/index_153.html',
        'http://pic.netbian.com/4kmeinv/index_154.html',
        'http://pic.netbian.com/4kmeinv/index_155.html',
        'http://pic.netbian.com/4kmeinv/index_156.html',
        'http://pic.netbian.com/4kmeinv/index_157.html',
        'http://pic.netbian.com/4kmeinv/index_158.html',
        'http://pic.netbian.com/4kmeinv/index_159.html',

        'http://pic.netbian.com/4kmeinv/index_160.html',
        'http://pic.netbian.com/4kmeinv/index_162.html',
        'http://pic.netbian.com/4kmeinv/index_163.html',
        'http://pic.netbian.com/4kmeinv/index_164.html',
        'http://pic.netbian.com/4kmeinv/index_165.html',
        'http://pic.netbian.com/4kmeinv/index_166.html',
        'http://pic.netbian.com/4kmeinv/index_167.html',
        'http://pic.netbian.com/4kmeinv/index_168.html',
        'http://pic.netbian.com/4kmeinv/index_169.html',

        'http://pic.netbian.com/4kmeinv/index_170.html',
        'http://pic.netbian.com/4kmeinv/index_172.html',
        'http://pic.netbian.com/4kmeinv/index_173.html',
        'http://pic.netbian.com/4kmeinv/index_174.html',
        'http://pic.netbian.com/4kmeinv/index_175.html',
        'http://pic.netbian.com/4kmeinv/index_176.html',
        'http://pic.netbian.com/4kmeinv/index_177.html',
        'http://pic.netbian.com/4kmeinv/index_178.html',

        'http://pic.netbian.com/4kmeinv/index_180.html',
        'http://pic.netbian.com/4kmeinv/index_182.html',
        'http://pic.netbian.com/4kmeinv/index_183.html',
        'http://pic.netbian.com/4kmeinv/index_184.html',
        'http://pic.netbian.com/4kmeinv/index_185.html',
        'http://pic.netbian.com/4kmeinv/index_186.html',
        'http://pic.netbian.com/4kmeinv/index_187.html',
        'http://pic.netbian.com/4kmeinv/index_188.html',
        'http://pic.netbian.com/4kmeinv/index_189.html',

        'http://pic.netbian.com/4kmeinv/index_190.html',
        'http://pic.netbian.com/4kmeinv/index_192.html'
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
