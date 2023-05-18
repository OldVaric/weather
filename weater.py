import datetime

import requests
from pprint import pprint
from config import api

def get_weather(city, api):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric'
        )
        data = r.json()
        # pprint(data)
        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Мелкий дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }



        city = data['name']
        weather_disckription = data["weather"][0]["main"]
        wind = data['wind']['speed']
        temp = data['main']['temp']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        if weather_disckription in code_to_smile:
            wd = code_to_smile[weather_disckription]
        else:
            wd = "Посмотрите в окно, не пойму что там за погода!"

        print(f'Погода в городе: {city}\nТемпература: {temp}°C {wd}\n'
              f'Максимальная температура: {temp_max}°C\n'
              f'Минимальная температура: {temp_min}°C\n'
              f'Влажность: {humidity}%\nДавление: {pressure}мм.рт.ст.\nВетер: {wind}м.с.\n'
              f'Восход солнца: {sunrise}\nЗакат солнца: {sunset}\nПродолжительность дня: {length}\n'
              f'Хорошего дня!')


    except Exception as ex:
        print(ex)
        print("Проверьте город")


def main():
    city = input("Водите город: ")
    get_weather(city, api)

if __name__ == '__main__':
    main()