import requests
import os
from dotenv import load_dotenv


load_dotenv()
API = os.getenv("TOKEN")
months = {
    1: "Января",
    2: "Февраля",
    3: "Марта",
    4: "Апреля",
    5: "Мая",
    6: "Июня",
    7: "Июля",
    8: "Августа",
    9: "Сентября",
    10: "Октября",
    11: "Ноября",
    12: "Декабря"
}


payload = {"api_key": API, "year": "2025", "country": "RU"}
url = f"https://calendarific.com/api/v2/holidays"
response = requests.get(url, params=payload)
data = response.json()
for holiday in data["response"]["holidays"]:
    print(f"Дата: {holiday["date"]["datetime"]["month"]} {months[holiday["date"]["datetime"]["month"]]}")
    print(f"Название: {holiday["name"]}")
    print(f"Описание: {holiday["description"]}\n")