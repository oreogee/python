# 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서 o, 중복 o, 수정 x, 삭제 x) # 불변 immutable

# 선언

a = ()
b = (1)
b2 = (1,)    # 원소 1개일 때만 끝이 , 로 끝나야 튜플

print(type(a))
print(type(b))
print(type(b2))

c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>')
print('d[1] : ', d[1])
print('d[-1] : ', d[-1])
print('e[-1] : ', e[-1])
print('e[-1][1] : ', e[-1][1])
print('튜플을 리스트로 형변환 : ', list(e[-1]))
print('문자열을 튜플로 : ', tuple(e[-1][1]))

print('>>>> 수정 불가 확인 TypeError 발생')
# d[0] = 1500  # TypeError !! tuple object does not support item assignment

# 슬라이싱
print('>>>>')
print('d[0:3] : ', d[0:3])
print('d[2:] : ', d[2:])
print('e[2][1:3] : ', e[2][1:3])

# 튜플 연산
print('>>>>')
print('c + d : ', c + d)
print('c * 3 : ', c*3)

# 튜플 함수
print('>>>>')
a = (5, 2, 3, 1, 4, 3, 3)
print('index 함수. 인덱스값 구하는것 : ', a.index(3))
print('count 함수. 해당 값 몇 번? : ', a.count(3))

# 튜플에서는 팩킹 & 언팩킹 (packing and unpacking) 파이썬에서 중요!!
# 팩킹. 하나로 묶다. 튜플선언하는 것도 팩킹
t = ('A', 'B', 'C', 'D')

# 언팩킹
(x1, x2, x3, x4) = t    # x1, x2, x3, x4 = t 괄호 없어도 언팩킹 가능한데, 관습상 써주는게 매너
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹&언팩킹
t2 = 1, 2, 3    # 이렇게 선언해도 됨
t3 = 4,         # 이것도 가능. 괄호 생략 가능하니까
print(type(t2), type(t3))
x1, x2, x3 = t2     # 언팩킹
x4, x5, x6 = 4, 5, 6    # 언팩킹!! 튜플을 바로 써준거지

print(t2)   # 팩킹. 튜플로 출력됨
print(t3)   # 팩킹. 튜플로 출력됨
print(x1, x2, x3)   # 언팩킹
print(x4, x5, x6)   # 언팩킹
