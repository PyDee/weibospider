# weibospider
微博用户信息数据采集

## 初始化数据
在 data_init 文件夹下添加文件 weibo.txt
 
weibo.txt内容格式为：
```angular2
1111111111111
2222222222222
3333333333333
```
添加 weibo_id 后，执行 python redis_init.py 进行数据初始化

## 代理的使用
在middleware中实现了使用代理的代码

推荐使用黑洞IP代理(https://www.heidongip.com/)，不是打广告，单纯是因为便宜

在 settings 中修改 proxy_url 参数为你的 API 即可
