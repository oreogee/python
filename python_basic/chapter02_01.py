# print 문  (역시 시작은 다 이건가)

print('파이썬 Python Start!')
print("double")
print('''333''')
print("""wow""")

print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N')
print('P','Y','T','H','O','N', sep='||')

print('010', '8577', '7170', sep='-')
print('ugeegee', 'gmail,com', sep='@')

print()

# .end 옵션
# print문으로 한줄 이어서 쓰기 가능. print문 끝에 어떻게 처리할건지
print('Welcome to', end='')
print('It news', end='')

print('Welcome to', end='    ')
print('It news', end='')

print()

# file 옵션
import sys

print('Learn Python', file=sys.stdout)   #sys.stdout 콘솔에 작성하는걸 의미

print()

#format 사용(d,s,f) d정수 s문자열 f실수
print('%s %s' % ('one', 'two'))  # 문자열의 자리임을 명시
print('{} {}'.format('one', 'two')) #format함수가 어떤 형식 드러가게끔 알아서
print('{1} {0}'.format('one', 'two'))

print()

# %s   문자열에서는 {}.format 형식 사용할 때 s 생략이 가능하다

## 오른쪽 정렬
print('%10s' % ('nice'))  # 총 자리수 10자리. 왼쪽부터 공백으로 채우고 문자열 채우기
print('{:>10}'.format('nice')) # 기호로 표시를 >함. 왼쪽부터 공백 채우기
## 왼쪽 정렬
print('%-10s' % ('nice'))  # 위에랑 정렬 반대. 문자열 채우고 오른쪽 공백으로 채우기
print('{:10}'.format('nice')) # 부등호 기호 없애면 오른쪽 공백으로 채우기
## 중앙정렬
print('{:^10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:@>10}'.format('nice'))

print('%5s' % ('pythonstudy')) # 5자리 넘어도 출력
print('%.5s' % ('pythonstudy')) #.5 5자리에서 절삭! 출력 멈춤

print('{:10.5}'.format('pythonstudy')) #공간은 10자리. 하지만 5자리까지만 출력. s 생략 가능


print()

# %d
print('%d %d' % (1,3))
print('{} {}'.format(1,3))

print('%4d' % (42))
print('%-4d' % (42))
print('{:>4d}'.format(42))
print('{:<4d}'.format(52))

print('{:4d}'.format(123456789))

print()

# f
print('%f' % (3.1434343434))
print('{:f}'.format(3.1434343434))

print('%1.3f' % (3.1434343434))  # 정수는 1자리, 소수점 3자리까지 출력

print('%06.2f' % (3.1434343434)) #총 자리 수 6. 소수점 이하 2자리. 003.14
print('{:06.2f}'.format(3.1434343434))
