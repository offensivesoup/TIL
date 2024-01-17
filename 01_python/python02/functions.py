# 리스트를 다루는 연습
# 수업시간에 다루지 않은 메서드라는 개념

# 어떤 함수를 정의하는데, 2개의 매개변수를 가진다.
def some_func(parm1, parm2):
    # 함수가 하는 일을 작성하는 영역
    result = parm1 + parm2

answer = some_func('가','나')
print(answer) # None => 값이 없음을 나타내기 위한 데이터 타입 | output이 없기 때문에

## 리스트란 시퀀스 형태의 데이터다
## 순서가 있는 값이고, 정렬 되어 있음을 보장하진 않는다.
## 내부 요소를 오름차순으로 정렬하고 싶다.

# method : 누군가가 가지고 있는 함수
# 내장함수 : 파이썬이 가지고 있는 함수

numbers = [4,3,2,1]
result = numbers.sort() # 사용 방법은 함수와 완전히 동일하다
print(result) # None 
print(numbers) # sort된 결과를 확인할 수 있다. => 즉 따로 변수 필요X

numbers = [4,3,2,1]
# sorted 함수와 sort 메서드의 차이
# list.sort() 메서드는 정렬 대상인 주어(리스트)가 정해져있다.
# sorted 함수는 '누구를' '정렬' 할 것인지 정해 줘야한다. -> 인자를 넘긴다.
print(numbers)
result = sorted(numbers)
print(result)

def some_func(parm1, parm2):
    # 함수가 하는 일을 작성하는 영역
    result = parm1 + parm2
    return result

answer = some_func('가','나')
print(answer)


def other_func(parm1, parm2):
    result = parm1 * parm2
    print(result, '함수 내부에서 실행')
    return result

answer = other_func(2,3)
print(answer, '함수 외부에서 실행')

answer = sorted(numbers, reverse = True)
print(answer)


def some_func(name, age):
    pass

a = 3
b = 3
some_func(age = a , name = b)


# def other_func(*args, name):
# 	pass

# other_func(1,2,3,4,5,6,7)



## LEGB 

global_var = 100
my_list = [1,2,3]
def local():
    # 글로벌 스코프의 변수 함수 내에서 출력
    my_list[0] = 100
    print(global_var)
    # 글로벌 변수의 값을 로컬에서 변경할 수 없다.
local()
print(my_list)



global_var = 100
def local(parm):
    parm += 3
    return parm

global_var = local(global_var)
print(global_var)

# gloabl 키워드만 사용 X

global_var = 100
def local():
    global global_var
    global_var += 3
local()
print(global_var)

