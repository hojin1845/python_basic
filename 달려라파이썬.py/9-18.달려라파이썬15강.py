#15강 리스트

#리스트[]
# numbers = [1,2,3,4,5]

# 다양한 자료형 : lion = [라이언,사자]
#list안에list도 가능

#+* : number = [1,2,3] + [4,5,6] 
#numbers = [1,2] * 3

#나의 운동 점수 리스트
score = [500,470,330,250,180,100]

# 인덱싱 하기
print(score)

# 슬라이싱 하기
# 앞에서부터 높은 점수 3개 가져오기
#print(score[0:3])

#뒤에서 낮은점수 3개 가져오기
#print(score[-3:])

#변경 , 삭제 : 인덱스를 이용한값 변경 삭제
#numbers[1] = 10
#del number

# 리스트의 값 삭제
del score[3]
print(score)