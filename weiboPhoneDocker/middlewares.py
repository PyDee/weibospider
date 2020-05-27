import time
import random
import json
import requests
from scrapy.downloadermiddlewares.retry import RetryMiddleware, response_status_message
from fake_useragent import UserAgent


class RandomUserAgentMiddleware(object):
    '''
    随机更换User-Agent
    '''

    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE', 'random')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)

        request.headers.setdefault('User-Agent', get_ua())


class MyProxyMiddleware(object):
    """
    check account status
    HTTP Code = 302/418 -> cookie is expired or banned, and account status will change to 'error'
    """

    def __init__(self):
        self.count = 0
        self.flag = True
        self.proxy = self.fetch_proxy()

    def fetch_proxy(self):
        # You need to rewrite this function if you want to add proxy pool
        # the function should return a ip in the format of "ip:port" like "12.34.1.4:9090"
        url = 'http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.hdtiqu_api_url&packid=0&fa=0&groupid=0&fetch_key=&time=100&qty=1&port=1&format=json&ss=5&css=&dt=0&pro=&city=&usertype=4'
        result = json.loads(requests.get(url).text)
        ip = result.get('data')[0].get('IP')
        port = result.get('data')[0].get('Port')
        proxy = '{}:{}'.format(ip, port)
        return proxy

    def process_request(self, request, spider):
        if not self.flag:
            self.proxy = self.fetch_proxy()
            self.count += 1
            spider.logger.debug('总共获取：{}个ip'.format(self.count))
            self.flag = True
        current_proxy = f'https://{self.proxy}'
        spider.logger.debug(f"request current proxy:{current_proxy}")
        request.meta['proxy'] = current_proxy

    def process_response(self, request, response, spider):
        http_code = response.status

        if http_code == 302 or http_code == 403:
            print('cookie is done')
            return request

        elif http_code == 418:
            self.flag = False
            return request
        else:
            return response
