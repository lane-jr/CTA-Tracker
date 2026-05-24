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

response = requests.get(url)
print(response.status_code)

train_data = response.json()

arrival_times = train_data["ctatt"]["eta"][0]

if arrival_times["isApp"] == "1":
    print("Due")

else:
    arr_time = datetime.fromisoformat(arrival_times["arrT"])
    current_time = datetime.now(arr_time.tzinfo)

    min = round(
        (arr_time - current_time).total_seconds() / 60
    )
    
    print(f"{min} min")