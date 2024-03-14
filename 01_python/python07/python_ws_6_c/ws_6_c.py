data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
# 데이터를 순회한다.
for dictionary in data:
    print()
    for key in key_list:
        if dictionary.get(key, "uuu") == "uuu":
            dictionary.setdefault(key, "unknown")
            print(f'{key}은/는 {dictionary[key]}입니다.')
        else:
            print(f'{key}은/는 {dictionary[key]}입니다.')

## 강사님 코드
            
for item in data:
    for key in key_list:
        # print(item['name'], key)
        # 순회중인 key로 조회해보았을때, 해당하는 키가 없다면
        if item.get(key) == None:
            item.setdefault(key, "unknown")
        # 모든 상황에 대해서 -> 순회대상 모두에게 
        print(f'{key} 은/는 {item[key]}입니다.')
    print()
