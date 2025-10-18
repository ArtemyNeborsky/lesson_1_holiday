import requests
import os
from dotenv import load_dotenv


API = os.getenv("TOKEN")
MONTHS = {
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


def main():
    load_dotenv()
    payload = {"api_key": API, "year": "2025", "country": "RU"}
    url = "https://calendarific.com/api/v2/holidays"
    response = requests.get(url, params=payload)
    for holiday_data in response.json()["response"]["holidays"]:
        print(f"Дата: {holiday_data["date"]["datetime"]["month"]} {MONTHS[holiday_data["date"]["datetime"]["month"]]}")
        print(f"Название: {holiday_data["name"]}")
        print(f"Описание: {holiday_data["description"]}\n")


if __name__ == "__main__":
    main()
