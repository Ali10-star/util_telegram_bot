import requests as http_client
from telegram import Update
import random as rand
from telegram.ext import ContextTypes

def fetch_random_unsplash():
    ACCESS_KEY = 'mZJFczj1LxorOGYL_W3qowmUd5cwvEih_U38bOrSU3I'
    # SECRET_KEY = 'iLJ2jZoBaa3ytfl6wR_JhQIZ6Zvtg4wys6zepZ9gwNg'
    URL = f"https://api.unsplash.com/photos/random/?client_id={ACCESS_KEY}"
    response = http_client.get(URL)
    json_res = response.json()
    status_code = response.status_code
    print(status_code)
    print("\n\n\n")
    photo_url = json_res["urls"]["full"]
    taken_by = json_res['user']['name']
    taken_by_username = json_res['user']['username']
    preview = json_res["urls"]["small"]
    print(f"Taken by {taken_by}, username: {taken_by_username}")
    # return photo_url, preview, taken_by, taken_by_username, status_code

fetch_random_unsplash()