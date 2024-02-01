## 정렬을 한다는 것은 무엇인가?(오름차순)
## 큰수가 뒤로간다는 것이거나, 작은수가 앞으로 오는 것
## 그럼 수마다 비교해줘서, 큰수를 뒤로 보내거나, 작은수를 앞으로 오게 하면 안될까?
## 반복문을 돌려서 인덱스는 커지니까, 큰수를 뒤로 보내는 게 맞을듯 하다

num_list = [2,1,3,9,4,5,6,12]
# 일단 한번 순회
for i in range(len(num_list)):
    # 순회 한 것에서 +해서 순회하는 것이 필요할 것 같다.
    # 2 가 뽑히면 1,3,0,4,5,6,12를 돌고 적절한 위치에 들어감
    # 1 이 뽑히면 2,3,9,4,5,6,12를 돌고 들어감
    # 3 이 뽑히면, 1,2,9,4,5,6,12를 돌고 들어감
    k = len(num_list) - i
    for j in range(1,k-1):
        if num_list[j] <= num_list[i]:
            # 작은수가 뒤로 가야하니까
            sort_num = num_list[i]
            num_list[j] = sort_num
            num_list[j-1] = num_list[i]

print(num_list)
