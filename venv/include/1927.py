# https://www.acmicpc.net/problem/1927

# 파이썬에서 heapq 라이브러리를 구현하면 최소 힙을 간단히 구현할 수 있다.

import heapq

n = int(input())
heap = []
result = []

for _ in range(n):
    data = int(input())
    # 입력받은 데이터가 0이라면
    # pop()연산을 수행
    if data == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    #  데이터가 하나도 남아있지 않는다면, 0을 리스트에 넣음
    else:
        heapq.heappush(heap,data)
#         그렇지 않고 데이터 입력되면, 힙에 해당 데이터를 넣음
for data in result:
    print(data)

