import sys
sys.stdin = open('input.txt')

T = int(input())
for T in range(1,T+1):
    N = int(input())
    triangle = [[1]]
    for i in range(1, N):
        row = [1]
        for j in range(1, i):
            num = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(num)
        row.append(1)
        triangle.append(row)
    print(f'#{T}')
    for tmpLst in triangle:
        for result in tmpLst:
            print(result,end = ' ')
        print()
