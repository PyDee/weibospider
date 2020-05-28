import json
import random
import requests
from fake_useragent import UserAgent
import redis
from twisted.internet.error import TimeoutError, DNSLookupError, \
    ConnectionRefusedError, ConnectionDone, ConnectError, \
    ConnectionLost, TCPTimedOutError
from scrapy.core.downloader.handlers.http11 import TunnelError
from twisted.internet import defer
from twisted.web.client import ResponseFailed
from .settings import proxy_url


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


# class MyProxyMiddleware(object):
#     def __init__(self):
#         self.count = 0
#         self.proxy = self.fetch_proxy()
#
#     def fetch_proxy(self):
#         # You need to rewrite this function if you want to add proxy pool
#         # the function should return a ip in the format of "ip:port" like "12.34.1.4:9090"
#         url = 'http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.hdtiqu_api_url&packid=0&fa=0&groupid=0&fetch_key=&time=100&qty=10&port=1&format=json&ss=5&css=&dt=0&pro=&city=&usertype=4'
#         result = json.loads(requests.get(url).text)
#
#         ip = result.get('data')[0].get('IP')
#         port = result.get('data')[0].get('Port')
#         self.proxy = '{}:{}'.format(ip, port)
#
#         return self.proxy
#
#     def process_request(self, request, spider):
#         if self.count % 200 == 0 and self.count != 0:
#             self.proxy = self.fetch_proxy()
#             self.count = 0
#         self.count += 1
#         current_proxy = f'https://{self.proxy}'
#         spider.logger.debug(f"current proxy:{current_proxy}")
#         request.meta['proxy'] = current_proxy
#
#     def process_response(self, request, response, spider):
#         http_code = response.status
#
#         if http_code == 302 or http_code == 403:
#             print(response.request.url)
#             print('cookie is done')
#             return request
#
#         elif http_code == 418:
#             self.flag = False
#             return request
#         else:
#             print('ip 过期')
#             return response


redis_pag = {
    "host": "127.0.0.1",
    "port": 6379,
    "db": 14
}

redis_rm = {
    "host": "127.0.0.1",
    "port": 6379,
    "db": 13
}

pool = redis.ConnectionPool(**redis_pag)
r_insert = redis.Redis(connection_pool=pool)

pool_rm = redis.ConnectionPool(**redis_rm)
rm = redis.Redis(connection_pool=pool_rm)


# def select_proxy_list():
#     """获取当前不可使用的ip"""
#     lists = rm.keys()
#     lists = [str(proxy, encoding="utf-8") for proxy in lists]
#     val_list = rm.mget(*lists)
#     val_list = [str(proxy, encoding="utf-8") for proxy in val_list]
#     return val_list


def rm_proxy(value):
    """
    1、再代理池中删除此过时代理
    2、将过期代理或不可用代理存入不可用池中
    3、设置不可用代理的期限为24小时
    """
    r_insert.srem("httpsproxy", value)
    proxskey = value.replace(".", "").replace(":", "").replace("//", "")
    rm.set(proxskey, value)
    rm.pexpire(proxskey, 86400000)


def redom_proxy():
    """获取一个随机代理"""
    # proxy = r_insert.srandmember("httpsproxy")
    # proxy = str(proxy, encoding="utf-8")
    # return proxy
    url = 'http://your_ip_proxy'
    result = json.loads(requests.get(url).text)
    proxy_list = result.get('data')
    proxy_count = len(proxy_list)

    num = random.randint(0, proxy_count)
    ip = proxy_list[num].get('IP')
    port = proxy_list[num].get('Port')
    proxy = 'https://{}:{}'.format(ip, port)

    return proxy


class ProxiesMiddleware:
    ALL_EXCEPTIONS = (defer.TimeoutError, TimeoutError, DNSLookupError,
                      ConnectionRefusedError, ConnectionDone, ConnectError,
                      ConnectionLost, TCPTimedOutError, ResponseFailed,
                      IOError, TunnelError)

    def __init__(self):
        self.proxy = redom_proxy()  # 随机获取一个代理方法
        self.count = 0

    def process_request(self, request, spider):
        if self.count % 500 == 0:
            self.proxy = redom_proxy()
        self.count += 1
        spider.logger.info("[proxy]   {}".format(self.proxy))
        request.meta["proxy"] = self.proxy

    def process_response(self, request, response, spider):
        # 因为遇到过那种返回状态码是200但是是一个被反扒的界面，界面固定都是小于3000字符
        # if len(response.text) < 3000 or response.status in [403, 400, 405, 301, 302, 418]:
        if response.status in [403, 400, 405, 301, 302, 418]:
            spider.logger.info("[此代理报错]   {}".format(self.proxy))
            # rm_proxy(self.proxy)
            # while True:
            new_proxy = redom_proxy()
            # if new_proxy not in select_proxy_list():
            self.proxy = new_proxy
            spider.logger.info("[更的的新代理为]   {}".format(self.proxy))
            # break
            new_request = request.copy()
            new_request_l = new_request.replace(url=request.url)
            return new_request_l
        return response

    def process_exception(self, request, exception, spider):
        # 捕获几乎所有的异常
        if isinstance(exception, self.ALL_EXCEPTIONS):
            # 在日志中打印异常类型
            spider.logger.info("[Got exception]   {}".format(exception))
            spider.logger.info("[需要更换代理重试]   {}".format(self.proxy))
            # rm_proxy(self.proxy)
            # while True:
            new_proxy = redom_proxy()
            # if new_proxy not in select_proxy_list():
            self.proxy = new_proxy
            spider.logger.info("[更换后的代理为]   {}".format(self.proxy))
            # break
            new_request = request.copy()
            new_request_l = new_request.replace(url=request.url)
            return new_request_l
        # 打印出未捕获到的异常
        spider.logger.info("[not contained exception]   {}".format(exception))
