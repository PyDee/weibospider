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
from settings import proxy_url


class RandomUserAgentMiddleware(object):

#    '''
#    随机更换User-Agent
#    '''
#
#    def __init__(self, crawler):
#        super(RandomUserAgentMiddleware, self).__init__()
#        self.ua = UserAgent(verify_ssl=False)
#        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE', 'random')
#
#    @classmethod
#    def from_crawler(cls, crawler):
#        return cls(crawler)
#
#    def process_request(self, request, spider):
#        def get_ua():
#            return getattr(self.ua, self.ua_type)
#
#        request.headers.setdefault('User-Agent', get_ua())
#
#class UserAgentDownloadMiddleware(object):
    # user-agent随机请求头中间件
    def __init__(self):
        self.USER_AGENT = [
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)',
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
            'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
            'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
            'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
        ]

    def process_request(self,request,spider):
        user_agent = random.choice(self.USER_AGENT)
        request.headers['User-Agent'] = user_agent

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
    "host": "redis",
    "port": 6379,
    "db": 14
}

redis_rm = {
    "host": "redis",
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
    url = proxy_url
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
