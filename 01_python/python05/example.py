import requests
import pprint

api_key = '87246d75e1ce26e1392a087b3d1d88c5'
# 서울의 위도
lat = 37.56
# 서울의 경도
lon = 126.97

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
data = requests.get(url).json()
pprint.pprint(data)
pprint.pprint(data['name'])
pprint.pprint(data['weather'])
print(data['weather'][0]['description'])



