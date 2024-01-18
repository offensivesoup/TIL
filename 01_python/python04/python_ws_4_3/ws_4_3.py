import requests
from pprint import pprint as print

dummy_data = []
for page_num in range(1,11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(page_num)
    user_dict = {}
    response = requests.get(API_URL)
    parsed_data = response.json()
    company = parsed_data['company']['name']
    name = parsed_data['name'] 
    lat  = parsed_data['address']['geo']['lat']
    lng  = parsed_data['address']['geo']['lng']
    if -80 < float(lat) < 80 and - 80 < float(lng) < 80:
        user_dict['company'] = company
        user_dict['name']    = name
        user_dict['lat'] = lat
        user_dict['lng'] = lng
    if len(user_dict) > 0:
        dummy_data.append(user_dict)
print(dummy_data)