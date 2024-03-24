import sys
sys.stdin = open('input.txt')

def sumi(idx, tops):
    global result

    if tops >= B:
        result = min(result, tops)
        return
    
    if tops > result:
        return
    
    if idx == N-1:
        return
    
    sumi(idx+1, tops + people[idx + 1])
    sumi(idx+1, tops)

T = int(input())
for test_case in range(1,T+1):
    N, B = map(int,input().split()) ## N명의 점원, B의 탑 높이
    people = list(map(int,input().split()))
    ## 리스트를 안만들고 풀려면...
    ## 1명일단 제일 작은애가 서본다
    ## 근데 그게 탑을 넘어? => 그럼 어차피 그게 최소임
    ## 근데 그게 탑을 못넘어 => 그럼 그 애에 나머지 애들을 돌려서 더해줘보아야 한다.
    ## 그럼 두가지 경우의 수로 나누어가야하는 것 같다
    ## 1. 한 애에서 누적합을 해볼 경우랑,
    ## 2. 그 다음 녀석을 바라볼 경우
    
    result = sum(people)
    cnt = 1
    for i in range(N):
        sumi(i-1, 0)
    print(f'#{test_case} {result-B}')