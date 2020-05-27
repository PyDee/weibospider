import requests
import time
import json
from pprint import pprint

userItem = dict()
url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=6197250416'
response = requests.get(url)
result = json.loads(response.text)
# pprint(result)
# exit()
gender = '男'
result_data = result.get('data')
user_info = result_data.get('userInfo')
tabs_info = result_data.get('tabsInfo').get('tabs')

userItem['_id'] = user_info.get('id')
userItem['nick_name'] = user_info.get('screen_name')
userItem['crawl_time'] = int(time.time())
userItem['gender'] = gender if user_info.get('gender') == 'm' else '女'
userItem['brief_introduction'] = user_info.get('description')
userItem['vip_level'] = user_info.get('mbrank')
userItem['follows_num'] = user_info.get('follow_count')
userItem['fans_num'] = user_info.get('followers_count')
userItem['tweets_num'] = user_info.get('statuses_count')
for item in tabs_info:
    if item.get('tab_type') == 'profile':
        userItem['profile_id'] = item.get('containerid')
    if item.get('tab_type') == 'weibo':
        userItem['weibo_id'] = item.get('containerid')
    if item.get('tab_type') == 'album':
        userItem['album_id'] = item.get('containerid')
pprint(userItem)

data = {
    'data': {'avatar_guide': [],
             'fans_scheme': 'https://m.weibo.cn/p/index?containerid=231051_-_fans_intimacy_-_3112824195&luicode=10000011&lfid=1005053112824195',
             'follow_scheme': 'https://m.weibo.cn/p/index?containerid=231051_-_followersrecomm_-_3112824195&luicode=10000011&lfid=1005053112824195',
             'scheme': 'sinaweibo://userinfo?uid=3112824195&type=uid&value=3112824195&_T_WM=52042539111&v_p=42&luicode=10000011&lfid=1005053112824195',
             'showAppTips': 1,
             'tabsInfo': {'selectedTab': 1,
                          'tabs': [{'containerid': '2302833112824195',
                                    'hidden': 0,
                                    'id': 1,
                                    'must_show': 1,
                                    'tabKey': 'profile',
                                    'tab_type': 'profile',
                                    'title': '主页'},
                                   {'apipath': '/profile/statuses',
                                    'containerid': '1076033112824195',
                                    'hidden': 0,
                                    'id': 2,
                                    'must_show': 1,
                                    'tabKey': 'weibo',
                                    'tab_type': 'weibo',
                                    'title': '微博',
                                    'url': '/index/my'},
                                   {'containerid': '1078033112824195',
                                    'hidden': 0,
                                    'id': 10,
                                    'must_show': 0,
                                    'tabKey': 'album',
                                    'tab_type': 'album',
                                    'title': '相册'}]},
             'userInfo': {'avatar_hd': 'https://wx3.sinaimg.cn/orj480/b989ed83ly8gcdemg2y21j20ro0rotas.jpg',
                          'close_blue_v': False,
                          'cover_image_phone': 'https://tva2.sinaimg.cn/crop.0.0.640.640.640/a1d3feabjw1ecasunmkncj20hs0hsq4j.jpg',
                          'description': '为未来的我而努力💚',
                          'follow_count': 155,
                          'follow_me': False,
                          'followers_count': 51,
                          'following': False,
                          'gender': 'f',
                          'id': 3112824195,
                          'like': False,
                          'like_me': False,
                          'mbrank': 0,
                          'mbtype': 0,
                          'profile_image_url': 'https://tvax3.sinaimg.cn/crop.0.0.996.996.180/b989ed83ly8gcdemg2y21j20ro0rotas.jpg?KID=imgbed,tva&Expires=1590588249&ssig=DkN6OdbHX8',
                          'profile_url': 'https://m.weibo.cn/u/3112824195?uid=3112824195&luicode=10000011&lfid=1005053112824195',
                          'screen_name': '琪琪琪咩Sickey',
                          'statuses_count': 29,
                          'toolbar_menus': [
                              {'name': '关注',
                               'params': {'uid': 3112824195},
                               'pic': '',
                               'type': 'profile_follow'},
                              {'name': '聊天',
                               'params': {
                                   'scheme': 'sinaweibo://messagelist?uid=3112824195&nick=琪琪琪咩Sickey'},
                               'pic': 'http://h5.sinaimg.cn/upload/2015/06/12/2/toolbar_icon_discuss_default.png',
                               'scheme': 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=https%3A%2F%2Fm.weibo.cn%2Fapi%2Fcontainer%2FgetIndex%3Ftype%3Duid%26value%3D3112824195',
                               'type': 'link'},
                              {'name': '文章',
                               'params': {
                                   'scheme': 'sinaweibo://cardlist?containerid=2303190002_445_3112824195_WEIBO_ARTICLE_LIST_DETAIL&count=20'},
                               'pic': '',
                               'scheme': 'https://m.weibo.cn/p/index?containerid=2303190002_445_3112824195_WEIBO_ARTICLE_LIST_DETAIL&count=20&luicode=10000011&lfid=1005053112824195',
                               'type': 'link'}],
                          'urank': 14,
                          'verified': False,
                          'verified_type': -1}},
    'ok': 1
}
