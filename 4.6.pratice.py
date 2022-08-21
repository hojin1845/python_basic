#4.6.퀴즈 3
url = "http://youtube.com"
my_str = url.replace("http://", "") # 규칙 1
#print(my str)
my_str = my_str[:my_str.index(".")] # 규칙 2
#my_str[0:5] -> 0 ~ 5 직전까지. (0, 1, 2, 3, 4)
#rint(my_str)
password = my_str[:3] + str(len(my_str) + my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(password))