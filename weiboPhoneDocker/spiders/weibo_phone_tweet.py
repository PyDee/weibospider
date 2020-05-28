# -*- coding: utf-8 -*-
import json
from scrapy_redis.spiders import RedisSpider
import time
from ..items import TweetItem


class WeiboPhoneTweetSpider(RedisSpider):
    name = 'phone_tweet'
    allowed_domains = ['m.weibo.cn']
    # start_urls = ['http://m.weibo.cn/']
    redis_key = "tweet_spider:start_urls"

    def parse(self, response):
        result = json.loads(response.text)
        tweet_list = result.get('data').get('cards')
        for item in tweet_list:
            tweet_item = TweetItem()
            tweet_item['_id'] = item.get('mblog').get('bid')
            tweet_item['tool'] = item.get('mblog').get('source')
            tweet_item['created_at'] = item.get('mblog').get('created_at')
            tweet_item['crawl_time'] = int(time.time())
            tweet_item['content'] = item.get('mblog').get('text')
            tweet_item['comment_num'] = item.get('mblog').get('comments_count')
            tweet_item['repost_num'] = item.get('mblog').get('reposts_count')
            tweet_item['like_num'] = item.get('mblog').get('attitudes_count')
            tweet_item['user_id'] = item.get('mblog').get('user').get('id')
            tweet_item['weibo_url'] = item.get('scheme')
            tweet_item['image_url'] = []
            pics = item.get('mblog').get('pics')
            for pic in pics:
                tweet_item['image_url'].append(pic.get('url'))
            yield tweet_item
