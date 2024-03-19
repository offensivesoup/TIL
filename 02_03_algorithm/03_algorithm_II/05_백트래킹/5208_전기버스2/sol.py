import sys
sys.stdin = open('input.txt')

'''
충전지를 교환하는 방식의 전기버스 => 정류장에 충전지가 있고, 충전지마다 얼마나 갈수 있는지 정해져있다
충전지가 방전되기 전에, 교체하고 운행하는데, 교체하는 시간을 줄이려면 최소한의 횟수로 도착
=> 얼마가 최소인가를 출력 ( 출발지는 제외 )

1. 횟수를 세는 것이 중요하다
2. 배터리는 교체되는 것이다.

'''
#
def backtracking(now, total, battery, cnt):
    ## now = 현재 위치
    ## total = 도착지점
    ## battery = 거기서 충전한 배터리
    ## cnt = 충전횟수
    global mini
    if now + battery >= total - 1:
        if mini > cnt:
            mini = cnt
            return
    elif cnt >= mini:
        return
    else:
        for ba in range(1,battery+1):
            backtracking(now + ba, total, stops[now:][ba], cnt + 1)

T = int(input())

for tc in range(1,T+1):
    user_input = list(map(int,input().split())) # [5 2 3 1 1]
    N      = user_input[0] # 정류장이 몇개인지 (어디가 종점인지) 5
    first_battery = user_input[1] # 처음 배터리
    stops = user_input[1:]
    mini = 1e9
    backtracking(0, N, first_battery, 0)
    print(f'#{tc} {mini}')