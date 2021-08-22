# 파이썬 문자형 ***중요!!

# 문자열 생성
str1 = "I am Python"
str2 = 'python'
str3 = """How are you?"""
str4 = '''Thanks'''

print(type(str1))
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열 선언
str1_t1 = ''
str2_t2 = ""
str3_t3 = str()

print(type(str1_t1), len(str1_t1))
print(type(str3_t3), len(str3_t3))

print()

# 이스케이프 문자 사용
# I'm Boy

print("I'am Boy")
# print('I'am Boy') # 에러나지!
print('I\'am Boy')  # \이스케이프문 뒤에 오는 문자는 그대로 출력한다.
print('I\\am Boy')

print('a \t b') # tab
print('a \n b') # 줄바꿈
print('a \"\" b')
print('\000 : 널 문자')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'Waht\'s on TV?'
print(escape_str2)

t_s1 = "Click \t Start!"
# t_s1 앞에 띄어쓰기 해보기 > 에러난다! 파이썬은 띄어쓰기에 민감하다..!
print(t_s1)

print()

# Raw String 역슬래시 신경 안쓰고 그대로 출력!
raw_s1 = r'\Users\joan\Desktop'
raw_s2 = r'\tUsers\njoan\Desktop'
print(raw_s1)
print(raw_s2)

print('--------')
# 멀티라인 입력
multi_str1 = """
따옴표를 이렇게 작성해야함
따옴표 시작을 줄바꿈해서 쓰고 싶으면??
"""
print(multi_str1)

print('--------')
# 역슬래시로 끝나면 이 다음에 어떤 변수를 바인딩한다.
multi_str2 = \
"""
이렇게 역슬래시 필요함
Hic mentitum cohaerescant.
Se an despicationes de doctrina multos nescius.
"""
print(multi_str2)

print('--------')
# 역슬래시 다음에 어떤 변수를 바인딩한다. 이것도 가능하지
multi_str3 = \
'one!' \
'two!!' \
'three!!!'
print(multi_str3)

print()

# 문자열 연산
str_o1 = "Python"   # 하나의 문자 문자를 리스트라고 생각하면 된다.
str_o2 = "Android"
str_o3 = "how are you"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('a' in str_o2)    # 'a' 있니? 대소문자도 구분하네
print('A' in str_o2)
print('p' not in str_o1) # 'b' 없니?
print('P' not in str_o1)

print()
# 문자열 형 변환
print(str(66), type(str(66)))   # 숫자 66을 입력했지만 문자열 66인셈
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))

print()
# 문자열 함수 (upper, isalnum, startswitch, count, 등등..)
print("Capitalize : ", str_o3.capitalize())  # 첫글자 대문자로
print("endswith : ", str_o2.endswith("d"))  # 마지막 문자가 무엇으로 끝나는지 확인
print("replace : ", str_o1.replace("Nice", "good")) # 해당하는게 없어서 그대로
print("replace : ", str_o1.replace("thon", "  good")) # 해당값 교체
print("sorted : ", sorted(str_o1))  # 정렬이 되서 나왔다..?
print("split : ", str_o3.split(' '))

print()
# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str))  # im_str에서 사용할 수 있는 모든 것 모두 나열.
# 그중에 __iter__ 가 있다? 시퀀스. 반복할 수 있다!

for i in im_str :
    print(i)

print()
# 슬라이싱 연습
str_s1 = "Nice Python"
print(str_s1[0:3])  # [] 안의 숫자는 인덱스를 의미. 마지막의 -1 인덱스까지 출력. 0부터 3-1까지
print(str_s1[:3])   # 처음부터 3-1까지.
print(str_s1[5:11])
print(str_s1[5:])   # 5부터 끝까지.
print(str_s1[:len(str_s1)]) # = [0:11] 랑 똑같은거
print(str_s1[:len(str_s1)-1]) # = [0:11] 랑 똑같은거
print(str_s1[:])    # ㅋㅋ이것도 되네
print(str_s1[0:11:2])  # 2칸씩
print(str_s1[0:11:3])   # 3칸    3번째 값은 단위로 보면 된다.
# 음수도 사용 가능! 뒤에서부터 세기. 마지막 글자가 -1
print(str_s1[-5:])  # -5 번째부터 오른쪽으로 끝까지
print(str_s1[1:-2]) # = [1:-2-1] 1부터 -3까지
# 단위에 음수 값을 써보면??
print(str_s1[::-1]) # 뒤에서 한글자씩 가져오는셈!!
print(str_s1[::-2])

print()
# 아스키 코드
a = 'z' # z를 표기하기 위해서 아스키 코드 표에 해당하는 값으로 컴퓨터는 해석하는...
print(ord(a))   # 해당 문자의 아스키 코드 값 구하기
print(chr(122)) # 해당 아스키값이 의미하는 문자 구하기
