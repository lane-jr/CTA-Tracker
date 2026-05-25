import fastapi
import requests
import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

#jarvis station id
#Jarvis = "41190"

api_key = os.getenv("API_KEY")

url = (
    "https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"
    f"?key={api_key}"
    "&mapid=41190"
    "&outputType=JSON"
)

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    train_data = response.json()

    arrivals = train_data["ctatt"]["eta"]

    if not arrivals:
        print("No upcoming trains")
        exit()

except requests.exceptions.RequestException:
    print("Network/API error")
    exit()

except KeyError:
    print("Unexpected API format")
    exit()

except Exception as e:
    print(f"Unexpected error: {e}")
    exit()

train_data = response.json()

for train in train_data["ctatt"]["eta"]:

    if train["trDr"] == "5":

        if train["isApp"] == "1":
            print("arriving")

        else:
            arr_time = datetime.fromisoformat(train["arrT"])
            current_time = datetime.now(arr_time.tzinfo)

            minutes = round(
                (arr_time - current_time).total_seconds() / 60
            )

            print(f"Train toward the Loop in {minutes} min")
