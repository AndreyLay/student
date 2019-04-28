import requests
import json

def iata_code():
    origin = input("Введите название города: ")
    link = "https://www.travelpayouts.com/widgets_suggest_params?q=Из%20"+origin+"%20в%20Лондон"
    try:
        data = json.loads(requests.get(link).text)
        data = data['origin']
        print('IATA код запрошенного города:', data['iata'])
    except:
        print("Нам жаль. Этому городу пока не присвоен код IATA.")

iata_code()