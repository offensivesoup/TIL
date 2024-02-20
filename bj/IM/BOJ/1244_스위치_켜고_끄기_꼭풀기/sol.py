import sys
sys.stdin = open('input.txt')
'''1은 켜진거, 0은 꺼진거

남학생 : 스위치 번호가, 자기가 받은 수의 배수라면? => 그 스위치의 상태를 바꾼다.
여학생 : 1. 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이고
        2. 가장 많은 스위치를 포함하는 구간을 찾고, 그 구간의 스위치 모두를 바꾼다
        3. 구간의 개수는 항상 홀수이다.
        
        

'''


N = int(input()) # 스위치의 개수
switchs = list(map(int,input().split())) # 스위치
M = int(input()) # 학생수
for _ in range(M):
    student, num = map(int,input().split()) # 남1 여2 / 받은 스위치 개수
    if student == 1: # 남학생이면
        for idx in range(1,len(switchs)): # 스위치를 한번씩 순회돌려볼께
            if idx % num == 0: # 만약 그 스위치가 남학생 번호의 배수라면
                if switchs[idx-1]: #스위치가 켜져있어
                    switchs[idx-1] = 0
                else: # 꺼져있음
                    switchs[idx-1] = 1 # 키는것임
    else: #여학생이면
        cnt = 1 # 여학생의 좌우대칭을 확인할 변수
        if switchs[num-1]: # 일단 자기꺼 켜져있으면
            switchs[num-1] = 0 # 끔
        else: # 꺼져있으면
            switchs[num+1] = 1 # 켠다
        while check:  # 그리고 순회돌려봐야함
            if num-1-cnt >=0 and num-1+cnt<N:
                if switchs[num-1+cnt] == switchs[num-1-cnt]: # 자기가 뽑은 앞에거 뒤에거가 같음
                    if switchs[num-1+cnt]: # 양쪽 거가 켜져있음
                        switchs[num - 1 + cnt] , switchs[num-1-cnt] = 0, 0 # 둘다 끌거임
                    else: # 아니면
                        switchs[num - 1 + cnt], switchs[num - 1 - cnt] = 1, 1 # 둘다 킬거임
                    cnt += 1 # 그리고 다음거 볼거임
                else: # 양쪽거가 달랏음
                    break
            else:
                break

print(*switchs)





