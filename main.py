import requests
import os
from requests.auth import HTTPBasicAuth
from datetime import datetime
import time

#added to environment variable
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

GENDER = "Your gender"
WEIGHT_KG = "Your weight"
HEIGHT_CM = "Your height"
AGE = "Your age"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

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

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]

#shetty API endpoint
sheety_endpoint = "https://api.sheety.co/f3c745f8a24a93bba75c5156fd1cd446/workoutTracking/workouts"
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHETTY_PASSWORD = os.environ.get("SHETTY_PASSWORD")

today = datetime.now()

workout_params = {
    "workout" : {
        "date" : today.strftime("%d/%m/%Y"),
        "time" : time.strftime("%H:%M:%S", time.gmtime()),
        "exercise" : exercise_text.title(),
        "duration" : duration,
        "calories" : calories
    }
}
response = requests.post(url=sheety_endpoint, json=workout_params, auth=HTTPBasicAuth(SHEETY_USERNAME, SHETTY_PASSWORD))
print(response.text)
