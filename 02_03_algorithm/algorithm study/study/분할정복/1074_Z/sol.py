import sys
sys.stdin = open('input.txt')
'''
4등분하고
방문한다
그럼 행과 열에 따라서, 방문할 박스를 미리 찾아주는 정도는 가능할듯
예를 들어 N이 3으로 주어져
그럼 8 * 8 박스를 4*4 박스 4개로 나누잖아?
그럼 인덱스는 0부터 7까지가 되는데
예를 들어 r이 3초과면
위 두박스는 볼 필요가 없고, 찾을 cnt에 그 두박스의 크기만큼 더해줄 수 있어
또 c도 3초과면 마찬가지로
위 두박스 + 왼쪽박스까지 볼 필요가 없음
그럼 48을 더한 상태로 오른쪽 아래 박스만 봐주면 된다.
이말이지
그럼 1. 두 조건으로 나누어준다
행과 열의 N의 절반과의 대소비교
그리고 2^N-1승에서 만들어진 박스를 가지고 행과 열이 몇번째인지 찾아본다
여기서 찾을 행과 열은 상황에 따라서, 경우의 수를 나누어주는 것이 필요할거같애
'''
# 입력을 받는다
N, r, c = map(int,input().split())
# 위쪽 두 박스중 하나야
cnt = 0
half = (2**(N-1))
if r < half:
    ## 왼쪽 박스야
    if c < half:
        ## 그럼 어차피 0부터 새야해
        pass
    ## 오른쪽 박스네? 그럼 한박스 건너뛰면 돼
    else:
        cnt = half**2
        ## c는 왼쪽박스인 척 해야해
        c -= half
# 아래쪽 박스야
else:
    # 왼쪽 박스야 => 두박스 건너뛰기
    r -= half
    if c < half:
        cnt = 2 * (half**2)
    # 오른쪽 박스야 => 세박스 건너뛰기
    else:
        cnt = 3 * (half**2)
        c -= half

breaker = True
for i in range(0,half):
    for j in range(0,half):
        if i == r:
            if j == c:
                breaker = False
                break
        cnt += 1
    if not breaker:
        break

print(cnt)