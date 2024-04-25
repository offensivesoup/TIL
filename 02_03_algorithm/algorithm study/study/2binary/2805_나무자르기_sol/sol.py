import sys
sys.stdin = open('input.txt')

'''
상근이는 나무 m미터가 필요해, 근데 나무 판매점이 다 망해서
직접 벌목해야함. 
1. 상근이는 절단기의 높이 H를 지정한다.
2. 지정된 높이 위에서 절단기는 나무를 다 잘라버린다.
3. h보다 높으면 잘리고, 낮으면 안잘린다.
4. 15로 지정하면 잘린건 15 안잘린건 그대로
5. 상근이가 가져가는건 잘리고 남은 부분
6. 상근이는 딱 필요한 만큼만 가져가려고한다.
7. 적어도 M미터의 나무를 가져가려면, 절단기에 설정할 높이의 최댓값(최대한 나무를 적게 자르도록)
'''

N, M = map(int,input().split()) # N은 나무의 개수, M은 상근이가 가져갈 나무의 길이
trees = list(map(int,input().split())) # 나무의 높이들 # 상근이는 무조건 필요한 만큼 가져갈 수 있음
start = 0
end = max(trees) # 최대값
result = 0 # 결과물
while start <= end: # 나무의 합이 구해지기 전까지
    cut = (start+end)//2
    sumi = 0 # 나무의 합을 담을 변수
    for tree in trees:
        if tree-cut > 0:
            sumi += tree - cut
    if sumi > M: # 자른게 필요한거 보다 더 많네
        result = cut
        start = cut + 1 # 그럼 더 높게 잘라보아야 함
    elif sumi < M: # 모잘라
        end = cut - 1 # 더 잘게 잘라보자
    else:
        result = cut
        break

print(result)