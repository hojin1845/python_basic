#12강 인덱스
#indexing(인덱싱) : 문자열[index] : game = "브롤스타즈"
#브 : 0 롤 : 1 스 : 2 타 : 3 즈 : 4

# 인덱싱하기
#game = "브롤스타즈"
#print(game)
#print(game[0], game[1], game[2], game[3], game[-1])

#print(game[5]) (o) : 인덱스는 리스트와 같이 자료형에도 많이 사용
#slicing (슬라이싱) 문자열[시작위치:끝위치] : game = "브롤스타즈"
#내가 롤스 을 출력하고 싶다면 game[1:3]
# 슬라이싱 하기
# "롤스"
#print(game[1:3])

# "브롤"
#print(game[:2])

# "스타즈"
#print(game[2:])

#연습문제
# 토끼고양이강아지물고기
animal = "토끼고양이강아지물고기"

rabbit = animal[0:2]
cat = animal[2:5]
dog = animal[5:8]
fish = animal[8:]

print(rabbit)
print(cat)
print(dog)
print(fish)