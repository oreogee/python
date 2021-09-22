# 리스트 (순서 o, 중복 o, 수정 o, 삭제 o)
## [] 로 선언 = list()
print('## ----- 리스트')
lst1 = []
lst2 = list()
print(type(lst1), type(lst2), lst1, lst2)
lst1.append(1)
lst1.append('TWO')
lst1.append(3)
lst1.append('FOUR')
lst1.append(5)
lst1.append('SIX')
print(lst1)
lst1.reverse()
print('역순: ', lst1)
lst1.reverse()
# lst1.sort() string, int 섞여서 오름차순 불가

del lst1[1], lst1[2]
# lst[1], lst1[3] 으로 하면 'TWO' 삭제하고 5를 삭제하게 됨.
lst1.remove('SIX')
# 인덱스가 아니라 해당 값을 찾아서 삭제

lst1.append(0)
lst1.sort()
print('오름차순: ', lst1)
lst1.reverse()
print('POP!! Last in First out: ', lst1.pop(), lst1)
print(len(lst1))
lst1.append(1)
lst1.append(1)
lst1.append([1,1,1])
print('lst1에 1이 몇개? ', lst1.count(1))

print('# 슬라이싱 # ', lst1)
print('lst1[0:3] (0부터 3-1까지) : ', lst1[0:3])
print('lst1[3:] (3부터 끝까지) : ', lst1[3:])
print('lst1[-1][:] : ', lst1[-1][:])    # [:] 이것도 되네ㅎㅎ
print('lst1[:4] : ', lst1[:4] )

lst2 = ['Good', 'Bye']
lst1.extend(lst2)
print(lst1)
lst3 = ['A', 'B', 'C']
print('# 신기했던 리스트 연산 #')
print(lst2 + lst3)
print(lst3 * 3)

print(lst1 == lst1[:3] + lst1[3:])
print(lst2 == ['Good', 'Morning'])

print('튜플로 형변환 가능 : ', lst3 , '>>', tuple(lst3))
print(type(tuple(lst3)))

lst3.clear()
print('리스트 전체 삭제 : ', lst3)
print()
print()

# 튜플 (순서 o, 중복 o, 수정 x, 삭제 x) 불변. immutable.
## () 로 선언 *괄호 생략도 가능!! = tuple()
print('## ----- 튜플')
tp1 = ()
tp2 = (1)
tp3 = (1,)  # 원소가 1개일 때만 끝이 ,로 끝나야 튜플선언한 것
print(type(tp1), type(tp2), type(tp3))
tp1 = ('A', 'B', 'C', (1, 2, 3), [1, 2, 3])
print(tp1)
print(len(tp1))
# tp1[0] = 'a'    # 수정 불가!!
print('리스트로 형변환 가능 : ', tp1[-2], '>>', list(tp1[-2]))

print('# 슬라이싱 #')
print('tp1[-2][:2]: ', tp1[-2][0:2])

print('# 튜플도 리스트처럼 연산 가능 #')
tp3 = (1,2,3,4,5)
print('tp3*2 : ', tp3 * 2)
print('tp1+tp3 : ', tp1 + tp3)

print('# (중요) 팩킹 & 언팩킹 #')
tp4 = 1, 2, 3, 'A'  # 괄호 생략 가능함
tp5 = 'A',
print('팩킹 : ', type(tp4), tp4)
print('팩킹 : ', type(tp5), tp5)
x1, x2, x3, x4 = tp4    # 언팩킹
print('언팩킹 : ', x1, x2, x3, x4)
x5, x6, x7 = 5, 6, 7    # 이것도 언팩킹. 튜플 바로 써준 것
print('언팩킹 : ', x5, x6, x7)

print()
print()

# 딕셔너리 (순서 x, 키 중복 x, 수정 o, 삭제 o)
# Key, Value 한 쌍. Json 떠올리기.
## {} 로 선언 가능. 선언 방법이 많음.
## 원칙적으로는 선언은 dict([
#     ('Key', 'Value')
#     ('Key2', 'Value2')
# ])
print('## ----- 딕셔너리')
dict0 = dict([
    ('Name', 'YJY'),
    ('City', '서울 강동구'),
    ('Phone', 7170)
])
dict1 = {
    'Name': 'YJY',
    'City': '서울 강동구',
    'Phone': 7170
}
dict2 = dict(
    Name = 'YJY',
    City = '서울 강동구',
    Phone = 7170
)
print(type(dict0), dict0)
print(type(dict1), dict1)
print(type(dict2), dict2)
print(dict2['Name'])
print(dict2.get('Name'))
# print(dict2['Name2']) # 해당 Key없으면 에러 발생
print(dict2.get('Name2'))   # 해당 Key없으면 None
dict2['Age'] = 20
print('Age 추가 : ', dict2)
print('dict2 Key 개수 : ', len(dict2))
print('Key만 가져오기 : ', dict2.keys())
print('Value만 가져오기 : ', dict2.values())
print('Key,Value 모두 가져오기 : ', dict2.items()) # 가져온 형태보면 원칙적으로 dict 선언하는 것과 동일. dict([(Key, Value)])
print('POP 가능 : ', dict2.pop('City'))
print(dict2)
print('랜덤으로 POP : ', dict2.popitem())
print(dict2)
print('Key 조회 : ', 'Name' in dict2)
print('Key 조회(대소문자 구분) : ', 'name' in dict2)

dict2['Name'] = 'JIYEUN' # 키값으로 접근해서 수정 가능
print(dict2)
dict2.update(Name = 'Joan') # 명시적으로 함수 선언해서 수정
print(dict2)
tmp = dict( # 이렇게도 가능한데, 잘 안쓰는 방법
    Name = 'JY'
)
dict2.update(tmp)
print(dict2)

print()
print()

# 집합 (순서 x, 중복 x, 추가 o, 제거 o)
## {} 로 선언 = set()
print('## ----- 집합')
s1 = set()
print(type(s1), s1)
s2 = {'A', 'B', 'C', 1, 2, 3}
s3 = set([4, 5, 6, 'A', 'B', 'C']) # 리스트 형식으로 []로 넣어줘야함
print(type(s2), s2)
print(type(s3), s3)
print('합집합 : ', s2 | s3, '/ 함수: ', s2.union(s3))
print('교집합 : ', s2 & s3, '/ 함수: ', s2.intersection(s3))
print('차집합 : ', s2 - s3, '/ 함수: ', s2.difference(s3))
print(s2.isdisjoint(s3))    # dis가 들어갔으니. 교집합이 있으면 False
s4 = set(['A', 'B'])
print('s4가 s2의 부분집합? : ', s4.issubset(s2))
print('s2가 s4를 포함? : ', s2.issuperset(s4))
s4.add('C')
s4.add('D')
s4.add('E')
print('추가: ', s4)   # 순서가 없어서 실행할 때마다 출력 순서 바뀜
s4.remove('A')
s4.discard('B')
print('삭제:', s4)
# s4.remove('Z') # 없는 원소 삭제하면 Error
s4.discard('Z') # 없는 원소 삭제해도 Error 발생하지 않음
s4.clear()
print('전체 삭제: ', s4)
