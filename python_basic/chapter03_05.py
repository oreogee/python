# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용 (json도 이런 형태지-!)
# 딕셔너리 자료형 (순서X, 키 중복X, 수정O, 삭제O)

# 선언  상당히 많은 방법이 있음. 편한 방법 택하면 됨.
# [리스트] (튜플) {딕셔너리}
a = {'name': 'Kim', 'phone': '01085777170', 'birth': '870514'}
# a = {'name': 'Kim', 'name': 'Lee'}  이렇게 중복 불가!
b = {0: 'Key 숫자 문자 모두 가능하다'}
c = {'arr': [1,2,3,4]} # 이렇게 리스트 넣을 수 있음
d = {
    'Name': 'Yoo',
    'City': 'Seoul',
    'Age': 22,
    'Grade': 'A',
    'Status': True
}

# 원칙적으로 선언하는 방법. []리스트 안에 ()튜플로 선언해줘야함. 잘 쓰이진 않음
e = dict([
    ('Name', 'Yoo'),
    ('City', 'Seoul'),
    ('Age', 22),
    ('Grade', 'A'),
    ('Status', True)
])

# 강사님이 주로 사용하는 방법 ㅎㅎ
f = dict(
    Name='Yoo',
    City='Seoul',
    Age=22,
    Grade='A',
    Status=True
)

# d=e=f 모두 같은 값 선언한 것
print('a - ', type(a), a)
print('d - ', type(d), d)
print(e)
print(f)

# 출력
print('a - ', a['name']) # 대소문자 구분함. 'Name'으로는 못찾음
print('a - ', a.get('name'))

# Key로 접근, get으로 접근 차이점 !! key 값이 없을 때
# print('a - ', a['name1'])   # Error 발생
print('a - ', a.get('name1'))   # None 으로 출력. 좀 더 안전하게 개발 혹은 None 따로 처리하든

print('b - ', b[0])
print('b - ', b.get(0))


# 딕셔너리 추가
a['address'] = 'seoul'  # 'name'에 넣으면 덮어쓰기
print('a - ', a['address'])
a['rank'] = [1,2,3] # list도 추가 가능
print('a - ', a)

print()
# len = 키의 개수 세는 것
print('a - ', len(a))
print('b - ', len(b))
print('d - ', len(d))

print()
# key값만 가져오기
print('a - ', a.keys())
print('b - ', b.keys())
print('d - ', d.keys())
print(type(a.keys()))

print(list(a.keys()))
print(list(b.keys()))

print()
# value값만 가져오기
print('a - ', a.values())
print(type(a.values()))

print(list(a.values()))
print(tuple(a.values()))
print(list(b.values()))

print()
# key, value 둘다 가져오기
# 이 형태 원칙적으로 선언했던 e 형태와 동일. 리스트안에 튜플
print('a - ', a.items())
print('b - ', b.items())
print('d - ', d.items())
print(list(a.items()))

print()
print('a - ', a.pop('name'))    # pop은 꺼내오고 제거
print('a - ', a)
print('c - ', c.pop('arr'))
print('c - ', c)

print()
print('f - ', f.popitem())  # 랜덤으로 꺼내오고 제거
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)    # 다 꺼내서 비었음
# print('f - ', f.popitem())    # 또 꺼내면 Error. dictionary is empty
# print('f - ', f)

print()
# 키 조회하기
print('a - ', 'birth' in a)
print('a - ', 'Birth' in a) # 대소문자 구분
print('a - ', 'birth2' in a)

print()
# 수정 & 추가   키값으로 접근해서 가능
a['test'] = 'test_dict'
print(a)
a['test'] = 'test_modify'
print(a)
# update 함수도 있다. 문법적으로 확실하게 표현
a.update(birth="900715")
print(a)
# 이렇게는 잘 쓰지 않지만.. 이렇게도 가능
tmp = {'address': 'Busan'}
a.update(tmp)
print(a)
