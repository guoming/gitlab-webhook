from flask import Flask, request
import libs.ai
import config
import libs.feishu

app = Flask(__name__)


@app.route('/healthcheck', methods=['GET'])
def handler_healthcheck():
    return "{\"Status\":\"OK\"}", 200


@app.route('/webhook/<group>', methods=['POST'])
def handle_merge_request(group):
    payload = request.get_json()

    # 检查事件类型是合并请求
    if payload['object_kind'] == 'merge_request':

        # 获取合并请求的相关信息
        merge_request = payload['object_attributes']

        # 项目ID
        project_id = payload["project"]["id"]

        # 项目地址
        repo_url = payload["project"]["git_http_url"]

        # 用户名称
        user_name = payload["user"]["name"]

        # 目标分支
        target_branch = payload["object_attributes"]["target_branch"]

        # 源分支
        source_branch = payload["object_attributes"]["source_branch"]

        # 状态
        state = payload["object_attributes"]["state"]

        # 合并请求地址
        merge_request_url = payload["object_attributes"]["url"]

        # 合并请求ID
        merge_request_id = payload["object_attributes"]["iid"]

        if config.openai_open == 0:
            print("openai_open is 0, skip ai code review")
        else:
            # AI自动代码评审
            acr = libs.ai.AICodeReview(gitlab_server_url=config.gitlab_server_url,
                                       gitlab_private_token=config.gitlab_private_token,
                                       project_id=project_id,
                                       merge_request_id=merge_request_id,
                                       openai_api_key=config.openai_api_key)
            acr.ai_code_review()
            acr.comment()

        # 发送飞书消息
        card_data = {
            "repo_url": repo_url,
            "user_name": user_name,
            "target_branch": target_branch,
            "source_branch": source_branch,
            "state": state,
            "merge_request_url": merge_request_url
        }

        send_ret = libs.feishu.send_msg(group, card_data)

        if send_ret == 1:
            # 返回成功响应
            return 'ok', 200
        else:
            return "error", 500

    else:
        # 返回不支持的事件类型响应
        return 'OK', 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8000)
