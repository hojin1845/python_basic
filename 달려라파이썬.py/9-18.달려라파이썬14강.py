#자료형bool (2)

#논리연산자 : and : or : not
# a and b : 두 값 모두 참인 경우만 True
# a or b : 두 값 중 하나라도 참인 경우 True
# not a :반대값 반환

# 논리연산자 테스트
# 수 입력받기
#x = int(input("수를 입력하세요 :"))

# and
# 입력값이 100보다 크거나 같고, 200보다 작은지 확인하기
#bVal = (x >= 100) and (x < 200)
#print(bVal)

# or
# 입력값이 100보다 작은지 또는 200보다 크거나 같은지 확인하기
#bVal = x < 100 or x >= 200
#print(bVal)

# not
#light_on = True
#print(light_on, not light_on)

#연습문제
height = int(input("키를 입력하세요"))
weight = int(input("몸무게를 입력하세요"))

# 백드롭 탑승 
bVal = height >= 132
print("백드롭 놀이기구 탑승 가능 :",bVal)

# 플라잉 다이노 소어 탑승
bVal = height >= 132 and weight >= 45
print("더 플라잉 다이노 소어 탑승가능 :", bVal)

#죠스탑승 탑승
bVal = height >= 122 or weight >= 30
print("죠스 탑승 가능:",bVal)




