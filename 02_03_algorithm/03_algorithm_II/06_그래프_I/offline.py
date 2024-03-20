def make_set(x):
    parent = [i for i in range(x)] # 노드 번호 수 만큼 parent 리스트 생성
    rank   = [0] * x # 첫 make_set 시행시, 본인을 루트로 하는 노드만 있으므로
    # parent 정보와 rank 정보를 함께 반환
    return parent, rank

parent, rank = make_set(7)

def find_set(x):
    # 자기자신을 부모로 하는 루트 노드를 찾을때 까지 탐색
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x,y):
    root_x = find_set(x)
    root_y = find_set(y)
    # 두 집단의 루트 노드가 서로 다르면 합치는 과정
    if root_x != root_y:
        # 합칠 때, 기준은 rank를 기준으로 작업을 한다.
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

union(1, 3)
print(parent)
print(rank)
union(2, 3)
print(parent)
print(rank)
union(5, 6)
print(parent)
print(rank)
union(6, 3)
print(parent)
print(rank)

