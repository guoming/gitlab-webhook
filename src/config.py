import os
from dotenv.main import load_dotenv

load_dotenv()

print("------------------开始系统环境变量------------------")
# git token
gitlab_private_token = os.getenv('GITLAB_PRIVATE_TOKEN', "<gitlab private token>")
print("GITLAB_PRIVATE_TOKEN: " + gitlab_private_token)
# git 服务端地址
gitlab_server_url = os.getenv('GITLAB_SERVER_URL', "<gitlab address>")
print("GITLAB_SERVER_URL: " + gitlab_server_url)
# openai api key
openai_api_key = os.getenv('OPENAI_API_KEY', "<openai api key>")
print("OPENAI_API_KEY: " + openai_api_key)

openai_open = os.getenv('OPENAI_OPEN', "0")
print("OPENAI_OPEN: " + openai_open)
print("------------------完成系统环境变量------------------")
