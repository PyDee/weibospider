import requests
import time
import json
from pprint import pprint

profile_containerid = '2302836197250416'
userItem = dict()
url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=6197250416&containerid={}'.format(profile_containerid)
ret = requests.get(url)
result = json.loads(ret.text)
pprint(result)
exit()
data = {'data': {'banners': None,
                 'cardlistInfo': {'can_shared': 0,
                                  'cardlist_menus': [{'name': '刷新',
                                                      'type': 'button_menus_refresh'},
                                                     {'name': '返回首页',
                                                      'params': {'scheme': 'sinaweibo://gotohome'},
                                                      'type': 'gohome'}],
                                  'cardlist_title': '个人主页',
                                  'containerid': '2302833112824195',
                                  'desc': '',
                                  'page': None,
                                  'show_style': 1,
                                  'v_p': '42'},
                 'cards': [{'card_group': [{'actionlog': {'cardid': ''},
                                            'card_type': 41,
                                            'display_arrow': 0,
                                            'item_content': '其他',
                                            'item_name': '所在地',
                                            'itemid': '',
                                            'scheme': ''},
                                           {'actionlog': {'act_code': 594,
                                                          'cardid': '2302833112824195_-_WEIBO_INDEX_PROFILE_ABOUT',
                                                          'ext': 'uid:0|ouid:3112824195|verified_type:-1|ptype:0|load_read_level:',
                                                          'fid': '2302833112824195',
                                                          'unicode': '10000198'},
                                            'card_type': 6,
                                            'card_type_name': '更多基本资料',
                                            'desc': '更多基本资料',
                                            'itemid': 'more_web',
                                            'scheme': 'https://m.weibo.cn/p/index?containerid=2302833112824195_-_INFO&title=%E5%9F%BA%E6%9C%AC%E8%B5%84%E6%96%99&luicode=10000011&lfid=2302833112824195',
                                            'show_type': 0,
                                            'title': '更多基本资料'}],
                            'card_type': 11,
                            'card_type_name': '',
                            'itemid': '',
                            'show_type': 2,
                            'title': ''},
                           {'async_api': '/api/container/getItem?itemid=2306183112824195_-_HOTMBLOG&download=',
                            'card_group': [],
                            'card_type': 11,
                            'is_asyn': 1,
                            'itemid': '2306183112824195_-_HOTMBLOG'},
                           {'actionlog': {'act_code': '2961',
                                          'cardid': '2302833112824195_-_PROFILE_TOURIST_BUTTON',
                                          'ext': 'uid:0|ouid:3112824195|verified_type:-1|ptype:0|load_read_level:',
                                          'fid': '2302833112824195',
                                          'unicode': '10000198'},
                            'card_type': 7,
                            'desc': '登录注册后查看更多微博\n立即查看 >',
                            'desc_alignment': 1,
                            'highlight': {'desc_em': [[12, 20]]},
                            'scheme': 'https://m.weibo.cn/feature/applink?scheme=sinaweibo%3A%2F%2Flogin'}],
                 'scheme': 'sinaweibo://cardlist?containerid=2302833112824195&type=uid&value=3112824195&_T_WM=91565906302&v_p=42&luicode=10000011&lfid=2302833112824195'},
        'ok': 1}
