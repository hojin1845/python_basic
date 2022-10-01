# 17강 리스트 2
#list 함수 : append(), insert(), extend(),
#remove(),pop(),clear(),index(),count(),sort(),
#sort(),reverse()

# 메소드 : 특정 객체에 종속된 함수
#append("사과") : 리스트 맨 뒤에 추가
#insert(2,"사과") : 위치  지정해서 추가
#extend(["사과","배"]) : 여러값, 새로운 리스트 붙이기

# 과일 리스트
fruits = ["오렌지","사과","배","바나나","키위","사과","바나나"]
print(fruits)

#리스트에 값 추가
#리스트 맨 뒤에 값 추가
fruits.append("포도")
print(fruits)

#특정위치에 값 추가
fruits.insert(2,"복숭아")
print(fruits)

# 여러값 또는 새로운 리스트 추가
new_fruits = ["수박","체리"]
fruits.extend(new_fruits)
print(fruits)
