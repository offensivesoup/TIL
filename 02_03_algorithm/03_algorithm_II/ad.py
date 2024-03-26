### 월말평가 준비

## 2진수 16진수 10진수

value = 60

b = bin(value)
o = oct(value)
h = hex(value)

print(b)
print(o)
print(h)

'''
0b111100
0o74
0x3c
결과는 전부 문자열이다
'''

b = int('0b111100', 2)
o = int('0o74', 8)
h = int('0x3c', 16)

print(b) # 바꾸고자 하는 진수 형태를 넣어주면 된다.
print(o)
print(h)

## 2진수를 16진수로 변환하기

## 다음 코드에서 format 함수를 사용해서 04b를 주면 4자리 2진수로 표현된다.
## int뒤에 표현하고자하는 수와, 그 진법을 주면 10진수로 표현된다.
## 그걸 bin 에 넣으면 01b ~~ 로 되지만, format에 넣으면 된다.

T = int(input())
for test_case in range(1,T+1):
    print(f'#{test_case}', end = ' ')
    N, N16 = input().split()
    for char in N16:
        print(format(int(char, 16), '08b'), end = '')
    print()