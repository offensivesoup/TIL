import sys
sys.stdin = open('input.txt')


'''
수열의 길이로 경우의 수를 나눈다.
수열이 1개면 => A (무수히 많다)
수열이 2개면 => 같으면 그 숫자, 다르면 무수히 많음
수열이 3개 이상이면 => 규칙성을 찾아야 한다. 최대 50길이까지 수열
수들의 절대값이 100 보다 작대
그럼 어쨋든 순열의 수들은 100을 넘지 않아야함.
그럼 완전탐색으로 나누어본다면
'''

n = int(input())
arr = list(map(int,input().split()))
result = []
if n == 1:
    print('A')
elif n == 2:
    if len(set(arr)) == 1:
        print(arr[0])
    else:
        print('A')
else:
    for i in range(-200,201):
        cnt = 2
        num = arr[1] - (arr[0] * i)
        while arr[cnt] - (arr[cnt-1] * i) == num:
            if cnt == n - 1:
                result.append(arr[n-1] * i + num)
                break
            cnt += 1
    if len(set(result)) == 1:
        print(result[0])
    elif len(set(result)) >= 2:
        print('A')
    else:
        print('B')