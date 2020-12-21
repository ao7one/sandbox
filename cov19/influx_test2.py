from influxdb import InfluxDBClient
import datetime
import random

client = InfluxDBClient(host='192.168.1.150', port=8086, username='telegraf', password='hakase-ndlr')

# remove test db and create each run
client.drop_database('pytest')
client.create_database('pytest')
client.switch_database('pytest')
response = client.get_list_database()
print(response)

now = datetime.datetime.utcnow()

print("now    ", now.isoformat('T'))

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

# create sample data
for x in range(6):
    now = now - datetime.timedelta(days=1)
    print("now -", x+1, now.isoformat('T'))
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

# write db
client.write_points(json_body)