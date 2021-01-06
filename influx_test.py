from influxdb import InfluxDBClient

#client = InfluxDBClient(host='192.168.1.150', port=8086, username='telegraf', password='hakase-ndlr', ssl=True, verify_ssl=True)
client = InfluxDBClient(host='192.168.1.150', port=8086, username='telegraf', password='hakase-ndlr')

response = client.get_list_database()
print(response)

json_body = [
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-28T8:01:00Z",
        "fields": {
            "duration": 127
        }
    },
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-29T8:04:00Z",
        "fields": {
            "duration": 132
        }
    },
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },

        "fields": {
            "duration": 129
        }
    }
]

client.switch_database('pytest')

client.write_points(json_body)