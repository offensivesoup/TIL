import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)

### 입력 받기

nums = []

while True:
    try:
        nums.append(int(input()))
    except:
        break

## 후위순회 하기

def postorder(s, e):
    # 만약 앞에 값이 커지면
    if s > e:
        return # 그만 볼거임
    ## 뒤에값을 기준으로 잡는다
    mid = e + 1

    # 자기를 제외한 애들로 순회를 돌면서
    for i in range(s+1, e+1):
        # 만약 자기보다 커지는 순간이온다면
        if nums[s] < nums[i]:
            # 다시 재 갱신
            mid = i
            break

    ## 순회를 돌린다
    postorder(s + 1, mid - 1)
    postorder(mid, e)
    print(nums[s])

postorder(0, len(nums)-1)