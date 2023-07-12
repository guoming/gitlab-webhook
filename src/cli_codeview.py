import re
import sys
import config
import libs.ai
import os
import gitlab


# 从命令行中获取参数
args = sys.argv

matchs= re.match("^http[s]?:\/\/(.*?)\/(.*)\/merge_requests\/(.*)$", args[1])

project_path= matchs[2]
print("project_path: ", project_path)

# 获取 693 部分
merge_request_iid = matchs[3]
print("merge_request_iid: ", merge_request_iid)

gl= gitlab.Gitlab(
            config.gitlab_server_url,
            private_token=config.gitlab_private_token,
            timeout=300,
            api_version='4')

project = gl.projects.get(project_path)

# AI自动代码评审
acr = libs.ai.AICodeReview(gitlab_server_url=config.gitlab_server_url,
                        gitlab_private_token=config.gitlab_private_token,
                        project_id=project.get_id(),
                        merge_request_id=merge_request_iid,
                        openai_api_key=config.openai_api_key)
acr.ai_code_review()
acr.comment()