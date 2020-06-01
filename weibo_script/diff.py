with open('user.txt', 'r') as user:  # 接下来可实现提取想要的字段内的数据
    user_content = user.readlines()

with open('weibo.txt', 'r') as user:  # 接下来可实现提取想要的字段内的数据
    weibo_content = user.readlines()

with open('weibo.txt', 'w+') as diff:
    ret = list(set(user_content) ^ set(weibo_content))
    for index, item in enumerate(ret):
        print(index, item)
        diff.write(str(item))
        diff.write('\n')
