# 아래 함수를 수정하시오.
def union_sets(aSet, bSet):
    answer = aSet.union(bSet)
    return answer


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)
