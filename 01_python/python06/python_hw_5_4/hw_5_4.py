# 아래 함수를 수정하시오.
def find_min_max(user_input):
    maxi = max(user_input)
    mini = min(user_input)
    answer = (mini, maxi)
    return answer


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
