import sys
sys.stdin = open('input.txt')
'''
1. 4등분하고
2. 방문한다
그럼 행과 열에 따라서, 방문할 박스를 미리 더해주는 것이 가능할듯
예를 들어 N이 3으로 주어져
그럼 8 * 8 박스를 4*4 박스 4개로 나누잖아?
그럼 인덱스는 0부터 7까지가 되는데
예를 들어 r이 4이상면 아래 박스니까
위 두박스는 볼 필요가 없고, 찾을 cnt에 그 두박스의 크기만큼 더해줄 수 있어
또 c도 4이상이면 마찬가지로
위 두박스 + 왼쪽박스까지 볼 필요가 없음
그럼 48을 더한 상태로 오른쪽 아래 박스만 봐주면 된다.
이말이지
그럼 1. 두 조건으로 나누어준다
행과 열의 N의 절반과의 대소비교
그리고 2^N-1승에서 만들어진 박스를 가지고 행과 열이 몇번째인지 찾아본다
여기서 찾을 행과 열은 상황에 따라서, 경우의 수를 나누어주는 것이 필요할거같애
그 다음 그 작아진 박스를 다시 4분면으로 나누기 위해 만약 2분면 3분면 4분면이라면
해당 행과 열의 크기를 다시 그 반만큼 줄여주면, 그 줄어든 박스에 적용할 수 있다
다시 나누어서, 똑같이 반복,
그럼 결국 2*2 박스가 만들어지고
마지막으로 세어지는 숫자가 나타나게 될것이다.
'''

# 입력을 받는다
N, r, c = map(int,input().split())
# 위쪽 두 박스중 하나야
cnt = 0

while N > 0:
    N -= 1 # 일단 절반으로 나눌거임(2의 N승을 2의 N-1승으로 나누는거지)
    half = 2**N # 절반지점
    box  = half ** 2 # 한 박스의 사이즈 (정사각형이니까 half * half가 된다)
    ## 왼쪽 위 박스
    ## 그냥 넘어가야해
    if r < half and c < half:
        pass
    ## 오른쪽 위 박스
    ## 한박스는 이미 z가 지나왔어
    elif r < half and c >= half:
        cnt += box # 그 한박스 더해줌
        c -= half
    ## 왼쪽 아래 박스
    elif r >= half and c < half:
        cnt += 2 * box # 이건 두박스
        r -= half
    elif r >= half and c >= half:
        cnt += 3 * box # 이건 세박스
        r -= half
        c -= half
print(cnt)

