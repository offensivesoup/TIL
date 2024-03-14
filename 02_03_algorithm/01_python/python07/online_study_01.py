# 세트 주의사항

my_set = {} # 빈 딕셔너리가 된다.
my_set = set() # 빈 세트의 생성
my_set = {1} # 요소가 하나라도 들어가면 세ㅐ트

# 세트 메서드

my_set = {'a', 'b', 'c', 1, 2, 3}

## add

my_set.add(4)
print(my_set)

my_set.add(4)
print(my_set)

## remove

my_set.remove('a')
print(my_set)

# my_set.remove('z')
print(my_set)

## clear


# my_set.clear()
# print(my_set)

## pop

my_set = {'a','b','c',1,2,3}
element = my_set.pop()
print(element)

my_set = {'a', 'b', 'c', 'd'}
elemnet = my_set.pop()
print(elemnet)

## update

my_set.update([1,4,5])
print(my_set)

## discard

my_set.discard(1)
my_set.discard('z')
print(my_set)

## 세트의 집합 메서드

set1 = {0,1,2,3,4}
set2 = {1,3,5,7,9}

print(set1.difference(set2)) ## 차집합, 세트1에 있고, set2에 없는 거
print(set1.intersection(set2)) ## 교집합
print(set1.issubset(set2)) ## 세트 1의 항목이 모두 세트2에 들어있으면 True, or False
print(set1.issuperset(set2)) ## 세트 2의 항목이 모두 세트1에 들어있으면 True, or False
print(set1.union(set2)) ##