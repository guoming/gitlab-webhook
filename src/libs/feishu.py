import requests
import json

def send_msg(group,card_data):

    # 飞书机器人的 Webhook URL
    webhook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/'+group

    # 飞书卡片消息的内容
    card_data = {
        "msg_type": "interactive",
        "card": {
            "config": {
                "wide_screen_mode": True
            },
            "header": {
                "template": "turquoise",
                "title": {
                    "content": "Git Merge Request",
                    "tag": "plain_text"
                }
            },
            "elements": [

                {
                    "tag": "div",
                    "text": {
                        "content": "仓库地址：" + card_data['repo_url'],
                        "tag": "lark_md"
                    }
                },
                  {
                    "tag": "div",
                    "text": {
                        "content": "来源分支：" + card_data['source_branch'],
                        "tag": "lark_md"
                    }
                },
                  {
                    "tag": "div",
                    "text": {
                        "content": "目标分支：" + card_data['target_branch'],
                        "tag": "lark_md"
                    }
                },
                  {
                    "tag": "div",
                    "text": {
                        "content": "提交人：" + card_data['user_name'],
                        "tag": "lark_md"
                    }
                },
                  {
                    "tag": "div",
                    "text": {
                        "content": "状态：" + card_data["state"],
                        "tag": "lark_md"
                    }
                },
                  {
                    "tag": "div",
                    "text": {
                        "content": "详情点击 <a href=\"" + card_data['merge_request_url'] + "\">这里</a> ",
                        "tag": "lark_md"
                    }
                }

            ]
        }
    }

    # 发送 POST 请求
    response = requests.post(webhook_url, data=json.dumps(card_data))

    # 检查请求是否成功
    if response.status_code == 200:
        print('发送成功')
        return 1
    else:
        print('发送失败')
        return 0
