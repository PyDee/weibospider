# -*- coding: utf-8 -*-
import scrapy


class WeiboPhoneTweetSpider(scrapy.Spider):
    name = 'weibo_phone_tweet'
    allowed_domains = ['m.weibo.cn']
    start_urls = ['http://m.weibo.cn/']

    def parse(self, response):
        pass
