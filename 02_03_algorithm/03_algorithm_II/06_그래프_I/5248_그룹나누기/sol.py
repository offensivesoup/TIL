import sys
sys.stdin = open('input.txt')

'''
5 3
1 2 2 3 4 5
1 2
1 2 findset을해 그럼 1, 2가 나오지 아직 누구랑 하기로 안함
그리고 rank에는 (깊이 : 몇명이랑 하는데?)
핵심 : 내가 누구랑 같이 조를 하고 싶은데, 걔 누구랑 조임
'''

def find_set(x): # 내가 벌써 누구랑 조를 하기로 했네? 하는걸 찾아줌
    if x != parents[x]: # 그니까 나는 벌써 누구랑 하기로 했어
        parents[x] = find_set(parents[x]) # 누구랑 하기로 했는데?
    return parents[x] # 결국 누구랑하는지 보여준다

def union(x, y):
    root_x = find_set(x) # 1, 2->1, 4
    root_y = find_set(y) # 2, 3, 5
    if rank[root_x] >= rank[root_y]: # 처음엔 같네?
        parents[root_y] = root_x # 어차피 부모의 2가 1로 바뀌는거임 조장이 결정되어버렷어
        if rank[root_x] == rank[root_y]: # 근데 둘이 하기로한 애들도 같음
            rank[root_y] += 1 # 그럼 그냥 한명 추가된거임
    else: # 근데 아니 x 조가 y조보다 작아, 약해 그럼 그냥 인수되어라
        parents[root_x] = root_y # 그럼 그냥 y가 x로 들어가라~


T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    paper = list(map(int,input().split()))
    parents  = [x for x in range(N+1)]
    rank     = [0 for _ in range(N+1)]
    print('초기 부모', parents)
    print('초기 순위', rank)
    cnt   = N - len(set(paper)) # 아무도 지목받지 못한 사람은 단독으로 조 구성
    for i in range(0,2*M-1,2):
        left, right = paper[i], paper[i+1]
        union(left,right)
        print('유니온 하고 부모',parents)
        print('유니온 하고 순위',rank)
        # 왼쪽이 지목당하고 오른쪽이 지목한 사람 순이라고 했을때,
        # 지목당한 사람이 지목한 사람과 같은 조다

    for j in range(0,N+1):
        find_set(j)
        print('파인드셋',parents)

    print(parents)

    print(f'#{tc} {len(set(parents)) - 1}')
