## question

'''
1.
함수를 정의할 때, 매개변수에 패킹을 사용해서
가변인자로 받게 되면 튜플로 받는데...

왜, 변수에 패킹을 사용해서
다수의 데이터를 받으면 리스트로 받는 이유는 뭔가요?

tuple
- 순서가 있는 시퀀스
- 순회가 가능한 iterable
- 여러개의 데이터를 담는 collection
- 변경 할 수 없는 immutable

list
- 순서가 있는 시퀀스
- 순회가 가능한 iterable
- 여러개의 데이터를 담는 collection
- 변경 가능한 mutable
'''

## 함수에 가변인자는 튜플

# 함수는 입력값에 따른 정확한 출력값을 기대한다
# 함수가 하는 일에 대해서 항상 같은 입력값에 같은 출력값이 나와야 한다.
# 애초에 코드를 그렇게 안쓰면 되는거 아닌가?
    # 매개변수로 넘겨 받은 데이터가 변경되지 않도록 코드를 쓴다.
    # 일부로 tuple로 한번 더, 

def some_func(*args):
    print(args) # (1,2,3,4)
    print(type(args)) # tuple

some_func(1,2,3,4)

# 변수에 값을 할당할때의 기대값은,
# 특정 데이터를 편하게 참조할 수 있는 기능,
# 해당 데이터의 값을 변경하거나, 조작하거나, 활용하는 용도를 기대

a, *b, c = [1,2,3,4,5]
print(b) # [2,3,4]
print(type(b)) # list

print([1,2,3,4,5])
# 하나의 리스트를 출력하는 것
print(*[1,2,3,4,5])
# 5개의 인자를 튜플에 담아, 순회하며 출력하는 것



'''
2.
기명 함수 정의 키워드
def 함수 이름(매개변수, 매개변수): (이름이 있어서 나중에 다시 부를 수 있음)
    함수 할일
- 코드 재사용 가능
- a데이터도, b데이터도, c데이터도 매번 ㄱ함수를 거쳐야 한다....

익명 함수 정의 키워드
lambda (매개변수, 매개변수) : 함수 할일
- 코드 재사용 불가능
- 아주 간단한 로직인데, 순회가능한 어떤 데이터에 대해서
- 각 요소들에 대해서만 똑같은 로직을 실행해야 할 때.
'''

def my_sum(num1, num2):
    return num1 + num2

result = my_sum(1, 2)

my_sum_lambda = lambda num1, num2 : num1 + num2
result_2 = my_sum_lambda(3, 4)

print(result)
print(result_2)

a = [1,2,3]
b = [4,5,6]
result_3 = list(map(lambda num1, num2 : num1 + num2, a, b))

print(result_3)

result_4 = list(map(my_sum, a, b))
print(result_4)