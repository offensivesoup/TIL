# function_vs_method.py (특히, str.method)
# 헷갈리기 시작하는 것
# 언제 어느 순간의 어떤 함수는 이렇게 작동하는데
# 얘는 왜 이렇게 작동함
# 이거 외우는가?
# str.title()
# str.upper()
# str.lower()
# str.join()
# str.is_decimal() ...
# string이 무엇인지 알아야 한다.
print('a'.zfill(5))

a = 'a'

while len(a) != 5:
    a = '0'+a
print(a)

# list의 메서드는 대체적으로 원본을 바꾼다.
# -> list는 원본을 바꿀 수 있으니까, 원본을 바꿈
# 메서드라는 것 자체가 ~~의 함수
# list.append(a) -> 반환값이 None
# list.extend() -> 반환값이 None
# list.pop() -> 반환값이 있음
# list.remove() -> 반환값이 None
    # 함수는 return하는게 일이 아니라
    # 함수는 무언가 input에 대한 처리를 하는 것이 함수가 하는 일
    # remove 메서드는 제거하려는 대상의 값을 내가 뭔지 알아야 한다.
    # pop은 그냥 없앤다.

# 파이썬은 함수의 return 값이 반드시 존재한다.
# 와
# 함수는 반드시 어떤 값을 반환해야 한다 XXXX
# 두 이야기는 다른 이야기

# 근데, 문자열 메서드는 죄다 반환값이 있는 것 같음.
## 문자열은 원본 수정이 안되니까.
a = 'hello world'
b = a.title()
print(b)