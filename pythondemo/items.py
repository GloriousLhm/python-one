# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# 这个文件是爬取数据的容器
import scrapy


class PythondemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    imgsrc = scrapy.Field()
    releasetime = scrapy.Field()
    score = scrapy.Field()
    # 名
    firstname = scrapy.Field()
    # 姓
    lasttname = scrapy.Field()
    # 美女图片
    imgsrc = scrapy.Field()

    pass
