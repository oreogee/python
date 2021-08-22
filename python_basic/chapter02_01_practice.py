print('%s %s %s' % ('A', 'B', 'C'))
print('{} {} {}'.format('A','B','C'))
print('{2} {1} {0}'.format('A','B','C'))

print()

# 오른쪽 정렬
print('%10s' % 'TEN')
print('{:>10s}'.format('TEN'))

# 중앙 정렬
print('{:^10s}'.format('TEN'))

# 왼쪽 정렬
print('%-10s' % 'TEN')
print('{:<10s}'.format('TEN'))
print('{:10s}'.format('TEN'))

print()

print('{:10s}'.format('열글자 넘어가도 전부 출력되긴함'))
print('{:.10s}'.format('열글자까지만 출력되고 잘라버림'))
print('{:.10}'.format('s 생략도 가능!! 모든 곳에서 생략가능하진 않은듯하고 format형태일 때는 가능한듯?'))

print()

print('H', 'E', 'L', 'L', 'O')
print('H', 'E', 'L', 'L', 'O', sep='-')
print('ugeegee', 'gamil.com', sep='@')

print()
print('This is', end='')
print('ATOM')
print('This is', end='   ')
print('ATOM')
