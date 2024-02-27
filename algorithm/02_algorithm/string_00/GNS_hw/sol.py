import sys
sys.stdin = open('input.txt')
earthLst = ["ZRO", "ONE" , "TWO", "THR", "FOR", "FIV","SIX", "SVN", "EGT", "NIN"] # 리스트 생성
T = int(input()) # 테스트케이스 입력
for test_case in range(1,T+1):
    strNumLst = [] # 문자를 숫자로 변경할 리스트
    N, M = input().split() # 입력 받기
    masLst = input().split() # 외계인이 입력한 리스트
    for i in range(int(M)):
        strNumLst.append(earthLst.index(masLst[i])) # 각 숫자별로 대입한 값을 str리스트에 넣음
    strNumLst.sort() # 정렬시킴
    print(N) # 테스트 케이스 출력
    for x in strNumLst:
        print(earthLst[x], end = ' ') # 다시 지구리스를 통해 원본으로 변경, 출력
    print()