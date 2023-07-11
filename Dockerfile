# 使用官方 Python 镜像作为基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中的工作目录
COPY . /app

# 安装项目依赖
RUN pip3 install --no-cache-dir -r requirements.txt

# 设置环境变量（可选）
ENV GITLAB_SERVER_URL=http://gitlab.com
ENV GITLAB_PRIVATE_TOKEN=xxx
ENV OPENAI_API_KEY=xxx
ENV OPENAI_OPEN=0

ENTRYPOINT ["python3", "app.py"]