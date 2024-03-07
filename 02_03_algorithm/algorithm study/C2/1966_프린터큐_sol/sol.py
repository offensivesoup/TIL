import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split()) # N : 문서의 개수, 몇번째로 인쇄되었는지 궁금한 문서가 현재 어디에 있는지 M
    user_input = list(map(int,input().split())) # 문서의 중요도가 주어진다
    papers = []
    for idx, paper in enumerate(user_input):
        papers.append((paper,idx))
    cnt = 0
    now = 0
    while papers:
        if N == 1:
            print(1)
            break
        if papers[0][0] == max(user_input): # 젤 앞쪽에 있는게 젤 중요한 문서야
            now = papers.pop(0) # 그걸 뺄거임
            cnt += 1 # 뺏다고 세줄거야
            user_input.remove(now[0])
            if now[1] == M: # 빼준 문서가 찾던 문서면
                print(cnt) # 그때 몇번째인지 출력하고
                break # 멈춘다
        else: # 젤중요한 문서가 아니네?
            now = papers.pop(0)
            papers.append(now) # 맨 뒤로 넣어줄게


