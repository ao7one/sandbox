import requests

# Query ISS API
response = requests.get("http://api.open-notify.org/iss-now.json")

# Printer response
print(response.status_code)