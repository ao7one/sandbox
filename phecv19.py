from uk_covid19 import Cov19API

england_only = [
    'areaType=nation',
    'areaName=England'
]

cases_and_deaths = {
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "newAdmissions": "newAdmissions",
    "cumAdmissions": "cumAdmissions",
    "covidOccupiedMVBeds": "covidOccupiedMVBeds",
    "hospitalCases": "hospitalCases",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeathsByDeathDate": "newDeathsByDeathDate",
    "cumDeathsByDeathDate": "cumDeathsByDeathDate"
}

api = Cov19API(filters=england_only, structure=cases_and_deaths)

data = api.get_json()

print(data)