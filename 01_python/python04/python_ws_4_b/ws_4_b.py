food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

for category in food_list:
    if category['이름'] == '토마토':
        category['종류'] = '과일'
    elif category['이름'] == '자장면':
        print('자장면엔 고춧가루지')
    print(f'{category["이름"]} 은/는 {category["종류"]} (이)다.')
    
print(food_list)