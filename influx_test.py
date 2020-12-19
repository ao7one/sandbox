from influxdb import InfluxDBClient

client = InfluxDBClient(host='192.168.1.150', port=8086)

response = client.get_list_database()

print(response)