# 아래 함수를 수정하시오.
def remove_duplicates(user_list):
    new_lst = []
    for data in user_list:
        if data not in new_lst:
            new_lst.append(data)
    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
