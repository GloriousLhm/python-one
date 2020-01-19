# -*- coding: utf-8 -*-
import scrapy
# 导入item
from pythondemo.items import PythondemoItem

class CnnameSpider(scrapy.Spider):
    name = 'cnname'
    allowed_domains = ['www.resgain.net']
    start_urls = [
        'http://www.resgain.net/xmdq_a.html',
        'http://www.resgain.net/xmdq_b.html',
        'http://www.resgain.net/xmdq_c.html',
        'http://www.resgain.net/xmdq_d.html',
        'http://www.resgain.net/xmdq_e.html',
        'http://www.resgain.net/xmdq_f.html',
        'http://www.resgain.net/xmdq_g.html',
        'http://www.resgain.net/xmdq_h.html',
        'http://www.resgain.net/xmdq_i.html',
        'http://www.resgain.net/xmdq_j.html',
        'http://www.resgain.net/xmdq_k.html',
        'http://www.resgain.net/xmdq_l.html',
        'http://www.resgain.net/xmdq_m.html',
        'http://www.resgain.net/xmdq_n.html',
        'http://www.resgain.net/xmdq_o.html',
        'http://www.resgain.net/xmdq_p.html',
        'http://www.resgain.net/xmdq_q.html',
        'http://www.resgain.net/xmdq_r.html',
        'http://www.resgain.net/xmdq_s.html',
        'http://www.resgain.net/xmdq_t.html',
        'http://www.resgain.net/xmdq_u.html',
        'http://www.resgain.net/xmdq_v.html',
        'http://www.resgain.net/xmdq_w.html',
        'http://www.resgain.net/xmdq_x.html',
        'http://www.resgain.net/xmdq_y.html',
        'http://www.resgain.net/xmdq_z.html',

                  ]

    def parse(self, response):
        namelist =  response.xpath("//div/div[@class='panel-body']/div")
        for item in namelist:
            print(item)
            # 创建一个变量 item文件导进来
            enname_itme = PythondemoItem()
            enname_itme['firstname']= item.xpath(".//text()").extract_first()
            #    把数据yield到管道中去
            yield enname_itme