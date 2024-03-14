# 아래 함수를 수정하시오.
def get_value_from_dict(user_dict, user_key):
    answer = user_dict.get(user_key)
    return answer


my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice
