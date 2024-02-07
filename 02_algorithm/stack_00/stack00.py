def push(n, size):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = n



top = -1
stack = [0] * 10 # 최대 10개 push
size = 10

top += 1  # push(10)
stack[top] = 10
top += 1  # push(20)
stack[top] = 20

push(30,10)

while top >= 0:
    top -= 1
    print(stack[top+1])
