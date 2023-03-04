import requests
import json

url = 'https://weather.contrateumdev.com.br/api/weather/city/?city=Recife,Pernambuco'

response = requests.get(url=url)

clima = response.json()

#print(clima)


print('Temp: ', clima['main']['temp'])
print('Sensação termica: ', clima['main']['feels_like'])
print('temp minima: ', clima['main']['temp_min'])
print('temp max: ', clima['main']['temp_max'])
print('Umidade: ', clima['main']['humidity'], '%')
print('Tempo: ', clima['weather'][0]['description'])


