# https://www.acmicpc.net/problem/1766

# 문제집
# 문제난이도 중(Medium)
# 문제유형 : 힙, 위상정렬

# 본 문제는 전형적인 위상 정렬 문제임.
# 위상정렬은 순서가 정해져 있는 작업을 차례로 수행해야 할 때,
# 순서를 결정해주는 알고리즘이다.
# 위상 정렬의 시간 복잡도는 O(V+E)로 문제를 해결 할 수 있다.
# 위상 정렬의 시간 복잡도는 노드의 갯수 + 간선의 갯수로 해결
# 3->1
# 4->2
#
# 정답예시  : 3-1-4-2

# 위상정렬 알고리즘
# 1) 진입차수가 0인 정점을 큐에 삽입.
# 2) 큐에서 원소를 꺼내 해당 원소와 간선을 제거
# 3) 제거 이후에 진입 차수가 0이 된 정점을 큐에 삽입
# 4) 큐가 빌 때까지 2-3)과정 반복
#
# 모든 원소를 방문하기 전에 큐가 빈다면 사이클 존재
# 모든 원소를 방문 했다면 큐에서 꺼낸 순서가 위상 정렬의 결과

import heapq
n,m = map(int,input().split())
array = [[]for i in range(n+1)]
# 모든 노드에 대해서 어떤 정보를 담는지 array
indegree = [0] * (n+1)

heap = []
result = []

# 어떤 노드들이 연결되어 있는 지 확인가능
# x,y로 이어져 있음
for _ in range(m):
    x,y = map(int,input().split())
    array[x].append(y)
    indegree[y] +=1
#     간선이 이어진 진입 차수가 몇개인지 .

for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(heap,i)
result = []

# 힙이 빌 때까지 반복을 하는데
while heap:
    data = heapq.heappop(heap)
    # 힙이 빌 때까지 하나씩 꺼내서
    result.append(data)
    # 큐에서 꺼낸 데이터를 result에 담고

    # 꺼낸 데이터에서 이동할 수 있는 정점 들에 대해서 확인
   for y in array[data]:
        # 간선을 제거
        indegree[y] -=1
        # 진입차수가 0으로 바뀐 것 들을
        if indegree[y] == 0:
            heapq.heappush(heap,y)
#             힙에다가 넣음
for i in result:
    print(i,end='')




