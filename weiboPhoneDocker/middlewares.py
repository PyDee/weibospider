import time
import json
import random
import requests
from fake_useragent import UserAgent
from twisted.internet.error import TimeoutError, DNSLookupError, \
    ConnectionRefusedError, ConnectionDone, ConnectError, \
    ConnectionLost, TCPTimedOutError
from scrapy.core.downloader.handlers.http11 import TunnelError
from twisted.internet import defer
from twisted.web.client import ResponseFailed
from .settings import proxy_url


class RandomUserAgentMiddleware(object):
    """随机更换User-Agent"""

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


class ProxiesMiddleware:
    ALL_EXCEPTIONS = (defer.TimeoutError, TimeoutError, DNSLookupError,
                      ConnectionRefusedError, ConnectionDone, ConnectError,
                      ConnectionLost, TCPTimedOutError, ResponseFailed,
                      IOError, TunnelError)

    def __init__(self):
        self.proxy = self.random_proxy()  # 随机获取一个代理方法
        self.count = 0

    def random_proxy(self):
        """获取一个随机代理"""
        response = requests.get(proxy_url)
        status_code = response.status_code
        print('[status_code]:', status_code)
        if status_code != 200:
            time.sleep(1)
            self.random_proxy()
        else:
            response_text = response.text
            result = json.loads(response_text)
            print('[result.code]:', result.get('code'))
            if result.get('code') != 0:
                self.random_proxy()
            else:
                proxy_list = result.get('data')
                proxy_count = len(proxy_list)

                num = random.randint(0, proxy_count - 1)
                # 芝麻代理
                # ip = proxy_list[num].get('ip')
                # port = proxy_list[num].get('port')

                # 黑洞IP
                ip = proxy_list[num].get('IP')
                port = proxy_list[num].get('Port')
                self.proxy = 'https://{}:{}'.format(ip, port)
                print('[new_proxy]:', self.proxy)
                # return proxy

    def process_request(self, request, spider):
        if self.count % 500 == 0:
            self.random_proxy()
        self.count += 1
        spider.logger.info("[proxy]   {}".format(self.proxy))
        request.meta["proxy"] = self.proxy

    def process_response(self, request, response, spider):
        if response.status in [403, 400, 405, 301, 302, 418]:
            spider.logger.info("[此代理报错]   {}".format(self.proxy))
            self.random_proxy()
            spider.logger.info("[更的的新代理为]   {}".format(self.proxy))
            new_request = request.copy()
            new_request_l = new_request.replace(url=request.url)
            return new_request_l
        return response

    def process_exception(self, request, exception, spider):
        if isinstance(exception, self.ALL_EXCEPTIONS):
            spider.logger.info("[Got exception]   {}".format(exception))
            spider.logger.info("[需要更换代理重试]   {}".format(self.proxy))
            self.random_proxy()
            spider.logger.info("[更换后的代理为]   {}".format(self.proxy))
            new_request = request.copy()
            new_request_l = new_request.replace(url=request.url)
            return new_request_l
        spider.logger.info("[not contained exception]   {}".format(exception))
