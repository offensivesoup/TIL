# 아래 함수를 수정하시오.
def even_elements(lst):
    odLst = []
    deli  = -1
    answer = []
    for data in lst:
        if data % 2 == 1:
            odLst.append(data)
    for m in odLst:
        deli -= 1
        lst.pop(deli)
    answer.extend(lst)
    return answer

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)