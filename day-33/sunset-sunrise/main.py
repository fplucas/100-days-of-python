from datetime import datetime
import requests
import smtplib
import time

MY_EMAIL = "example@example.com"
MY_PASSWORD = "example"
MY_SMTP_SERVER = "smtp.example.com"
MY_LAT = 53.412910
MY_LONG = -8.243890


def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    lat_offset = MY_LAT - iss_latitude
    long_offset = MY_LONG - iss_longitude
    return (-5 <= lat_offset <= 5 and -5 <= long_offset <= 5)


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    return time_now.hour >= sunset


while True:
    time.sleep(60)
    if (is_iss_overhead() and is_night()):
        connection = smtplib.SMTP(MY_SMTP_SERVER)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr="MY_EMAIL",
            to_addrs="MY_EMAIL",
            msg="Subject: Look Up\n\nThe ISS is above you in the sky."
        )
