import sys
sys.stdin = open('sample_input.txt')
print('assad')

T = int(sys.stdin.readline())

for test_case in range(1,T+1):
    N = int(sys.stdin.readline())
    user_list = list(map(int, sys.stdin.readline().split()))
    tmpMax = user_list[0]
    tmpMin = user_list[0]
    for i in range(1,N):
        if tmpMax < user_list[i]:
            tmpMax = user_list[i]
        if tmpMin > user_list[i]:
            tmpMin = user_list[i]
    result = tmpMax - tmpMin
    print(f'#{test_case} {result}')