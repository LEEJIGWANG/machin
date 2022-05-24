from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/text1', methods=['GET', 'POST'])
def sms():
    text = request.get_json() #client에서 온 요청을 text변수에 넣어줌
    print(text)
    result = '광고 메시지입니다.'
    return str(result)

if __name__ == '__main__':
    app.run(host= '',debug=True)