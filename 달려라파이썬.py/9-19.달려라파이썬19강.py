#연습문제
#1. 2학년 3반 학생 리스트
members = ['유재석', '지석진', '김종국', '양세형', '하하', '송지효', '이광수', '전소민','양세찬']
print(members)

#2. 전학 간 양세형
members.remove("양세형")
print(members)

# 전학 온 송지효 추가
members.append("송지효")
print(members)

#3. 송지효 학생 몇명인지 구하기
count = members.count("송지효")
print(count)

#4. 학생 리스트 오름차순 졍렬
members.sort()
print(members)