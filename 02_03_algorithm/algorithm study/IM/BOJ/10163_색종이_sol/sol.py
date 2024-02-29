import sys
sys.stdin = open('input.txt')


board = [[0] * 1001 for _ in range(1001)]
N = int(input())
for num in range(1,N+1):
    x, y, w, h = map(int,input().split())
    for row in range(x, x+w):
        board[row][y:y+h] = [num] * h

for num in range(1,N+1):
    sumi = 0
    for b in board:
        sumi += b.count(num)
    print(sumi)

