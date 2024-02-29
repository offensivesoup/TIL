# 큐 생성
N = 10
q = [0] * 10
front = rear = -1

rear += 1 # euqueue(1)
q[rear] = 1
rear += 1 # euqueue(2)
q[rear] = 2
rear += 1 # euqueue(3)
q[rear] = 3
while front != rear: # 큐가 비어있지 않으면 # dequeue()
     front += 1
     print(q[front])