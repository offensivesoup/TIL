def some():
    return False

## 객체 => 변수에 할당할 수 있는 것
## 모든 것은 변수에 들어갈 수 있지 => 파이썬은 다 객체다.
## 특성을 구분해서 생각하는 것이 어려운 것임.


## 모든 것이 객체이다.

a = 1
b = '가'
c = [1, 2, 3]
d = range(1,10)
e = map(int, '123')
f = set()
g = dict()
h = some 

## 함수가 객체인 이유

def other(arg):
    print(arg)

def some(func,arg):
    func(arg)
    return None

some(other, '안녕하세요')

a = [1,2]
b = ['a','b']
c = ['ㄱ','ㄴ']
d = list('가')

a.append(30)
b.append(20)
c.append(30)
d.append(30)

## 클래스는 공통된 요소들을 저장해놓은 것.
## 모든 사람은 숨을 쉰다. => 사람은 class , breath 는 함수(메서드)

class Person:
    def breath(self):
        print('습 하')

p1 = Person()
p2 = Person()

p1.breath()
p2.breath()
print(type(p1))
print(isinstance(p1,Person))

## 클래스를 통해 공통 속성을 만들어내고
## 각 클래스를 가진 인스턴스는 다른 특성을 가질 수 있다.
## p1의 이름과 p2의 이름이 다를 수 있는 것 처럼.
