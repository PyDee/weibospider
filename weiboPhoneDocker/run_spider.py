#!/usr/bin/env python
# encoding: utf-8
"""
File Description:
Author: nghuyong
Mail: nghuyong@163.com
Created Time: 2019-12-07 21:27
"""
import os
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.weibo_phone_user import WeiboPhoneUserSpider
from spiders.weibo_phone_tweet import WeiboPhoneTweetSpider

if __name__ == '__main__':
    mode = sys.argv[1]
    os.environ['SCRAPY_SETTINGS_MODULE'] = f'settings'
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    mode_to_spider = {
        'tweet': WeiboPhoneTweetSpider,
        'user': WeiboPhoneUserSpider,
    }
    process.crawl(mode_to_spider[mode])
    # the script will block here until the crawling is finished
    process.start()
