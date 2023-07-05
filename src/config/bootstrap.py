import os
print("------------------开始系统环境变量------------------")
# git token
gitlab_private_token = os.getenv('GITLAB_PRIVATE_TOKEN', "<gitlab private token>")
print("gitlab_private_token: " + gitlab_private_token)
# git 服务端地址
gitlab_server_url = os.getenv('GITLAB_SERVER_URL', "<gitlab address>")
print("gitlab_server_url: " + gitlab_server_url)
# openai api key
openai_api_key = os.getenv('OPENAI_API_KEY', "<openai api key>")
print("openai_api_key: " + openai_api_key)
print("------------------完成系统环境变量------------------")
