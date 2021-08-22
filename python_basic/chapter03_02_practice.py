str1 = "PYTHON"
print(str1, '/', len(str1), '/', type(str1))

str2 = "HELLO\tPYTHON"
print(str2)
str3 = "HELLO\nPYTHON"
print(str3)
str4 = "\\t : 탭, \\n : 줄바꿈, \\000 : 널문자"    # \ 뒤에 오는 문자는 그대로 출력!
print(str4)
str_null = '\000'
print(str_null)

print()

str5 = r"\Users\joan\Desktop\t\n"   # raw string은 역슬래시 신경쓰지 않고 모두 출력
print(str5)

bool_t = True
bool_f = False
print(bool_t, " / ", bool_f)
print(int(bool_t), "/", int(bool_f))
