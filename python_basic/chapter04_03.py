# 반복문 while

# while condition:    조건에 만족하지 않을 때까지 계속 반복

# 예제 1
n = 5
while n > 0:
    print(n)
    n = n - 1

print()
# 예제 2
a = ['foo', 'bar', 'baz']

# while a: 이렇게 짜면 a가 데이터가 있는 상태이므로 while True. 무한반복하게 됨
#     print(a)

while a:
    print(a.pop())  # 하나씩 꺼내다보면 비니까 = false

print()
# 예제 3
# break, continue

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended')

print()
# 예제 4
m = 5
while m > 0:
    m -= 1
    if m == 2:
        continue    # 뒤에 실행하지 않고 다시 앞으로
    print(m)
print('Loop Ended')

print()
# 예제 5
i = 1

while i <= 10:
    print('i: ', i)
    if i == 6:
        break
    i += 1

print()
# 예제 6
# while - else 구문
n = 10
while n > 0:
    n -= 1
    print(n)
    # if n == 5:
    #     break
else:
    print('no break. else out.')    # for문과 동일. break만나지 않고 while끝나면 실행

print()
# 예제 6
a = ['foo', 'bar', 'baz', 'qux']
s = 'quxxx'

i = 0
while i < len(a):
    if a[i] == s:
        break
    i += 1
else:
    print(s, 'not found')

# 무한반복되지 않게 조심!!

print()
# 예제 8
a = ['foo', 'bar', 'baz']

while True:
    if not a:   # a = true. not a가 true 되려면?
        print('무한반복 out')
        break
    print(a.pop())
