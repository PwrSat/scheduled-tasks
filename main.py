import requests
import os

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

parameters = {
    "lat": 3.595196,
    "lon": 98.672226,
    "appid": os.environ["WEATHER_APP_ID"],
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = any(hour_change["weather"][0]["id"] < 700 for hour_change in data["list"])

if will_rain:
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": "☔ Bring an umbrella, it's raining today!"
    }
    tg_response = requests.post(telegram_url, data=payload)
    tg_response.raise_for_status()
    print("Notifikasi terkirim:", tg_response.json())
