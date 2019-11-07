# https://www.acmicpc.net/problem/17269

# 8 14
# LEESIYUN MIYAWAKISAKURA

N,M = map(int,input().split())
A,B = input().split()

alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]


AB = ''
# AB를 기본문자열로 치면
min_len = min(N,M)

for i in range(min_len):
    AB += A[i] + B[i]
AB  += A[min_len:] + B[min_len:]
# 남은문자열 처리 - 긴 문자열을 뒤에 붙임
# list comprehension
lst = [alp[ord(i)-ord('A')] for i in AB]
# ord(i)
# i를 ASCII코드로 변환
# 앞에 값을 뒤에 더해주고, 마지막 값을 버려


# def f(lst):
#     ret = []
#     for i in range(lst-1):
#         ret.append(lst[i] + lst[i+1] % 10)
#     return ret



for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]
        lst[j] %= 10
print("{}%".format(lst[0] % 10*10 + lst[1] % 10))
