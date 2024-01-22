# 아래 함수를 수정하시오.
def sort_tuple(user_tuple):
    new_tuple = ()
    new_lst   = []
    for i in user_tuple:
        new_lst.append(i)
        new_lst.sort()
    for data in new_lst:
        new_tuple += (data,)
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
