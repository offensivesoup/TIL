## 간단한 소인수분해
# N = 2**a * 3**b * 5**c * 7**d * 11**e
# N 을 알면, abcde를 알 수 있을까?

T = int(input())
resultLst = []
numLst = [2,3,5,7,11]
for i in range(1,T+1):
    N = int(input())
    result = []
    for num in numLst:
        resultNum = 0
        while True:
            if N % num == 0:
                resultNum += 1
                N //= num
            else:
                break
        result.append(resultNum)
    if i > 1:
        print()
    print(f'#{i}', end = ' ')
    for answer in result:
        print(answer, end = ' ')

            