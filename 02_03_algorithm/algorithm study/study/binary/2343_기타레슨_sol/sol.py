import sys
sys.stdin = open('input.txt')

'''
강토가 기타 동영상을 판매한다.
조건
1. 블루레이의 순서가 바뀌면 안된다
2. 블루레이를 가급적 줄인다 -> 최소값
3. M개의 블루레이는 모두 같은 크기여야 한다. => sumi
4. 가능한 블루레이의 최소 크기
생각의 흐름
어쨋든, 최소 크기를 알아내야하는데, 최대 크기는 무엇인가? 다 더해주는거
end = sum(배열)
start = max(배열) => 왜? 길이를 최소로하려고 하기 때문에 제일 긴 강의가 들어가야하지 않을까
예제를 입력햇을때 9랑 45가 된다
그럼 처음 mid 27
일단, 강의의 길이를 27로 만들어보는거임
1을 뽑는다 27 로 만든다 26이 필요하다
2를 뽑는다 27 로 만든다 25가 필요하다
# 총 만들어진 개수가 cnt같아야 하고
# 그럼 더해준다.
다시 돌려본다
# 아니면 더 줄여본다 -> 더 작게 더해줘야 하므로
'''

N, M = map(int,input().split())
bluerays = list(map(int,input().split()))
start = max(bluerays)
end   = sum(bluerays)
result = 0
while start <= end:
    mid = (start+end)//2 # 만들어져야하는 블루레이의 개수
    sumi = 0
    cnt  = 1
    for cd in bluerays:
        if sumi + cd > mid: # 강의 길이를 다 채웠네
            cnt += 1 # 그럼 찍엇다고 표시해주고
            sumi = 0 # 블루레이의 길이를 최소화
        sumi += cd
    if cnt <= M: # 그렇게 만들어진 블루레이 개수가 같네?
        # 그럼 후보군으로 들어갈 수 있다
        # 강의 길이를 더 줄여볼수도 있다
        result = mid
        end = mid - 1
    else: # 더 크게 찍어보아야해
        start = mid + 1
print(result)
