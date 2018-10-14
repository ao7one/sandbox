import requests
import json
import time
import turtle

# Map
screen = turtle.Screen()
screen.setup(1440, 720)
screen.setworldcoordinates(-360,-180,360, 180)
screen.bgpic("world.png")

while True:
    # Query ISS API
    response = requests.get("http://api.open-notify.org/iss-now.json")

    # Printer response
    print(response.status_code)

    # Get content and overhead time in seconds
    result = json.loads(response.content)
    location = result["iss_position"]
    lat = float( location["latitude"] )
    lon = float( location["longitude"] )

    # ISS blimp
    location = turtle.Turtle()
    location.color('red')
    location.penup()
    location.goto( lon, lat)
    location.dot(5)
    location.hideturtle()

    time.sleep(30)