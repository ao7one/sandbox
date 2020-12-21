import requests
import json
import time
import turtle

# Sleep...
sleep = 30

# Map
screen = turtle.Screen()
screen.title("ISS Tracker")
screen.setup(1600, 800)
screen.setworldcoordinates(-180,-90, 180, 90)
screen.bgpic("hd_world_1600.png")

# Set time stamp
time_now = time.ctime()

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
    location.pendown()
    location.penup()
    location.hideturtle()

    # Print date
    location.goto(85,-85)
    style = ('Arial', 12, 'bold')
    location.color('white')
    location.write(time_now, font=style)

    # Update time stamp
    time_now = time.ctime()
    screen.title("ISS Tracker: " + time_now)

    # Print date
    location.color('red')
    location.write(time_now, font=style)

    time.sleep(sleep)