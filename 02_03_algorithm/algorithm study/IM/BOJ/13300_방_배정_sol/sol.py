import sys
sys.stdin = open('input.txt')

'''
남남, 여여끼리 방배정을 해야한다. , 같은 학년끼리 방배정
한방의 최대 인원 수 K가 주어졌을 때, 모든 학생을 배정하기 위한 최소개수
'''

N, K = map(int,input().split()) # 학생수, 방마다 최대 인원수
room = {} # 방마다 한명을 배정한다고 생각했을 때의 방 개수
information = [tuple(map(int,input().split())) for _ in range(N)]
for i in range(N):
    if information[i] not in room:
        room.setdefault(information[i], 1)
    else:
        room[information[i]] += 1

cnt = 0
for student in room.values():
    if student <= K:
        cnt += 1
    else:
        if student % K == 0:
            cnt += (student//K)
        else:
            cnt += (student // K) + 1

print(cnt)






