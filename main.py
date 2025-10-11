import requests
import os
from dotenv import load_dotenv


load_dotenv()
API = os.getenv("TOKEN")
months = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря"
}


payload = {"api_key": API, "year": "2025", "country": "RU"}
url = f"https://calendarific.com/api/v2/holidays?api_key={API}"
response = requests.get(url, params=payload)
data = response.json()
for holiday in data["response"]["holidays"]:
    print(f"Дата: {holiday["date"]["datetime"]["month"]} {months[holiday["date"]["datetime"]["month"]]}")
    print(f"Название: {holiday["name"]}")
    print(f"Описание: {holiday["description"]}\n")