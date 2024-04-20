
### **一个用FastAPI写的极其简略粗糙的“回调”接口**

## 一、部署方法

1. 拉取仓库
```shell
git clone https://github.com/MoMingRose/WxReadDetect
```

2. 构建并部署 Docker 容器

```shell
# 进入项目目录
cd WxReadDetect

# 可以先进行镜像的构建，也可以直接使用docker compose 或者 docker-compose
docker compose up --build -d

# 老版本可以使用
# docker-compose up --build -d
```

## 二、使用方法

【注意】如果是使用了阅读项目的，部署完成运行并且成功访问后\
可以不用往下看了，直接把你的ip地址和端口粘贴到 common.yaml 中即可
如果进行了内网穿透，则直接使用穿透后的地址即可

这里推荐一个免费的内网穿透网址（截止目前2024.04.20为止，仍然是免费的）: https://hpproxy.cn/#/



1. 构建client_id、target_id、redirect

`client_id`表示`客户端id`
> 也就是当前正在访问网页的用户，它应该具有唯一性

`target_id`表示要`接收消息的客户端id`
> 也就是其他正在访问网页或者正在等待消息的程序用户，它也应该具有唯一性

`redirect`表示`实际要访问的链接地址`
> (1) 用户访问网页，并且发送已访问的通知给 target_id (监控访问成功性的客户端) \
> (2) 等待target_id回复接收通知后，再重定向到此 redirect 链接
