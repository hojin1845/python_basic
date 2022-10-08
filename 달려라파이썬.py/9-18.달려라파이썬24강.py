#24강 if 연습문제
#요일 입력받기
today  =  input("요일을 입력하세요: ")

# 급식 변수
food = ""

#if 조건문을  써서 요일별 급식 알아보기
#월요일 돈까스
#수요일 카레
#금요일 햄버거
#그밖에 쌀밥

if today == "월요일":
    food = "돈까스"
elif today == "수요일":
    food = "카레"
elif today == "금요일":
    food = "햄버거"
else:
    food = "쌀밥"


print("요일:", today,"급식:",food)


