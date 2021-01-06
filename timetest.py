import datetime
import random

# "time": "2018-03-30T8:02:00Z",
# current date and time

now = datetime.datetime.utcnow()

print("now    =", now.isoformat('T'))

json_body = [
    {
        "measurement": "cases",
        "time": now.isoformat('T'),
        "tags": {
            "region": "England",
            "area" : "Nation"
        },
        "fields": {
            "daily": 22775,
            "cumulative": 1711738
        }
    }
]

for x in range(6):
    now = now - datetime.timedelta(days=1)
    print("now -1 =", now.isoformat('T'))
    daily = 22775 + random.randint(-3000,3000)
    cumulative = 1711738 + daily
    json_body = json_body + [
        {
            "measurement": "cases",
            "time": now.isoformat('T'),
            "tags": {
                "region": "England",
                "area" : "Nation"
            },
            "fields": {
                "daily": daily,
                "cumulative": cumulative
            }
        }
    ]

print(json_body)