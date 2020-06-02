import pymongo
from pymongo.errors import DuplicateKeyError

from settings import MONGO_HOST, MONGO_PORT, MONGO_DB


class WeibophonedockerPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
        db = client[MONGO_DB]

        # 需要账号密码时开启
        # db.authenticate(MONGO_USER, MONGO_PSW, mechanism='SCRAM-SHA-1')
        self.Users = db["user"]
        self.Tweets = db["tweets"]

    def process_item(self, item, spider):
        if spider.name == 'phone_user':
            self.insert_item(self.Users, item)
        elif spider.name == 'phone_tweet':
            self.insert_item(self.Tweets, item)
        return item

    @staticmethod
    def insert_item(collection, item):
        try:
            collection.insert(dict(item))
        except DuplicateKeyError:
            pass
