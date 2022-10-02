#20강 dict 사전
#키(key와 값(value)의 쌍{키 : 값}
#fruits = {"사과":5,"오렌지":7}

#키 : 키에는 숫자,문자,튜플 사용 가능
#값 : 숫자,문자 뿐 아니라 리스트 같은 다양한 데이타 사용가능

#키와 값의 쌍 (키:값)
#contry_code = {80:"대한민국", 1:"미국"} : member = {"라이언":[160, 55]}

#인덱스 대신 키 입력
#fruits = {"사과":5, "오랜지":7}
#fruits[key]

# 과일과 과일갯수를 dict에 넣기
# 사과 5개,오렌지 7개
fruits = {"사과":5, "오렌지":7}
print(fruits)

#키를 이용해서 값 가져오기
#print(fruits["사과"], fruits["오렌지"])

#추가,변경,삭제 : fruits["사과"] = 10
#del fruits["사과"]

# 데이타 추가
# 딸기 20개
fruits["딸기"] = 20
print(fruits)

# 키를 입력해서 값 변경
# 사과 10개로 변경
fruits["사과"] = 10
print(fruits)

# 키를 이용해서 삭제
# 오렌지 삭제
del fruits["오렌지"]
print(fruits)