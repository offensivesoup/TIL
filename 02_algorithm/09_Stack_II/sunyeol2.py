'''
K = 탐색 대상이 된 원소 번호
result = 최종 결과값 (부분집합을 구하기 위함 type(list))
cnt = 부분집합의 합이 몇이냐
'''

def powerset(K, result, cnt):
    global count
    count += 1
    # 언제까지 조사 할 것이냐
    if cnt  > 10: #  한번이라도 누적합이 10을 넘어섰다면, 앞으로는 조사하는 의미 없음
        return # 돌아가
    # K번째 원소를 사용한 경우, 사용하지 않은 경우
    if K == N: # 모든 원소에 대해 조사를 마쳤다면.
        if cnt == 10: # 다음 조건 : 부분집합의 합이 10인 경우만
            print(result)
        return
    else: # 아직 조사해야하는 원소가 남아있는 경우라면
        # K번째 원소를 사용한 경우
        powerset(K+1, result + [arr[K]], cnt + arr[K])
        # K번째 원소를 사용하지 않은 경우
        powerset(K+1, result, cnt)

N = 10 # 원소의 개수가 N개
arr = list(range(1,11))
count = 0
print(arr)

# 0번 요소부터 조사, 공집합, 누적합 0
powerset(0, [], 0)
print(arr)

'''
from itertools import permutations
a = range(1,5)
b = list(permutations(a,3))
print(b)
=> 3개로 만들어진 순열 다나옴 ㄷ ㄷ
'''