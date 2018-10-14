import requests
import json
import time
import turtle

# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of Horton Heath.
parameters = {"lat": 50.9546, "lon": 1.2951}

# Query ISS API
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Printer response
print(response.status_code)

print("For Alexander")
print(response.content)

# Get content and overhead time in seconds
result = json.loads(response.content)
over = result['response'][1]['risetime']

# Print time in readable format
ctime = time.ctime(over)
print(ctime)

# Output nicely
screen = turtle.Screen()
screen.setup(1440, 720)
screen.setworldcoordinates(-360,-180,360, 180)
screen.bgpic("world.png")

location = turtle.Turtle()
location.penup()
location.color('red')
location.goto(1.2951,50.9546)
location.dot(5)

# Print date
style = ('Arial', 14, 'bold')
location.write(ctime, font=style)


time.sleep(10)