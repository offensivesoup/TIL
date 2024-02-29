import heapq

# q = PriorityQueue()
# q.put((45, 'z'))
# q.put((17, 'x'))
# print(q.queue)

arr = [(45, 'z'), (17, 'x'), (6, 'a'), (100,'b')]
heapq.heapify(arr)
print(arr)
'''
        6
    17  45
100
완전 이진 트리
'''
heapq.heappush(arr, (4,'t'))
print(arr)
heapq.heappush(arr, (30,'f'))
print(arr)
print(heapq.heappop(arr))
print(arr)