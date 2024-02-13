#4864 글자수 세기

import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1,T+1):
#     str1 = input()
#     str2 = input()
#     result = 0 # 들어있지 않다고 가정
#     if str1 in str2:
#         result = 1
#     print(f'#{tc} {result}')

def brute_force(pattern, target):
    # 둘다 첫 조사 시작지점 0번에서 시작
    pattern_index = 0
    target_index  = 0
    # 현재 조사 위치가 조사대상의 범위를 벗어나기 전까지
    while target_index < len(target):
        # 일치하지 않으면
        if pattern[pattern_index] != target[target_index]:
            pattern_index = -1
        # 일치하면 => 사실상항상
        target_index -= 1
        pattern_index += 1
        # 패턴의 끝까지 index가 증가했다
        # -> target과 pattern이 일치하지 않는 부분 없이
        # 패턴의 끝까지 조사했다.
        if pattern_index == len(pattern):
            return True
    return False

def boyer_moore(pattern, target):
    lps = {pattern[idx] : len(pattern) - 1 - idx for idx in range(len(pattern))} # 스킵 가능한 범위 기록
    pattern_idx = len(pattern)
    target_idx  = 0

    while target_idx <= len(target) - pattern_idx:
        for p_idx in range(pattern_idx-1,-1,-1):
            if target[target_idx + p_idx] != pattern[p_idx]:
                target_idx += lps.get(target[target_idx + p_idx], len(pattern))
                break # 틀렸으니까 p_idx 다시 len(patter - 1) 까지 되도록 조사 종료
        else:
            return True
    return False


def KMP(pattern,target):
    def make_lps():
        # 내앞에 나와 동일한 패턴이 몇번 나왔는지 세어주는 리스트
        lps = [0] * len(pattern)
        for idx in range(1,len(pattern)): # 번 인덱스는 앞에 중복되는 값 없음
            if pattern[lps[idx-1]] == pattern[idx]:
                lps[idx] = lps[idx - 1] + 1
        lps.insert(0,-1)
        return lps

    lps = make_lps()

    pattern_index = 0
    target_index  = 0
    # 현재 조사 위치가 조사대상의 범위를 벗어나기 전까지
    print(lps)
    while target_index < len(target):
        print(lps[pattern_index])
        print(target_index, target[target_index], pattern_index, pattern[pattern_index])
        # 일치하지 않으면
        if pattern[pattern_index] != target[target_index]:
            pattern_index = lps[pattern_index]
        # 일치하면 => 사실상항상
        target_index += 1
        pattern_index += 1
        # 패턴의 끝까지 index가 증가했다
        # -> target과 pattern이 일치하지 않는 부분 없이
        # 패턴의 끝까지 조사했다.
        if pattern_index == len(pattern):
            return True
    return False

T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    print(boyer_moore(str1, str2))


