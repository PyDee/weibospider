import time
import json
from scrapy_redis.spiders import RedisSpider
from ..items import UserInfo
import redis

r = redis.Redis(host='127.0.0.1')


class WeiboPhoneUserSpider(RedisSpider):
    name = 'phone_user'
    allowed_domains = ['m.weibo.cn']
    redis_key = "user_spider:start_urls"

    def parse(self, response):
        print('user_status_code', response.status)
        user_item = UserInfo()
        result = json.loads(response.text)
        gender = '男'
        result_data = result.get('data')
        user_info = result_data.get('userInfo')
        tabs_info = result_data.get('tabsInfo').get('tabs')

        user_item['_id'] = user_info.get('id')
        user_item['nick_name'] = user_info.get('screen_name')
        user_item['crawl_time'] = int(time.time())
        user_item['gender'] = gender if user_info.get('gender') == 'm' else '女'
        user_item['brief_introduction'] = user_info.get('description')
        user_item['vip_level'] = user_info.get('mbrank')
        user_item['follows_num'] = user_info.get('follow_count')
        user_item['fans_num'] = user_info.get('followers_count')
        user_item['tweets_num'] = user_info.get('statuses_count')
        for item in tabs_info:
            if item.get('tab_type') == 'profile':
                user_item['profile_id'] = item.get('containerid')
            if item.get('tab_type') == 'weibo':
                user_item['weibo_id'] = item.get('containerid')
                tweet_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=6197250416&containerid={}'.format(
                    user_item['weibo_id'])
                r.lpush('tweet_spider:start_urls', tweet_url)
            if item.get('tab_type') == 'album':
                user_item['album_id'] = item.get('containerid')

        yield user_item
