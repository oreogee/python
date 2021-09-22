# 집합(Set) 특징
# 집합(Set) 자료형 (순서x, 중복x)

# 선언
a = set()
print(a)
print(type(a))
b = set([1, 2, 3, 4, 4, 4])  # 리스트 형식으로 넣어줌.
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'A', 'B', 'C', 'TEMP'} # 딕셔너리에 사용되던 {} 인데, key가 없다면 집합 선언한 것
f = {42, 'foo', (1,2,3), 3.14159}

print('a - ', type(a), a, 2 in b)
print('b - ', type(b), b, 2 in c)   # 중복허용하지 않아서 내부적으로 4가 3번 있는 것 정리함
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

print()
# 튜플 변환 (set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[-2], t[1:3])

print()
# 리스트 변환 (set -> list)
l = list(c)
l2 = list(e)
print('l - ', type(l), l)
print('l2 - ', type(l2), l2)
# 형 변환 자유롭다. 파이썬에서 이게 될까?? 싶은 것 웬만한 것은 다 된다!

print()
# 길이
print(len(a))
print(len(d))
print(len(e))
print(len(f))

print()
# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
s3 = set([1, 2, 3])
print('교집합 s1 & s2 : ', s1 & s2)
print('함수로 교집합 : ', s1.intersection(s2))
print('합집합 s1 | s2 : ', s1 | s2)
print('함수로 합집합 : ', s1.union(s2))
print('차집합 s1 - s2 : ', s1 - s2)
print('함수로 차집합 : ', s1.difference(s2))

print()
# 중복 원소 확인
print('s1, s2 (교집합있으면 False) : ', s1.isdisjoint(s2))   # false가 교집합 존재한다는 것!! dis가 있으니 반대로 나옴

# 부분 집합 확인
print('s1이 s2의 부분집합? : ', s1.issubset(s2))
print('s3이 s1의 부분집합? : ', s3.issubset(s1))
print('s1이 s3를 포함하는지? : ', s1.issuperset(s3))

print()
# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)
s1.remove(2)
print(s1)
# s1.remove(7)  # 없는 원소 제거 시도 > Error 발생
s1.discard(3)
print(s1)
s1.discard(7)   # 없는 원소 제거 시도 > Error 발생하지 않음!! 예외 발생시키지 않음.

s1.clear()
print(s1)
# 리스트도 clear 가능!
a = [1,2,3,4,5]
a.clear()
print(a)
