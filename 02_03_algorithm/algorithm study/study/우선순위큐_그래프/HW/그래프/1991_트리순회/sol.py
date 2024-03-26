import sys
sys.stdin = open('input.txt')

def preorder(node):
    return

N = int(input()) ## 이진 트리 노드의 개수
tree = {} ## 트리 딕셔너리로 구성
for i in range(N):
    root, left, right = input().split()
    tree[root] = (left,right)
