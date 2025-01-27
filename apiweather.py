import requests
API_key = 'e491cc612d2d07d3829c4492b362ff67'
city = input('ใส่ชื่อเมืองที่ต้องการจะค้นหา :')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}'
#https://api.openweathermap.org/data/2.5/weather?q=bangkok&appid=API_key=e491cc612d2d07d3829c4492b362ff67
result = requests.api.get(url).json()

city_name = result['name']
country = result['sys']['county']
weather = result['weather'][0]()
des
print(result)