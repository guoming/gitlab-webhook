import gitlab
import openai
class AICodeReview():
    
    def __init__(self,
                 gitlab_private_token,
                 project_id,
                 merge_request_id,
                 openai_api_key,
                 gitlab_server_url='https://jihulab.com',
                 ):
        self.gl = gitlab.Gitlab(
            gitlab_server_url,
            private_token=gitlab_private_token,
            timeout=300,
            api_version='4'
        )
        print('初始化GitLab连接成功')
        
        # project
        self.project_id = project_id
        self.project = self.gl.projects.get(project_id)
        print('找到project')
        
        # mr
        self.merge_request_id = merge_request_id
        self.merge_request = self.project.mergerequests.get(merge_request_id)
        print('找到mr')
        
        # changes
        self.changes = self.merge_request.changes()
        
        # openai
        openai.api_key = openai_api_key
        
        # comments
        self.review_notes = []
        
        # note
        self.note = ''
        
        
    def ai_code_review(self):
        
        print('开始code review')
        for change in self.changes['changes']:
            # https://platform.openai.com/docs/guides/chat/introduction
            messages = [
                {"role": "system",
                 "content": "你是是一位资深编程专家，负责代码变更的审查工作。需要给出审查建议。在建议的开始需明确对此代码变更给出「拒绝」或「接受」的决定，并且以格式「变更评分：实际的分数」给变更打分，分数区间为0~100分。然后，以精炼的语言、严厉的语气指出存在的问题。如果你觉得必要的情况下，可直接给出修改后的内容。建议中的语句可以使用emoji结尾。你的反馈内容必须使用严谨的markdown格式。"
                 },
                {"role": "user",
                 "content": f"请review这部分代码变更{change}",
                 },
            ]

            print('思考中...')
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )
            new_path = change['new_path']
            print(f'对 {new_path} review中...')
            response_content = response['choices'][0]['message']['content'].replace('\n\n', '\n')
            total_tokens = response['usage']['total_tokens']

            review_note = f'# `{new_path}`' + '\n\n'
            review_note += f'({total_tokens} tokens) {"AI review 意见如下:" }' + '\n\n'
            review_note += response_content
            
            self.review_notes.append(review_note)

    def comment(self, notice=None):
        if notice is None:
            review_note = '\n\n---\n\n'.join(self.review_notes)
            self.note = {'body': review_note}
            self.merge_request.notes.create(self.note)
            print('review内容', self.note)
            print('review完成')
        else:
            self.note = {'body': notice}
            self.merge_request.notes.create(self.note)
            print(notice)