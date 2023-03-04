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

'''

    Pegar temperatura e clima com cidade e estado
    PEGAR TEMPERATURA E CLIMA COM CIDADE E ESTADO
    GET TEMPERATURE AND CLIMATE FOR CITY AND STATE
    get: https://weather.contrateumdev.com.br/api/weather/city/?city=Belo%20Horizonte,minas%20gerais
    Para cidades com nome composto usar %20 no lugar dos espaços

    GET TEMPERATURE AND CLIMATE FOR LATITUDE AND LONGITUDE
    get: https://weather.contrateumdev.com.br/api/weather?lat=-19.8218131&lon=-44.0094874

    github do criador: https://github.com/jhowbhz/weather-api

    outras API que podem ser uteis:
    https://openweathermap.org/current
    https://hgbrasil.com/status/weather

'''


