import requests, json


def model_exists(make,model):
    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{make}?format=json'
    r = json.loads(requests.get(url).text)
    model_names = [model['Model_Name'] for model in r['Results']]
    if model in model_names:
        return True
    else:
        return False


def make_exists(make):
    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/GetAllMakes?format=json'
    r = json.loads(requests.get(url).text)
    make_names = [make['Make_Name'] for make in r['Results']]
    if make.upper() in make_names:
        return True
    else:
        return False