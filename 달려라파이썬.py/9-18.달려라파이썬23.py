#23강 if문 2
#학생 입력받기
ret = input("학생번호를 입력하세요:")
number = int(ret)
# 팀 이름
team = "팀 없음"

# if 조건문을 써서 번호별 팀 알아보기
# 1 ~ 10번까지 A팀
# 11 ~ 20번 까지 B팀
# 21 ~ 30번까지 C팀
# 나머지 D팀
if number <= 10:
    team = "A"
elif number > 10 and number <= 20:
    team = "B"
elif number > 20 and number <= 30:
    team = "C"
else:
    team = "D"

print("학생번호", number,"팀 이름",team)

