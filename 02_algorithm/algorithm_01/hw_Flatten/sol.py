import sys
sys.stdin = open('input.txt')
'''
가장 높은 곳에거 가장 낮은곳으로 옮겨야 한다.
배열의 max 값에서, min 값으로 상자를 옮기는 것
이동횟수와 배열을 입력 받아, 최고와 최저점의 차이를 판가름 한다.
'''
# T = 10 # 테스트 케이스 10개
# for test_case in range(1,T+1):
#     dumps = int(input()) # 덤프 횟수
#     boxes = list(map(int,input().split())) # 박스 배열
#     result = []
#     for dump in range(dumps): # 덤프 횟수만큼의 반복 시행
#         # 덤프 할때마다 최고점의 박스와, 최저점의 박스를 알아야 한다.
#         # 최고점의 박스에서, 최저점의 박스로 옮기는 것
#         # 최고점 높이 -1, 최저점 높이 +1
#         boxes[boxes.index(max(boxes))] -= 1
#         boxes[boxes.index(min(boxes))] += 1
#     print(f'#{test_case} {max(boxes)-min(boxes)}')

for tc in range(1,11):
    dump = int(input())
    boxes = list(map(int,input().split()))

    h_cnt = [0] * 101
    min_v = 101
    max_v = 0

    for i in range(100):
        h_cnt[boxes[i]] += 1

        if boxes[i] > max_v:
            max_v = boxes[i]
        if boxes[i] < min_v:
            min_v = boxes[i]

    while dump > 0 and max_v - min_v > 1:
        h_cnt[min_v] -= 1
        h_cnt[max_v] -= 1
        h_cnt[min_v+1] += 1
        h_cnt[max_v-1] += 1

        if h_cnt[min_v] == 0:
            min_v += 1
        if h_cnt[max_v] == 0:
            max_v -= 1
        dump -= 1
    result = max_v - min_v
    print(result)

