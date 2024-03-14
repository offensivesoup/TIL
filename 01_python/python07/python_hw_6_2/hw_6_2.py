# 아래 함수를 수정하시오.
def remove_duplicates_to_set(Lst):
    answer = set(Lst)
    return answer

# 로직으로 풀어보자
# 가정 : arr 1~9까지의 정수만 요소로 삽입된다면.
def remove_duplicates_to_set(arr):
    # 기본 dict
    count_dict = {1 : 0, 2 : 0, 3 : 0, 4 : 0}
    # dict_comprehension
    count_dict = {i : 0 for i in range(1,10)}
    for num in arr:
        count_dict[num] += 1
    # 모든 출현횟수 기록해둔 dict를 순회해서
        # value가 1인 key만 모아서 새 list로 반환
    result = [key for key, item in count_dict.items() if item >= 1]
    return set(result)
    # 중복이 없다.
    # 배열의 모든 요소를 순회한다.
    # 이때, 순회 대상이, 이전에 한번도 나온적이 없다.
        # 요소를 중심으로, 해당 요소가 몇번 나왔는지 셀 수 있어야 함.
        # 1이 1번 나왔으면 1 = 1
        # 2가 3번 나왔으면 2 = 3
        # dict = {1: 1, 2: 3}

# 새로운 코드
def remove_duplicates_to_set(arr):
    count_list = [0 for i in range(10)]
    for index in arr:
        count_list[index] += 1
    result = [num for num in range(len(count_list)) if count_list[num] >= 1]
    return result
    
    


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
