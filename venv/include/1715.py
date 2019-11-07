# https://www.acmicpc.net/problem/1715

# 문제유형 : 힙,자료구조,그리디

# ex1
# (10,20),40 -> (30,40) -> 70
# 30+70 = 100
# ex2
# (40,10),20 -> 50,20 -> 70
# 50 + 70 = 120

# 가장 크기가 작은 숫자 카드 묶음들을
# 2개씩 합치기 위해, 힙 자료구조를 이용합니다.

#    10        30        50
#    / \      /  \      /
#  20  40    50  40    70
#  /
# 50        비교 : 30  비교: 120
# min heap을 사용하면 원소들이 항상 정렬된 상태로 추가되고
# 삭제되며, min heap에서 가장 작은값은 언제나 인덱스 0,
# 즉, 이진 트리의 루트에 위치합니다.
import heapq
n = int(input())
heap = []

for i in range(n):
    data = int(input())
    heapq.heappush(heap,data)
#     데이터를 힙에 다 넣음
result = 0

while len(heap) != 1:
    # 가장 작은 원소 2개를 꺼냄
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one+two
    result += sum_value
    heapq.heappush(heap,sum_value)
print(result)
