# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    name = scrapy.Field()
    avatar = scrapy.Field()
    link = scrapy.Field()
    author = scrapy.Field()
    following = scrapy.Field()
    followers = scrapy.Field()
    articles = scrapy.Field()
    words = scrapy.Field()
    likes = scrapy.Field()
    date = scrapy.Field()
