# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열 (시퀀스)
list : 리스트 (시퀀스)
tuple : 튜플 (시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = "Anaconda"
float_v = 10.0
int_v = 7
list = [str1, str2]
dict = {
    "name": "Machin Learning",  # Key: value
    "version": 2.0
}
tuple = (7,8,9) # 괄호 형태가 list랑 다름
tuple2 = 7,8,9  # 괄호 생략도 가능하지만, 생략하지 않고 쓰기!
set = {7,8,9}

print(list)
print(type(str1))
print(type(bool))
print(type(float_v))
print(type(int_v))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

print()

#숫자형 연산자
"""
+ - * /
// : 몫
% : 나머지
abs(x) : 절대값
pow(x,y) : x의 y승
x ** y : x의 y승
"""

# 정수 출력
i = 77
i2 = -14
big_int = 77777777777777777777777777777777777777777779999999999999999999999
# 파이썬은 이렇게 큰수도 int로 할당 가능!
print(i, i2, big_int)
print(type(big_int))

print()

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3/9
print (f, f2, f3, f4)

print()

# 서로 다른 형 계산하면 형변환이 자동으로 이루어짐
a = 3 + 1.0
print(a, type(a))

# 형 변환
a = 3. # 0생략 가능
b = 6
c = .7
d = 12.7

print(type(a), type(b), type(c), type(d))

print(float(b))
print(int(c)) # 1미만을 정수형으로 형변환하니 0됨
print(int(d))
print(int(True), float(False)) # 프로그래밍 언어 공통이지. True 1 False 0
print(complex(3))
print(complex('3')) # 문자형을 숫자형으로 바꾸고 실행됨! 똑똑한 파이썬 ㅋㅋ
print(complex(False))

print()

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)
print(x, y)
print(pow(5,3), 5 ** 3)

print()

# 외부 모듈(패키지 안에 모듈이 있다!?)
import math

print(math.pi)
print(math.ceil(5.1)) # x 이상의 수 중에 가장 적은 정수. = 올림 ㅋㅋㅋㅋ
