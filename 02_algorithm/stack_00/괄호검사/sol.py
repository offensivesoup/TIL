import sys
sys.stdin = open('input.txt')

'''
    class를 활용한 Stack 구현은 오늘 하루만 할 것이다.
    이 외에는 list 와 append와 pop을 써서 연산한다.
    pop(0)의 시간복잡도가 O(N) 이듯이,
    max, min, sum, in 등은 모두 O(N)이다.
        -> 내부적으로 모두 for문으로 연산한다.
        -> 즉 for문 쓰는것과 속도가같다.
'''

class Stack:
    # stack을 할 때 필요한 값이 있는데,
    # stack의 크기를 지정해야 한다.
    def __init__(self,size):
        self.size = size
        # 자료구조 stack을 list를 활용하여 구현
        self.data = [None] * size # 값이 없음을 나타내는 None
        self.top  = -1 # 초기 값이 없으므로, top의 위치는 -1

    def push(self, item): # stack의 값 삽입 -> 삽입할 대상 item을 인자로 받는다.
        if self.is_full(): # stack이 가득 차면
            print('stack is full')
        else:
            # 받아온 item을 내 data의 top 번째 위치에 삽입한다.
            self.top += 1
            self.data[self.top] = item

    def get(self): # top번째 있는 요소를 출력할 수 있는 요소
        return self.data[self.top]

    def __str__(self): # instance print했을 때, stack안의 data를 바로 출력
        return f'{self.data}'

    def pop(self):
        if self.is_empty(): # stack 이 비었다면,
            print('Stack is empty')
        else:
            # top_value = self.data[self.top]
            # self.data[self.top] = None
            self.top -= 1
            # return top_value
            return self.data[self.top + 1]

    def is_empty(self):
        # top이 -1을 가리키고 있다면 stack은 비었다.
        return self.top == -1

    def is_full(self):
        return  self.size == self.top + 1

# stack 사이즈 100짜리 생성 후 출력
# stack = Stack(100)
# print(stack.size)
# print(stack.data)
# print(stack.top)
# stack.push(10)
# print(stack.data)
# print(stack.top)
# print(stack.get())
# print(stack)
# print(stack.pop())
# print(stack.top)
# print(stack.pop())
# print(stack.top) # -2 의 값을 반환한다.

T = int(input())

for test_case in range(1,T+1):
    bracket = input()
    result = True
    stack = Stack(100)
    for char in bracket:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if not stack.is_empty():
                stack.pop()
            else:
                result = False
                break
    if not stack.is_empty():
        result = False
    print(f'#{test_case} {result}')
