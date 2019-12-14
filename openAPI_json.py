import requests, pprint
from decouple import config

# url = 'https://translation.googleapis.com/language/translate/v2'
# key = config('GOOGLE_TOKEN')

# data ={
#     'q': '엄마 판다는 새끼가 있네',
#     'source' : 'ko',
#     'target' : 'en',
# }
# result = requests.post(f'{url}?key={key}',data).json()
# print(result)

# http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}
weather_key = config('OPEN_WEATHER')
city=1835848
result = requests.post(f'http://api.openweathermap.org/data/2.5/forecast?id={city}&APPID={weather_key}').json()
pprint.pprint(result['list'][0]['weather'])
