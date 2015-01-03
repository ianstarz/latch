# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ConcertScraperItem(scrapy.Item):
    date = scrapy.Field()
    concert_time = scrapy.Field()
    headliner = scrapy.Field()
    pass
