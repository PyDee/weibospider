BOT_NAME = 'weiboPhoneDocker'

SPIDER_MODULES = ['weiboPhoneDocker.spiders']
NEWSPIDER_MODULE = 'weiboPhoneDocker.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'weiboPhoneDocker (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 5

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.01
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
# 'weiboPhoneDocker.middlewares.WeibophonedockerSpiderMiddleware': 543,
# 'weiboPhoneDocker.middlewares.MyProxyMiddleware': 200,

# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'weiboPhoneDocker.middlewares.ProxiesMiddleware': 100,
    'weiboPhoneDocker.middlewares.RandomUserAgentMiddleware': 543,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,

}
RANDOM_UA_TYPE = 'random'
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'weiboPhoneDocker.pipelines.WeibophonedockerPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 301
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 配置scrapy-redis调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 配置url去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'

# MongoDb docker Config
# MONGO_HOST = 'mongodb'
# MONGO_PORT = 27017

# mongo local config
MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "weibo"  # 库名
MONGO_USER = "user_name"
MONGO_PSW = "password"

# Redis docker Config
# REDIS_HOST = 'redis'
# REDIS_PORT = 6379

# redis local config
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
# REDIS_PARAMS = {
#     "password": "your_password",
# }

proxy_url = 'http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.hdtiqu_api_url&packid=0&fa=0&groupid=0&fetch_key=&time=100&qty=10&port=1&format=json&ss=5&css=&dt=0&pro=&city=&usertype=4'
# proxy_url = 'http://http.tiqu.alicdns.com/getip3?num=10&type=2&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=2&regions=&gm=4'
DOWNLOAD_TIMEOUT = 30
RETRY_ENABLED = False
