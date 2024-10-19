import os
import requests
from twilio.rest import Client


account_sid = os.environ.get("RAINALERT_ACCOUNT_SID")
auth_token = os.environ.get("RAINALERT_AUTH_TOKEN")


api_key = os.environ.get("OWM_API_KEY")



parameters = {
    "lat": 6.094600,
    "lon": 100.387627,
    "appid": api_key,
    "cnt": 4,

}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
weather_codes = []

for code in data["list"]:
    weather_code = code["weather"][0]["id"]
    weather_codes.append(weather_code)

will_rain = False
for i in weather_codes:
    if i < 700:
        will_rain = True

if will_rain:
    # for sms
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+19202140186',
        body='Its going to rain today. Bring an umbrella',
        to='+250798284094'
    )
    print(message.status)

    # for whatsapp
    # client = Client(account_sid, auth_token)
    #
    # message = client.messages.create(
    #     from_='whatsapp:+14155238886',
    #     body='Its going to rain today. Bring an umbrella',
    #     to='whatsapp:+250798284094'
    # )
