# 파이썬 리스트 **자료구조에서 중요
# 리스트 자료형 (순서 o, 중복 o, 수정 o, 삭제 o)

# 선언
a = []
b = list()
print(type(a))

c = [70, 75, 80, 85]
print(len(c))

d = [1000, 10000, 'Ace', 'Base', 'Captine'] # 서로 다른 자료형도 넣을 수 있음
e = [1000, 10000, ['Ace', 'Base', 'Captine']]   # 리스트안에 리스트도 가능

f = [21.42, 'footer', 3, 4, False, 3.141592]

print('>>>>')

# 인덱싱   원하는 데이터 꺼내오려면?
print('d : ', type(d), d)
print('d[1] : ', d[1])
print('d[0]+d[1] : ', d[0]+d[1])
print('d[-1], d[-3] : ', d[-1], d[-3])
print('e[-1][1] : ', e[-1][1], type(e[-1][1]))
print('문자열을 리스트 형태로 : ', list(e[-1][0]))

# str1 = 'text'
# lst1 = list(str1)
# print(lst1)

print('>>>>')

# 슬라이싱
print('d[0:3] : ', d[0:3])  # 0부터 3-1까지
print('d[2:] : ', d[2:])    # 2부터 끝까지
print('e[-1][1:3] : ', e[-1][1:3])

print('>>>>')

# 리스트 연산
print('c + d : ', c+d)  # 와우..? 리스트 더하기 리스트라니
print('c * 3 : ', c*3)  # OMG
# print("'Test' + c[0] : ", 'Test' + c[0])    # 문자 + 숫자느 불가. 형변환 필요
print("'Test' + str(c[0]) : ", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])

print('>>>>')

# Identity(id)  리스트도 효율성을 위해... 같은 주소를 바라보고 있다!
temp = c
print(temp, c)
print(id(temp), ' / ', id(c))

print('>>>>')

# 리스트 수정, 삭제
c[0] = 4
print(c)
# c[1:2] = ['a', 'b', 'c']
# print(c)    # 슬라이싱 사용. c[1]자리에 리스트가 통으로 들어가진 않았다.

# c[1] = ['a', 'b', 'c']
# print(c)    # 인덱싱 번호 사용했더니 리스트 통으로 들어감

# c[1:2] = [['a', 'b', 'c']]
# print(c)    # 슬라이싱 사용하고 리스트 통으로 넣으려면? [] 한번 더!

c[1:3] = [] # 빈값을 넣어서 삭제가됨. 실제로 삭제를 이렇게하진 않음 ㅎㅎㅎ
print(c)

del c[1]    # 리스트 삭제
print(c)

print(">>>> 여기")

#리스트 함수
a = [5, 2, 3, 1, 4]
print(a)
a.append(6)    # 마지막에 데이터 추가
print(a)
a.sort()    # 오름차순 정렬
print(a)
a.reverse() # 역순만들어줌
print(a)
print('a.index(3) : ', a.index(3))  # = a[3]
a.insert(2, 7)
print(a)

# del a[6]  # 인덱스 번호 찾아서 할 수 없으니
# print(a)
a.remove(1) # 해당 값 찾아서 삭제하기
print(a)
print('a.pop() : ', a.pop())    # 마지막 원소 꺼내오고 나머지원소글로 리스트 재구성
print(a)
# Last in First out!! lifo. 스택 예. 브라우저 뒤로가기 , fifo는 큐~!
a.pop()
print(a)
a.append(4)
print('a.count(4) : ', a.count(4))  # 리스트에 4가 1개

ex = [8,9]
a.extend(ex)
print(a)

# 삭제: remove, pop, del(인덱스 알아야함)
# 반복문 활용
while a:
    data = a.pop()
    print(data)
