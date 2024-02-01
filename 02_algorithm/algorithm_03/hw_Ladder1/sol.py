import sys
sys.stdin = open('input.txt')
'''
사다리게임으로 아이스크림 내기함
김대리가 사다리를 그리는데 문득궁금해짐
어느 사다리를 구하면 X로 갈 수 있을까?
'''

# for test_case in range(1,11):
#     T = int(input())
#     ladder = [list(map(int,input().split())) for _ in range(100)]
#     for i in range(len(ladder)):
#         if ladder[99][i] == 2:
#             for j in range(len(ladder)-1,-1,-1):
#                 left_move = 0
#                 right_move = 0
#                 if i != 0 and ladder[j][i-1] == 1:
#                     for l in ladder[j][i:-1:-1]:
#                         if l == 0:
#                             break
#                         left_move += 1
#                 elif i != 99 and ladder[j][i+1] == 1:
#                     for r in ladder[j][i:]:
#                         if r == 0:
#                             break
#                         right_move += 1
#                 elif ladder[j][i] == 1:
#                     continue
#                 i += right_move
#                 i -= left_move
#                 select = i
#     print(f'#{test_case} {select}')

for test_case in range(1,11):
    T = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    endLst = []
    for idx in range(len(ladder)):
        if ladder[0][idx] == 1:
            endLst.append(idx)
    start_idx = ladder[99].index(2)
    my_line   = endLst.index(start_idx)
    for i in range(99,-1,-1):
        if endLst[my_line] != 0 and ladder[i][endLst[my_line] - 1] == 1:
            my_line -= 1
        elif endLst[my_line] != 99 and ladder[i][endLst[my_line] + 1] == 1:
            my_line += 1
        else:
            pass
    print(f'#{test_case} {endLst[my_line]}')





