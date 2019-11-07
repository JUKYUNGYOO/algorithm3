# https://www.acmicpc.net/problem/10539

# B를 보고, A라는 리스트 복원
N, B = int(input()), list(map(int,input().split()))
A = [B[0]]
# A라는 리스트를 복원, A의 첫번째 값은 B[0]와 같다.
for i in range(1,N):
    A.append(B[i]*(i+1)-sum(A))
#     지금까지 평균 B[i] * 갯수(i+1) - 기존의 합
# B[i] = 3 2 3 5
# B[1] = 2
# A 리스트에 B[0]은 초기 값으로 들어가 있으므로
# B[1]부터 시작한다.
for i in A:
    print(i,end=' ')

# 다른 방법
# N,B = int(input()),list(map(int,input().split()))
#
# A = [0 for i in range(B)]
# A[0] = B[0]
#
# for i in range(1,N):
#     A[i] = (B[i]*(i+1)-sum(A))
#
# for i in A:
#     print(i,end=' ')