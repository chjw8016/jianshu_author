# -*- coding:utf-8 -*-
import scrapy
import time
from jianshu.items import UserItem


class RecommendedAuthorSpider(scrapy.Spider):
    name = "author"
    allowed_domains = ["jianshu.com"]
    start_urls = [
        "http://www.jianshu.com/recommendations/users?page=1",
        "http://www.jianshu.com/recommendations/users?page=2",
        "http://www.jianshu.com/recommendations/users?page=3",
        "http://www.jianshu.com/recommendations/users?page=4",
        "http://www.jianshu.com/recommendations/users?page=5",
    ]

    def parse(self, response):
        href_items = response.xpath('//a[@class="avatar"]/@href').extract()
        for href in href_items:
            url = "http://www.jianshu.com" + href
            yield scrapy.Request(
                url=url,
                callback=self.parse_user
            )

    def parse_user(self, response):
        item = UserItem()
        item["date"] = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        item["name"] = response.xpath('//a[@class="name"]/text()').extract()
        item["author"] = "签约作者" if response.xpath('//span[@class="author-tag"]').extract() else "普通作者"
        item["avatar"] = response.xpath('//div[@class="main-top"]/a[@class="avatar"]/img/@src').extract()
        info_html = response.xpath('//div[@class="info"]/ul/li/div/p/text()').extract()
        item["following"] = info_html[0]
        item["followers"] = info_html[1]
        item["articles"] = info_html[2]
        item["words"] = info_html[3]
        item["likes"] = info_html[4]
        item["link"] = "http://www.jianshu.com" + response.xpath('//a[@class="name"]/@href').extract()[0]
        yield item
