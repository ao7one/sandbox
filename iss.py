import requests
import json
import time
import turtle

# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of Horton Heath.
parameters = {"lat": 50.95, "lon": 1.29}

# Query ISS API
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Printer response
print(response.status_code)

# Get content and overhead time in seconds
result = json.loads(response.content)
over = result['response'][1]['risetime']

# Print time in readable format
print(time.ctime(over))

# Output nicely
screen = turtle.Screen()
screen.setup(720, 360)
screen.bgpic("world.jpg")
