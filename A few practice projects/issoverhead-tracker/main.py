import os
import requests
from datetime import datetime
import smtplib
import time

my_email = 'jerryagbaje@gmail.com'
password = os.getenv("ISSPASSWORD")
recipient = 'jerryagbajetest@yahoo.com'

MY_LAT = 30.104429  # Your latitude
MY_LONG = -1.970579  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def iss_close():
    if (25 <= iss_latitude <= 35) and (iss_longitude >= MY_LONG - 5 and iss_latitude <= MY_LONG + 5):
        return True
    else:
        return False


close = iss_close()

while True:
    time.sleep(60)
    if close:
        if hour >= sunset or hour <= sunrise:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=recipient, msg='Subject:Iss Overhead\n\nLook Up !')
