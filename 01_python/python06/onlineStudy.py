# print(type('1'))
# print(type([1,2]))

# print(help(str))
# print(help(list))

# def append():
#     pass

# append()


## 조회, 탐색, 검증 method

## find

my_str = 'banana'

print(my_str.find('b')) # 있으면 첫번째 인덱스
print(my_str.find('z')) # 없으면 -1

## index

print(my_str.index('b')) # 있으면 첫번째 인덱스
# print(my_str.index('z')) # 없으면 ValueError

## isalpha

string1 = 'Hello' 
string2 = '123'
string3 = 'a123'
string4 = '하이'

print(string1.isalpha()) # True
print(string2.isalpha()) # False
print(string3.isalpha()) # False 알파벳으로 구성되어있는지 확인
print(string4.isalpha()) # True

## 조작 method

## 리스트 메서드

## my_list

my_list = [1,2,3]

## append

my_list.append(4)
print(my_list) # [1,2,3,4]
print(my_list.append(4))

## extend

my_list.extend([4,5,6])
print(my_list) # [1,2,3,4,4,5,6] => unpacking되어 들어간다.

## insert

my_list.insert(3, 'ssafy')
print(my_list)

## remove

my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)

## pop

my_list = [1, 2, 3, 4, 5]
  
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1) # 5
print(item2) # 1
print(my_list) # [2, 3, 4]

## clear

my_list = [1, 2, 3]
my_list.clear()
print(my_list)

## index

my_list = [1, 2, 3]
index = my_list.index(2)
print(index)

## count

my_list = [1, 3, 2, 2, 3, 3]
count_num = my_list.count(3)
print(count_num)

## sort

my_list = [3,2,1]
sorted_list = my_list.sort()
print(sorted_list) # None
print(my_list)

# 내림차순

my_list.sort(reverse = True)
print(my_list)

## reverse() => 리스트의 순서를 역순으로 변경

my_list = [1,2,3,4,5,6,1,2,3,4,5,3,21,6,32,1,3,21,4,31, ' ']
my_list = ['1101','11','22','11','33','apple']
my_list.sort(reverse = True)
print(my_list)

# 복사

## 가변형타입

a = [1,2,3,4]
b = a
b[0] = 100
print(a) # [100,2,3,4]
print(b) # [100,2,3,4]

## 불변형타입

a = 100

b = a
b = 9

print(a) # 100
print(b) # 9

# => 같은 주소를 참조하기 때문에 => 주소를 할당하는 것이기 때문에

# 1. 할당

original_list = [1, 2, 3]
copy_list = original_list

copy_list[0] = 'hello'
print(original_list)
print(copy_list)

# 2. 얕은 복사

a = [1,2,3]
b = a[:]

b[0] = 100
print(a)
print(b)

## 한계

a = [1,2,[100, 200]]
b = a[:]
b[2][0] = 999
print(a)
print(b)


## 깊은 복사

import copy

original_list = [1,2,[1,2]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 100

print(original_list)
print(deep_copied_list)