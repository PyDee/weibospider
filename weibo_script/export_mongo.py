from pymongo import MongoClient

# 建立MongoDB数据库连接
client = MongoClient('127.0.0.1', 27017)

# 用户验证
db = client.weibo
# db.authenticate("账号", "密码")

# 连接所用集合，也就是我们通常所说的表
collection = db.user

# 接下里就可以用collection来完成对数据库表的一些操作
with open('user.txt', 'w+') as f:  # 接下来可实现提取想要的字段内的数据
    for item in collection.find({}, {"_id": 1}):
        print(item['_id'])
        f.write(str(item['_id']))
        f.write('\n')
