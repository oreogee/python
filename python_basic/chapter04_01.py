# 제어문 if

# 기본 형식
print(type(True))  # 0이 아닌 수, "비어있지 않은 문자열", [1,2,3...], (1,2,3...)
print(type(False))  # 0, "", [], (), {} 비어있는 것!

# 들여쓰기하지 않으면 Error 발생. 파이썬은 들여쓰기 민감함!
print('예1)')
if True:
    print('Good')

if False:
    print('Good2')

if [1, 2, 3]:  # = True
    print('Good3')

if []:  # = False
    print('Good4')
else:
    print('Else!!!')

# 관계 연산자: >, >= , <, <=, ==, !=
print('예2)')
x = 15
y = 10
print(x == y)
print(x != y)
print(x > y, x >= y)
print(x < y, x <= y)

print('예3) 흐름 제어')
city = ""
if city:
    print("city : ", city)
else:
    print("plz enter city")

# 논리연산자(중요!!)
# and, or, not
print('예4)')
a = 75
b = 40
c = 10

print('and: ', a > b and b > c)  # 모두 만족해야 True
# or 문에서 앞에 True가 나온다? 더이상 실행하지 않음. 앞에서 False 나온다? True 나오느지 더 확인해봄
print('or: ', a > b or b > c)
print('not: ', not a > b)
print('not: ', not True)

print()
# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print('e1: ', 3+12 > 7+3)  # 산술 먼저: 15 > 10
print('e2: ', 5+10*3 > 7+3*20)
print('e3: ', 5 + 10 > 3 and 7+3 == 10)
# 1. 산술 먼저: 15 > 3 and 10 == 10
# 2. 관계: True and True
# 3. 논리: True
print('e4: ', 5 + 10 > 0 and not 7 + 3 == 10)
# 1. 산술: 15 > 0 and not 10 == 10
# 2. 관계: True and not True
# 3. 논리: True and False 라서 False

score1 = 70
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')

print('예5)')
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')

print('예6) 다중 조건문')
num = 90
if num >= 90:
    print('Grade: A')
elif num >= 80:
    print('Grade: B')
elif num >= 70:
    print('Grade: C')
else:
    print('과락')

print('예7) 중첩 조건문')
grade = 'B'
total = 30

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')

# in, not in
print('예8)')
q = [10, 20, 30]
w = {70, 80, 90, 100}
e = dict(
    name="Yoo",
    city="Seoul",
    grade='A'
)
r = (10, 12, 14)
print(15 in q)
print(12 not in w)
print("name" in e)  # 키 조회 가능!
print("Seoul" in e.values())
print(e.values())
