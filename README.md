# github-webhook
## 1. 项目描述
 * 项目名称：github-webhook
 * 项目功能：Gitlab Webhook服务，用于将Gitlab事件转发到飞书群中并通过OpenAi进行代码评审
## 2. 安装说明

### 2.1. 安装依赖

``` sh 
pip3 install -r requirements.txt
```

### 2.2. 启动服务

#### 2.2.1 使用Docker启动

``` sh
docker build -f Dockerfile -t guoming/gitlab-webhook ./src
```

``` sh
docker run --rm --name gitlab-webhook -d \
-e GITLAB_SERVER_URL=http://xxx \
-e GITLAB_PRIVATE_TOKEN=xxx \
-e OPENAI_API_KEY=xxx \
-p 8000:8000 \
guoming/gitlab-webhook
```

#### 2.2.2 使用Python启动

``` sh
# 设置环境变量
GITLAB_SERVER_URL=<Gitlab Address>
GITLAB_PRIVATE_TOKEN=<Gitlab PriateToken>
OPENAI_API_KEY=<OpenAPI Key>
# 启动服务
python3 app.py
```

## 3. 使用说明
1. 在飞书群中创建机器人，获取Webhook地址。如： https://open.feishu.cn/open-apis/bot/v2/hook/<group>
1. 在Gitlab项目中设置Webhook，地址为 `http://<Server Address>:<Server Port>/webhook/<group>`
2. 在Gitlab项目中设置Merge Request事件触发Webhook
