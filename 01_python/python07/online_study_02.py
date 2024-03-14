## 딕셔너리 메서드

## clear

person = {
    'name' : 'Alice',
    'age' : 25
    }
person.clear()
print(person)

## get

person = {
    'name' : 'Alice',
    'age' : 25
    }

print(person['name'])
print(person.get('name')) # Alice
print(person.get('country')) # None
print(person.get('country', '키가 없습니다.')) # Unknown

## keys()

print(person.keys())

for key in person.keys():
    print(key)

## values()

print(person.values())

for value in person.values():
    print(value)

## items
    
print(person.items())
for k,v in person.items():
    print(k,v)


## pop

print(person.pop('age'))
print(person)
# print(person.pop('country'))
print(person.pop('country',None))

## setdefault

person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country','Korea'))
print(person)

## update

other_person = {'name' : 'Jane', 'gender' : 'Female'}
person.update(other_person)
print(person)

person.update(age = 50, country = 'korea')
print(person)


### 해시 테이블

my_list = [{'john' : 521-1234},
           {'Lisa' : 521-8976},
           {'Sandra' : 521-9655}]

my_dict = {'john' : 521-1234,
            'Lisa' : 521-8976,
            'Sandra' : 521-9655
            }

## 위에는 바로 처음부터 검색을 시작해야 한다.
## 아래 dict는 lisa가 어디에 있던지 상관 없다.


my_set = {3,2,1,9,100,4,87,39,10,52}

print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())


## => 정수값은 해시 함수를 통해도, 그냥 정수값이 해시값이된다.

print(hash(1))
print(hash(1))
print(hash('a'))
print(hash('a'))