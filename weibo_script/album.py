import requests
import json
from pprint import pprint

album_containerid = '1078036197250416'
userItem = dict()
url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=6197250416&containerid={}'.format(album_containerid)
ret = requests.get(url)
result = json.loads(ret.text)
pprint(result)
exit()
