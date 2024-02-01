import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    aCnt = 0 # a가 책을 찾은 횟수
    bCnt = 0 # b가 책을 찾은 횟수
    p, pa, pb = map(int,input().split()) # 전체 페이지, a가 찾을 페이지, b가 찾을 페이지
    start_num = 1 # 책의 시작
    end_num   = p# 책의 끝
    while True:
        center_num = (start_num + end_num) // 2
        if start_num >= end_num:
            aCnt = 0
            break
        if center_num == pa:
            aCnt += 1
            break
        elif pa < center_num:
            end_num = center_num
            aCnt += 1
        elif pa > center_num:
            start_num = center_num
            aCnt += 1
    start_num = 1
    end_num   = p
    while True:
        center_num = int((start_num + end_num) / 2)
        if start_num >= end_num:
            bCnt = 0
            break
        if center_num == pb:
            bCnt += 1
            break
        elif pb < center_num:
            end_num = center_num
            bCnt += 1
        elif pb > center_num:
            start_num = center_num
            bCnt += 1
    if aCnt < bCnt:
        print(f'#{test_case} A')
    elif aCnt == bCnt and aCnt != 0 and bCnt != 0:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} B')


def binary_search(start, end, target, cnt):
    T = int(input())
    for tc in range(1,end) // 2
        middle = int((start + end) / 2)
        if middle == target:
        # 언제까지? 중간지점이 내가 찾는 대상이면
            return cnt
        else:
            if middle > target:
                binary_search(start, middle, target, cnt+1)
        else: