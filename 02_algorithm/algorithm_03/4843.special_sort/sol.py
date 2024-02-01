import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    for i in range(N-1,-1,-1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    result = []
    for k in range(0,N,2):
        result.append(max(numbers))
        numbers.remove(max(numbers))
        result.append(min(numbers))
        numbers.remove(min(numbers))

    print(f'#{test_case}',*result[:10])