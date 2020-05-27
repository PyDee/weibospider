import requests
import time
import json
from pprint import pprint

weibo_containerid = '1076035518030219'
tweet_item = dict()
url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=5518030219&containerid={}'.format(weibo_containerid)
response = requests.get(url)
result = json.loads(response.text)
tweet_list = result.get('data').get('cards')
for item in tweet_list:
    pprint(item)
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
    pprint(tweet_item)
    exit()
