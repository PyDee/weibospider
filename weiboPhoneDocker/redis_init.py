"""将本地微博id上传到初始url队列中"""
import redis
import os


def redis_init(spider_name, url):
    r = redis.Redis(host='redis')
    for key in r.scan_iter(f"{spider_name}*"):
        r.delete(key)
    file_path = os.getcwd() + '\\weibo.txt'
    count = 0
    with open(file_path, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()
            lines = lines.replace("\n", "")
            if not lines:
                break
                pass
            new_url = url.format(lines)
            r.lpush(f'{spider_name}:start_urls', new_url)
            count = count + 1
            if count % 10000 == 0:
                print("execute insert! count is %d" % count)


def init_user_spider():
    # change the user ids
    url = "https://m.weibo.cn/api/container/getIndex?type=uid&value={}"
    redis_init('user_spider', url)


if __name__ == '__main__':
    init_user_spider()
