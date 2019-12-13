import requests
from decouple import config

# API 요청 기본사항
url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')

# 봇과 대화하고 있는 사용자의 chat_id추출
chat_id = config('CHAT_ID')
# chat_id = requests.get(f'{url}/bot{token}/getUpdates').json()["result"][0]["message"]["from"]["id"]

# 보낼 메세지 입력받기
text = input('메세지를 입력하세요: ')

# API에 요청을 보내 메세지 보내기
send_message = requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

print(send_message.text)