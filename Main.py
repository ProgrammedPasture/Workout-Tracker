import requests

App_ID = "f73e8e66"
API_KEY = "4aaedaabbbf935cacd8776e9c21fd8c8"

Gender = "Male"
Weight_lbs = 230
Height_Cm = 72
age = 28

workout_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("What exercise did you perform?")

headers = {
    "x-app-id" : App_ID,
    "x-api-key" : API_KEY,
}

params = {
    "query" : exercise_text,
    "gender" : Gender,
    "weight" : Weight_lbs,
    "height" : Height_Cm,
    "age" : age,
}

response  = requests.post(workout_endpoint, headers=headers, json=params)
data = response.json()
print(data)