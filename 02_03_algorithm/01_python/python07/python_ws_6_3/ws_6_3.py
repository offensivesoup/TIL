# 아래 함수를 수정하시오.
def intersection_sets(aSet, bSet):
    answer = aSet.intersection(bSet)
    return answer


result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)
