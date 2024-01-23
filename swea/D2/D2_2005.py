# 파스칼의 삼각형 
# 첫줄1, 둘째줄 부터 왼쪽, 오른쪽 위 숫자 합
# 2차원으로 두고, 이전 행의 이전 열과 이전 행의 현재 열과 더해지면, 파스칼 삼각형이 완성된다.
# 처음과 끝은 1이니까 row를 선언하고, 거기에 1을 주고, 끝낼때 1 append를 한다면 가능
# row개수를 사람이 말해준다. ex) 4면 4줄까지 볼래
# 그럼 N을 처음 range로 돌려준다.
# 그리고 그 행 내에서, 그 이전 행의 -1열, 현재 열의 값을 더한 것을 num으로 보고, num을 row에 추가.

t = int(input())
for T in range(1,t+1):
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
            