# github-webhook
## 1. 项目描述
 * 项目名称：github-webhook
 * 项目功能：Gitlab Webhook服务，用于将Gitlab事件转发到飞书群中并通过OpenAi进行代码评审
## 2. 如何安装

### 2.1. 安装依赖

``` sh 
pip3 install -r requirements.txt
```

## 3. 如何使用

### 2.2. 启动服务

#### 2.2.1 使用容器

* 构建镜像
``` sh
docker build -f Dockerfile -t geniusming/gitlab-webhook ./src
```
* 启动容器
``` sh
docker run --rm --name gitlab-webhook -d \
-e GITLAB_SERVER_URL=http://xxx \
-e GITLAB_PRIVATE_TOKEN=xxx \
-e OPENAI_API_KEY=xxx \
-p 8000:8000 \
geniusming/gitlab-webhook
```
* Helm部署
```sh
helm install gitlab-webhook ./helm
```

#### 2.2.2 使用Python

``` sh
# 设置环境变量
export GITLAB_SERVER_URL=<Gitlab Address>
export GITLAB_PRIVATE_TOKEN=<Gitlab PriateToken>
export OPENAI_API_KEY=<OpenAPI Key>
# 启动服务
python3 app.py
```

### 2.3. 配置
1. 在飞书群中创建机器人，获取Webhook地址。如： https://open.feishu.cn/open-apis/bot/v2/hook/<group>
1. 在Gitlab项目中设置Webhook，地址为 `http://<Server Address>:<Server Port>/webhook/<group>`
2. 在Gitlab项目中设置Merge Request事件触发Webhook
