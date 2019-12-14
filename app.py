from flask import Flask, render_template, request
from decouple import config
import requests, pprint, random, html
app = Flask(__name__)
#텔레그램 API
url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')

google_url = 'https://translation.googleapis.com/language/translate/v2'
google_key = config('GOOGLE_TOKEN')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route(f'/{token}',methods=['POST'])
def telegram():
    # 1. 메아리 기능
    # 데이터 구조확인
    pprint.pprint(request.get_json())
    # 2. 사용자 아이디, 메시지 추출
    chat_id = request.get_json()['message']['chat']['id']
    message = request.get_json()['message']['text']
    print(request.get_json)

    # 사용자가 로또라고 입력하면 로또번호 6개 돌려주기
    if message == '로또':
        result = random.sample([ i for i in range(1,46)],6)

    # 구글번역 검색결과 도출
    elif message[:4] == '/번역 ':
        data = {
            'q' : message[4:],
            'source' : 'ko',
            'target' : 'en',
            'format' : 'text'
        }
        response = requests.post(f'{google_url}?key={google_key}',data).json()
        result = html.unescape(response['data']['translations'][0]['translatedText'])
    # 날씨를 알아볼까


    # 그 외의 경우엔 메아리
    else:
        result = message

    # 3. 텔레그램 API에 요청해서 답장보내주기
    requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={result}')
    return '', 200


# @app.route('/write')
# def write():
#     return render_template('write.html')

# @app.route('/send')
# def send():
#     message = request.args.get('message')
#     send_message = requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={message}')
#     return render_template('send.html', message = message)


if __name__ == '__main__':
    app.run(debug=True)