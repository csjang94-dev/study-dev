# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "안녕! 나는 도커로 실행중이야!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)