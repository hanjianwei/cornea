# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PhotoItem(scrapy.Item):
    url = scrapy.Field()
    keyword = scrapy.Field()
    path = scrapy.Field()
    downloaded_at = scrapy.Field()
