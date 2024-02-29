import sys
sys.stdin = open('input.txt')

'''
퀴즈 대회 우승자는 , 주어진 숫자판들 중에 두개를 선택하여 , 정해진 횟수만큼 위치를 교환할 수 있다
교환이 끝나면, 가중치만큼 상금이 계산된다
오른쪽 끝에서 1원, 왼쪽으로 갈수록 10배씩(10원, 100원, 1000원 ....) => 가장 큰 숫자를 찾는거임
반드시 횟수만큼의 교환이 이루어져야 하고, 동일한 교환이 반복되어도 된다.
정해진 횟수만큼 교환했을 때, 받을 수 있는 가장 큰 금액
완전탐색으로 결정
'''

def dfs(numbers, cnt):
    global case, N # 돌리기로 한만큼 가져올게
    if cnt > case: # 그 횟수가 최대면 리턴해야해
        return
    answer = '' # 숫자 만들어줄 문자열
    for num in numbers: # 숫자를 만들어줄께
        answer+=num     # numbers의 요소들을 숫자로 합쳤다
    if int(answer) not in result[cnt]: # 그 숫자가 탐색 결과에 없어 ( 돌려본적 없는 숫자임 )
        result[cnt].append(int(answer)) # 그럼 그 순서의 리스트에 추가시킨다
    else: # 있다면
        return # 그만돌려봐도돼
    for i in range(N): # 그 숫자를 돌려본다
        for j in range(i+1,N):
            numbers[i], numbers[j] = numbers[j], numbers[i] # 버블솔트 처럼 바꿔줌
            dfs(numbers, cnt + 1)
            numbers[i], numbers[j] = numbers[j], numbers[i] # 재귀를 나오면 다시 돌려놔야한다

T = int(input())

for test_case in range(1,T+1):
    cnts = 0
    tmp, case = map(int,input().split())
    snumLst = list(str(tmp)) # 문자로 된 숫자 리스트
    result = [[] for _ in range(case+1)] # 돌려본 숫자들을 다 넣을거야 ( 케이스별로 )
    N = len(snumLst) # 돌려볼 길이
    dfs(snumLst, 0)
    print(f'#{test_case} {max(result[-1])}')


