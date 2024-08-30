import requests as req

from datetime import datetime

import os



APP_ID = os.environ["NT_APP_ID"]  # "a0082fec"

API_KEY = os.environ["NT_API_KEY"]  # "0139b127310aac1885c4e8af3cea094c    "

GENDER = "male"

WEIGHT_KG = "80"

HEIGHT_CM = "179"

AGE = "24"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("What exercise did you do ? ")

SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]

headers = {

    "x-app-id": APP_ID,

    "x-app-key": API_KEY,

}

parameters = {

    "query": exercise_text,

    "gender": GENDER,

    "weight_kg": WEIGHT_KG,

    "height_cm": HEIGHT_CM,

    "age": AGE

}

response = req.post(exercise_endpoint, json=parameters, headers=headers)

result = response.json()

print(result)

today_date = datetime.now().strftime("%d-%m-%Y")

now_time = datetime.now().strftime("%X")

bearer_headers = {

    "Authorization": f"Bearer {os.environ['TOKEN']}"

}

for exercise in result["exercises"]:
    sheet_inputs = {

        "workout": {

            "date": today_date,

            "time": now_time,

            "exercise": exercise["name"].title(),

            "duration": exercise["duration_min"],

            "calories": exercise["nf_calories"]

        }

    }

    sheet_response = req.post(SHEET_ENDPOINT, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.status_code)

    print(sheet_response.text)

    print(SHEET_ENDPOINT)