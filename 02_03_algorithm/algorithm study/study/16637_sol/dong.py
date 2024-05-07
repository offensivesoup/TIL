'''
괄호안에 괄호는 안되고,
괄호를 추가해 식의 최대값을 만드려면??
연산자는 곱이거나, 뺴기거나, 더하기
그럼 최대값이 된다는 것은 무슨 의미이지?

어쨋든 식은 순서대로 진행하는데, 그럼
1. 제일 많은 값을 더해주고,
2. 제일 적은 값을 빼주는 틀에서 벗어나지 않으면된다.
=> 연산자의 연속순서에 대해 고려해보면 된다.
어차피 +나 -는 괄호가 있으나 없으나 별로 상관이 없어
1 + 2 + (3 - 4) 예시로
1 + 2 - 1 이 되어버리더라도, 
어차피 값은 똑같다는 거임
그럼 곱셈을 마주했을 때, 이녀석이 괄호를 넣을지 말지를 선택하는 로직이 필요함
이는, 곱셈의 앞에 있는 수들을 최대로 만들어줄 순서를 정하는 거임
그럼 1. 현재까지 곱셈이 아닌, 만난 수식에 대한 정리가 필요하다.
2. 곱셈의 앞에 값을 최대로 만들어주는 것이 이 식의 결과를 최대로 만드는 방법
앞에 값을 최대로 만든다는 것은?
만약 앞에 값이 음수라면=> 곱셈을 최소화 하고
앞에값이 양수라면 => 곱셈을 최대화
그럼 이렇게말고 완전탐색을 해야한다면?
그냥 괄호가 쳐져 있거나, 안쳐져 있는 경우의 수를 나누어 볼 수 있다.
'''

import sys
sys.stdin = open('input.txt')

def calculate(x, operator, y):
  if operator == '+':
    num = x + y
  elif operator == '-':
    num = x - y
  elif operator == '*':
    num = x * y
  return num
    
def dfs(idx, value): # 쭉 나아가면서 더해줄값
  global result
  if idx == n-1:
    result = max(value, result)
    return
  if idx < n-2:
    next = calculate(value,express[idx+1],int(express[idx+2]))
    dfs(idx + 2, next)
  if idx < n-4:
    next_next = calculate(int(express[idx+2]),express[idx+3],int(express[idx+4]))
    next = calculate(value, express[idx+1] , next_next)
    dfs(idx + 4, next)

result = -1e9
n = int(sys.stdin.readline())
express = list(sys.stdin.readline())
dfs(0, int(express[0]))
print(result)