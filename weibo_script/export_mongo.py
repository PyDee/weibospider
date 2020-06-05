from pymongo import MongoClient
import os

# 建立MongoDB数据库连接
client = MongoClient('127.0.0.1', 27017)

# 用户验证
db = client.weibo
# db.authenticate("账号", "密码")

# 连接所用集合，也就是我们通常所说的表
collection = db.tweets

# 接下里就可以用collection来完成对数据库表的一些操作
k = 0
name = ''
# with open('tweet.txt', 'w+', encoding="utf-8") as f:  # 接下来可实现提取想要的字段内的数据
for item in collection.find({}, {'_id': 0, 'tool': 1, 'created_at': 1, "user_id": 1}):
    if item["tool"] != name:
        k += 1
        # if k == 20:
        #     break
    # os.system("cmd /u")
    os.system("echo {}----{}----{} >> tweet.txt".format(item["tool"], item["created_at"], item["user_id"]))
    os.system("echo {} >> tweet.txt".format('\n'))
    print(k)
