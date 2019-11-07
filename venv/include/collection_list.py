# list - mutable
# 생성된 후에 변경가능
# 원소 추가 삭제 가능

# tuple - immutable
# 생성된 후에 변경 불가능

a = []
print(a)

a = [1,2,3,5,10]
print(a)

a = ['Korea','canada',1,23,[34,56]]
print(a)

a = 'hello world'
b = list(a)
print(b)

c = (1,2,3)
d = list(c)
print(d)

a = 'hello world nice weather'
b = a.split()
print(b)

a = [1,2,3,4,5,6]
print(a[2])
print(a[5])
print(a[-1])

# 불변(immutable) - 문자
a = 'hello world'
print(a[0])

# a[0] = 'j' 이러면 에러남

b = 'jello world'
c = 'j' + a[1:]

d = a.replace('h','j')
print(d)
print(a)

a = [1,2,3,4,5]
a[0] = 100
a[-1] = 90
print(a)

#
a = [1,2,3,4,5,6,7,8]
print(a[4:7])
print(a[:7])
print(a[3:])

# slicing
# start:end:increment(1)
print(a[1:7:2])
# 2,4,6출력
# 1부터 7까지 2씩증가 하면서 출력

# append()
# 리스트의 끝에 항목을 추가함 .

a = [1,2,3,4,5]
a.append(10)
print(a)

a = [1,2,3,4,5]
b = [6,7,8,9,10]
a += b
print(a)

a = [1,3,4,5,6]
a.insert(1,40)
# 1번째 index에 40추가
print(a)

a = [1,2,3,4,5]
a.remove(2)
print(a)
