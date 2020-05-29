# 指定创建的基础镜像
FROM python:3.6

# 指定作者
MAINTAINER Bossen <bossenCheung@gmail.com>

# 指定工作目录,和本地目录结构是相同的
WORKDIR /app

#环境变量设置，将/usr/local/bin:$PATH赋值给PATH，即增加/usr/local/bin这个环境变量路径
ENV PATH /usr/local/bin:$PATH

# 将本地项目所有内容放置到虚拟容器的/code目录下
ADD . /code
RUN pip3 install -r requirements.txt -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com