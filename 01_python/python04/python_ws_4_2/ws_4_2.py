import requests
from pprint import pprint as print

dummy_data = []
for page_num in range(1,11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(page_num)
    response = requests.get(API_URL)
    parsed_data = response.json()
    dummy_data.append(parsed_data['name'])
print(dummy_data)