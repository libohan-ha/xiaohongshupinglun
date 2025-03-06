from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

COZE_API_URL = 'https://api.coze.cn/v1/workflow/run'
COZE_API_KEY = 'pat_qdPzK2PDXiueY58uEySWNiBDUpKyrX3nYncAfWxyboXG7QLAfrv0qSwyqcv19YhS'
WORKFLOW_ID = '7478705876653522978'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_comment', methods=['POST'])
def get_comment():
    try:
        url = request.form.get('url')
        
        headers = {
            'Authorization': f'Bearer {COZE_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'parameters': {
                'input': url
            },
            'workflow_id': WORKFLOW_ID
        }
        
        response = requests.post(COZE_API_URL, headers=headers, json=data)
        result = response.json()
        
        if result['code'] == 0:
            output_data = json.loads(result['data'])
            return jsonify({'success': True, 'comment': output_data['output']})
        else:
            return jsonify({'success': False, 'error': '获取评论失败'})
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)