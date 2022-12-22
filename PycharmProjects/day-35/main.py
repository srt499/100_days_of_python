import requests
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACea0544007d5b68ede2665c8a4f3c5c7b'
auth_token = '3a16d2b4ebbf26e6658b864cb25c8b45'


parameters = {
    'appid': "abbd30f0c706dad224b7ae943beea769",
    'lat': 45.22,
    'lon': -122.45,
}
response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

will_rain = False

weather_slice = data["list"][:6]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]['id']
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Looks like it's gunna rain today. Pack an ☂." ,
        from_='+12069446269',
        to='+15038878052'
    )
    print(message.status)

