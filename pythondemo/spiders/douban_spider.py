# -*- coding: utf-8 -*-
import scrapy
# 导入item
from pythondemo.items import PythondemoItem

class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['www.douban.com']
    # 入口url,扔到调度器里
    start_urls = ['https://www.douban.com/']
    # 默认的解析方法
    def parse(self, response):
        print(response.text)
        movie_list = response.xpath("//div[@class='section']")
        for i_item in movie_list:
            print(i_item)
            # 创建一个变量 item文件导进来
            douban_item = PythondemoItem()
            # .的意思是进一步的细分
            # 获取文本信息加上一个text()
            douban_item['title'] = i_item.xpath(".//div//h2[@class='section-title']//text()").extract_first()

            # 对好几行的内容进行处理
            content = i_item.xpath(".//....")
            # 进行字符串处理 这里的我们是要解析数据而不是解析第一行数据
            for i_content in content:
                # 先去掉空格
                content_s = "".join(i_content.split())
                douban_item["desc"] = content_s

            #    把数据yield到管道中去
            yield douban_item
            # 一定要写在for循环的外面
            # 看看有没有新的requrest请求
            # 下一页链接如何解析
            # 找到那个后一个标签自动翻页
            # 这里访问到他的数据即可
            next_link = response.xpath("//span[#class='next']/link/@href").extract()
            if next_link:
                next_link = next_link[0]
                yield scrapy.Request("网址的主机头"+next_link,callback=self.parse)

