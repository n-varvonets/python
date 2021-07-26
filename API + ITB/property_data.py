import requests

api_url = 'https://clientapi.immotoolbox.com/api/'
token = '61fcb9196054d494aa21719e3ffd7dd6'

def get_properties_data():
    page = 1
    lst_properties = []
    while page:
        params = {
            "page": page,
            "token": token,
        }
        res = requests.get(f"{api_url}properties/", params).json()
        lst_properties.extend(res['hydra:member'])
        if len(res['hydra:member']) > 1:
            page = page + 1
            continue
        break
    return lst_properties

properties_data = get_properties_data()

name = [i['reference'] for i in properties_data]
n = 1
d = {}
for i in name:
    d[n] = i
    n += 1

print(d)

"""Now that we have received complete data for the entire list of properties,
we can choose from this list what we need.... For example get tittle of property"""
tittle_properties = [i['texts']['en']['title'] for i in properties_data]




