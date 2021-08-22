# 파이썬 변수

# 기본 선언
n = 700  #컴퓨터 내부에 n이 생성된 주소에 700이란 값이 할당
print(n)
print(type(n))

# 동시 선언
x = y = z = 700
print(x, y, z)

# 선언하고 재선언. 재할당됨. 덮어쓰기
var = 75
var = "Change Value"
print(var)
print(type(var))

print()

# Object References
# 변수 값 할당 상태
print(300)      #편리성을 위해 int명시하지 않아도 되는 것
print(int(300)) #1>2>3의 과정을 통해 콘솔에 출력!
# 1.타입에 맞는 오브겢트 생성
# 2. 값 생성
# 3. 콘솔 출력

n = 777
print(n, type(n))

m = n
print(m, type(m))

m = 400
print(m, n)
print(type(m), type(n))

print()

# id(identity)확인 : 객체의 고유값 확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))

m = 800
n = 800
z = 800
i = 800

print(id(m))
print(id(n))
print(id(z))
print(id(i))
# 파이썬 내부에서 800이란 같은 값을 4개의 변수에 할당해서 쓴다? > 비효율이라고 판단
# 같은 값을 가져다가 쓰게됨. id값을 찍어보면 모두 같음
print(id(m) == id(n) == id(z) == id(i))

n *= 2
print(id(m))
print(id(n))
print(id(z))
print(id(i))
# 필요한 경우 값을 바꾸면 그 때가서 새로운 오브젝트 생성함
print(id(m) == id(n) == id(z) == id(i))

print()

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates > Method에서 많이 씀
# Pascal Case : NumberOfCollegeGraduates > Class에서 많이 씀
# Snake Case : number_of_colleage_graduates > 파이썬에서 변수 선언할 때 많이 씀

# 허용하는 변수 선언
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
# 밑줄, 달러 기호로는 시작 가능함. 숫자로 시작 불가ㅎㅎ
# 예약어는 변수명으로 사용 불가 예. as, class, for ...
# https://realpython.com/lessons/reserved-keywords/
