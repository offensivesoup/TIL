import sys
sys.stdin = open('input.txt', encoding='UTF-8')

from itertools import permutations
import math


## 강사님 수치 확인
N = int(input()) # 팀 수
teacher_score, teacher_exact = map(int,input().split())
teacher_result = teacher_score * (teacher_exact/100)
teacher = math.floor(teacher_result)

result = []
for team_num in range(1,N+1):
    boss_score, boss_exact, boss_char, boss_name = input().split()
    load_score, load_exact, load_char, load_name = input().split()
    team = (boss_name, load_name, f'({team_num} 팀)')
    ## 순위를 만들어주어야함
    ## 어휘별 점수 나누기
    boss_score = int(boss_score)
    load_score = int(load_score)
    boss_exact = int(boss_exact)
    load_exact = int(load_exact)
    if boss_char == "E":
        boss = math.floor(boss_score * (boss_exact/100))
    else:
        boss = math.floor((boss_score * (boss_exact/100)) * 0.7)
    if load_char == "E":
        load = math.floor(load_score * (load_exact/100))
    else:
        load = math.floor((load_score * (load_exact/100)) * 0.7)
    ## 팀원의 점수를 구한다
    team_avg = math.floor((boss + load) // 2)
    ## 팀원의 점수를 강사님과 비교한다
    ## 순열로 만들어 준다
    team_total = list(permutations(str(team_avg)))
    print(team_total)
    mini = 1e9
    for score in team_total:
        now = ''
        for s in score:
            now += s
        team_now = int(now)
        print(team_now)
        if abs(teacher_score - team_now) < mini:
            mini = abs(teacher_score - team_now)
    
    info = (team_avg, mini, team)
    result.append(info)

result.sort(key = lambda x : x[1])


for i in range(1,N+1):
    print(f'{i}등 : {result[i-1]}')