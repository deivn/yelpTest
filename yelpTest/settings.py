# -*- coding: utf-8 -*-

BOT_NAME = 'yelpTest'
SPIDER_MODULES = ['yelpTest.spiders']
NEWSPIDER_MODULE = 'yelpTest.spiders'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# 修改request去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 修改调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 允许暂停， redis数据不会丢失
SCHEDULER_PERSIST = True
# 默认的请求队列顺序
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

REDIS_HOST = '47.106.140.94'
REDIS_PORT = 6486
# 数据库配置
MYSQL_HOST = "184.181.11.233"
MYSQL_PORT = 3306
MYSQL_USER = "ebuyhouse"
MYSQL_PASSWD = "ebuyhouse135"
MYSQL_DB = "crawl_data"
# redis配置
REDIRECT_ENABLED = False
COOKIES_ENABLED = False
# 延时3秒
DOWNLOAD_DELAY = 2
# 超时时间
DOWNLOAD_TIMEOUT = 30
# 每个账号失败次数上限，失败次数多有可能已经被禁
MAX_FAIL_TIME = 10
DEFAULT_REQUEST_HEADERS = {
    'Accept-Encoding': 'gzip',
}
# 打开重试请求
RETRY_TIMES = 10
RETRY_ENABLED = True
# Disable cookies (enabled by default)
COOKIES_ENABLED = False
# 下载中间件配置User-Agent池
USER_AGENTS = [
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
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
USER_PASS = "wh429004:ylsvtvu1"

PROXIES = [
    {"ip_port": "40.114.109.214:3128", "user_pass": ""},
    {"ip_port": "40.114.109.214:3128", "user_pass": ""},
    {"ip_port": "40.114.109.214:3128", "user_pass": ""},
    {"ip_port": "40.114.109.214:3128", "user_pass": ""},
]
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': None,
    # 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
    'yelpTest.middlewares.RandomUserAgent': 400,
    'yelpTest.middlewares.RandomProxy': 600,
    'yelpTest.middlewares.ProcessAllExceptionMiddleware': 750,
}
# 如果要保证纵向爬取的时候，数据漏爬，可以打开此配置
AUTOTHROTTLE_ENABLED = True
# scrapy_redis  将数据存放到 redis
ITEM_PIPELINES = {
    'yelpTest.pipelines.YelptestPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

# 开启扩展
MYEXT_ENABLED = True
# 配置空闲持续时间单位为 360个 ，一个时间单位为5s
IDLE_NUMBER = 360

# 在 EXTENSIONS 配置，激活扩展
EXTENSIONS = {
    'yelpTest.extensions.RedisSpiderSmartIdleClosedExensions': 500,
}


