import datetime

import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import API_TOKEN, api

PROXY_URL = "http://proxy.server:3128"
bot = Bot(token=API_TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await message.reply("Привет работяга, чтобы узнать погоду напиши мне название города!")


@dp.message_handler()
async def test(message: types.Message):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={api}&units=metric'
        )
        data = r.json()


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
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])

        if weather_disckription in code_to_smile:
            wd = code_to_smile[weather_disckription]
        else:
            wd = "Посмотрите в окно, не пойму что там за погода!"


        await message.reply(f'***Погода в городе: {city}***\nТемпература: {temp}°C {wd}\n'
                          f'Влажность: {humidity}%\nДавление: {pressure}мм.рт.ст.\nВетер: {wind}м.с.\n'
                          f'Восход солнца: {sunrise}\nЗакат солнца: {sunset}\nПродолжительность дня: {length}\n'
                          f'***Хорошего дня!***'
                         )

    except:
        await message.reply("\U00002620 Ты меня обманул, такого нет города!!! \U00002620")


if __name__ == "__main__":
    executor.start_polling(dp)