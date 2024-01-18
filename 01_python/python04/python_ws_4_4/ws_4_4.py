import requests
from pprint import pprint as print

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]
dummy_data = []
user_list = {}
censored_user_list = {}

def create_user():
    # 데이터 가져옴
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
    # 더미 데이터에서 꺼내서 user_list 만듦
    for user in dummy_data:
        user_list[user['company']] = [user['name']]
        if censorship(user):
            censored_user_list[user['company']] = [user['name']]
    print(censored_user_list)
    # 그거 밑에 함수에 넣음 print 됌.
    # 이후 True면 censored_user_list에 넣음.
    # True, False 반환해야 한다.
    # if censorship(user_list):
    #     censored_user_list[user['company']] = [user['name']]    
def censorship(user_info):
    if user_info['company'] in black_list:
        print(f'{user_info["company"]}소속의{user_info["name"]}은/는 등록할 수 없습니다.')            
        return False
    else:
        print('이상 없습니다.')
        return True



create_user()