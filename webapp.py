import json

import requests
from flask import Flask, render_template, request

from shared import TOKEN

app = Flask(__name__, template_folder='webapp')


@app.get('/')
def root():
    return render_template('index.html')


@app.get('/returnResult')
def result():
    args = request.args['query']
    word = request.args['word']
    res = {
        'type': 'article',
        'id': 0,
        'title': 'Result',
        'input_message_content': {
            'message_text': word
        }
    }
    base_url = f'https://api.telegram.org/bot{TOKEN}' \
               f'/answerWebAppQuery?web_app_query_id={args}&result={json.dumps(res)}'
    req = requests.get(base_url)
    print(req.json())


@app.get('/<path:path>')
def push(path: str):
    return render_template(path)


if __name__ == '__main__':
    app.run()
