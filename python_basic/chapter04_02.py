# 반복문 FOR

# 코딩의 핵심
# for in <collection> 집합의 모음
#   <Loop body>

for v1 in range(10):  # 0부터 10-1까지
    print('v1 is : ', v1)

print()
for v2 in range(1, 11):  # 1부터 10까지
    print('v2 is : ', v2)

print()
for v3 in range(1, 11, 2):  # 1~10  2칸씩 띄고
    print('v3 is : ', v3)

# 1 ~ 1000까지의 합
print()

sum1 = 0

for v in range(1, 1001):
    sum1 += v
    if(v == 1000):
        print("1~1000 총 합: ", sum1)

print('1~1000 총 합 함수로: ', sum(range(1, 1001)))

print(type(range(1, 10)))
print('1~1000 4의 배수의 합: ', sum(range(4, 1001, 4)))

# Iterables 자료형. 반복. for문에서 사용 가능
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

print()
print("Iterables 자료형")
# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']
for name in names:
    print('You are : ', name)

# 예제2
lotto_numbers = [11, 19, 23, 27, 30, 36]
for n in lotto_numbers:
    print("Current number : ", n)

# 예제3
word = "Beautiful"
for s in word:
    print('word : ', s)

# 예제4
# 헷갈리는데, 딕셔너리 선언
# dict(로 선언할 때는 key = 'value')  /  {에 사용할 때는 'key' : 'value'}
my_info = dict(
    name='Yoo',
    age=20,
    City='Seoul'
)

for k in my_info:
    print('key: ', k, '/ value: ', my_info[k])
    print('key: ', k, '/ value: ', my_info.get(k))

for v in my_info.values():
    print('value: ', v)

# 예제5
name = 'FineApple'
name2 = ''
for n in name:
    if n.isupper():
        name2 += n
    else:
        name2 += n.upper()
print(name2)

# break = for문 탈출!
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for n in numbers:
    if n == 34:
        print(n, "찾음!!!")
        break  # 36,38은 실행하지 않음. 원하는 시점에 for문 탈출하는 것
    else:
        print('Not fount: ', n)

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]  # complex 복소수
for v in lt:
    if type(v) is bool:  # 자료형 비교할 때 is
        continue  # 뒤에 SKIP되는 것. if보다 들여쓰기 되어야 함
    print("current type: ", v, type(v))  # 여기 들여쓰기 한번 더하면 continue랑 묶이나봄. 실행안됨.
    print("multiply by 2", v * 3)

# for - else
for num in numbers:
    if num == 24:
        print(num, "찾음!!!")
        break  # if보다 들여쓰기 되어야 함
else:  # for문으로 원소 전부 돌았지만 해당사항이 없었다 > else 실행
    print('Not found !!!')

# 구구단
for i in range(2, 10):  # range (n,m) n부터 m-1까지
    for j in range(1, 10):
        # print(i, '*', j, '=', i*j)
        print('{:4d}'.format(i*j), end='')  # end='' 개행하지 않겠다.
    print()

# 변환 예제
name2 = 'Acemannn'
print('Reversed', reversed(name2))
print('List', list(reversed(name2)))  # 형변환 가능!
print('tuple', tuple(reversed(name2)))
# 집합은 순서가 없지. 중복된 값이 있다면? 제거. 대소문자 구분. 아스키코드 값이 다르니까
print('set', set(reversed(name2)))
