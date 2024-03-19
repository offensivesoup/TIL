# # 백트래킹
# # 완전탐색 + 가지치기
# # 가능성이 없는(볼 필요가 없는) 경우의 수를 제거하는 기법

# ## 중복된 순열
# ## 재귀 함수는 특정 시점으로 돌아오는게 핵심!
# ## 재귀 팁
# ## 파라미터 : 먼저 작성 X
# ## 구조를 먼저 잡으면 자연스럽게 필요한 변수들이 보인다.
# ## 조합을 구해보자
# ## 숫자를 한번만 사용해라

# def make_arr(level):
#     # 기저 조건
#     # 이 문제에서는 3개를 뽑았을 때 까지 반복
#     if level == 3:
#         return
#     # 들어가기 전
#     # 다음 재귀 호출
#     # - 다음에 갈 수 있는 곳들은 어디인가?
#     # - 이 문제에서는 1, 2, 3 세 가지 경우의 수가 존재한다.
#     path[level] = 1
#     make_arr(level + 1)
#     path[level] = 2
#     make_arr(level + 1)
#     path[level] = 3
#     make_arr(level + 1)
#     ## 갈수 있는 후보군이라면?
#     for i in range(len(arr)):
#         ## 여기는 못가!(가지치기)
#         ## 백트래킹 코드 팁
#         ## 갈 수 없는 경우를 활용하는 것

#         if arr[i] in path:
#             continue
#         path[level] = arr[i]
#         make_arr(level + 1)

# arr = [i for i in range(1,4)]
# path = [0] * 3
# make_arr(0)


## 트리

arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

## 정석 개발 버전
class Treenode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None
    
    def insert(self,child):
        # 왼쪽에 삽입시도
        if not self.left:
            self.left = child
            return
        
        # 오른쪽에 삽입시도
        if not self.right:
            self.right = child
            return
        
        # 삽입 실패
        return
    
    def inorder(self):
        if self != None:
            if self.left:
                self.left.inorder()
        
            print(self.value, end = ' ')

            if self.right:
                self.right.inorder()

# 이진 트리 만들기
## 1. 노드들을 생성    
# nodes = [Treenode(i) for i in  range(0, 14)]

# ## 2. 간선 연결
# for i in range(0, len(arr), 2):
#     parent_node = arr[i]
#     childe_node = arr[i+1]
#     nodes[parent_node].insert(nodes[childe_node])



## 코테에서는
nodes = [[] for _ in range(14)]
for i in range(0, len(arr), 2):
    parent_node = arr[i]
    child_node  = arr[i+1]
    nodes[parent_node].append(child_node)

## 자식이 없다는 걸 표시하기 위해서 None
for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)

print(nodes)

def inorder(nodeNum):
    # 갈수 없다면 return
    if nodeNum == None:
        return
    # 왼쪽으로 갈 수 있따면 진행
    inorder(nodes[nodeNum][0])
    print(nodeNum, end = ' ')
    inorder(nodes[nodeNum][1])

inorder(1)

