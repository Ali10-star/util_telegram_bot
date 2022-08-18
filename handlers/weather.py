import os
from urllib import response
import requests as http_client
from telegram import Update
from telegram.ext import ContextTypes
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('OPEN_WEATHER_API_KEY')
URL = 'http://api.openweathermap.org/data/2.5/weather'
# https://api.openweathermap.org/data/2.5/weather?q={QUERY}&appid=34fb43e4e1d267ad9b6c166f3ddc10b4

async def weather_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat_id = update.message.chat_id
    bot = context.bot
    query = context.args[0] if context.args else "London"
    response = http_client.get(URL, params={'q': query, 'appid': API_KEY})
    await bot.send_message(chat_id=chat_id, text=
        f"{dict_to_str(response.json())}"
    )

def celsius(kelvin: float) -> float:
    return kelvin - 273.15

def dict_to_str(dictionary: dict) -> str:
    return "\n".join(f"{key}: {value}" for key, value in dictionary.items())