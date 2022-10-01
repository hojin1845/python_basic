#18강 리스트(3)
#함수 사용법 : 함수 : 특정작업을 한뒤 결과값을 돌려주는것
#리턴값 = 함수이름(전달값) : print("Hello world ") 

#remove("사과") : 전달값 삭제(첫번째 한개만 삭제)
#pop() : 맨뒤에서 값 꺼내오기(꺼내온 값은 리스트 에서 삭제됨)
#clear() : 모두삭제

# 과일 리스트
fruits = ["오렌지","사과","배","바나나","키위","사과","바나나"]
print(fruits)

#리스트에서 값 삭제
#fruits.remove("배")
#print(fruits)

# 맨 뒤에서 값 꺼네오기
#my_fruit = fruits.pop()
#print(my_fruit)
#print(fruits)

# 리스트의 모든것을 삭제
#fruits.clear()
#print(fruits)

# 리스트
#index("사과") : 전달값의 인덱스 가져오기 : (첫번째 index 가져오기)
#count("사과") : 전달값의 개수 가져오기

# 바나나 객수 가져오기
#count = fruits.count("바나나")
#print(count)

# 인덱스 가져오기
#idx = fruits.index("바나나")
#print(idx)

#list 리스트
#sort() : 오름차순으로 정렬
#reverse() : 리스트 요소를 제자리에서 뒤집기

# 오름차순 정령

fruits.sort()
print(fruits)

# 꺼꾸로 뒤집어서 정렬하기
fruits.reverse()
print(fruits)