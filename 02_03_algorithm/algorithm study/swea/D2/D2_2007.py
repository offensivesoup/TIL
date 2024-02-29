# 문자열의 패턴 몇갠지 구하기
# 문자열의 길이가 30이다.
# set으로 중복을 없애기에는, 하나의 문자열에도 중복되는 문자가 있을 수 있다.
# 그럼 두가지로 상황을 나누어서 조건을 주면 되지 않을까
# 1. enumerate 로 나누어, 각 인덱스를 키값으로, 값을 벨류로 갖는 딕셔너리를 만든다.



T = int(input())
cleaning = []
result   = {}
for i in range(1, T+1):
    user_input = input()
for user in user_input:
    cleaning.append(user)

for idx, num in enumerate(cleaning):
    result[idx] = num