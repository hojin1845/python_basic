#21강 dict
#dict에 카트의 물건과 각격 저장하기
#키는 품목, 값은 가격
# 키는 품목, 값은 가격 {품목:가격}
snack = {"꼬북칩":2400,"신라면":950, "김밥":3500}
print(snack)

#2. 신라면 빼고 참깨라면 추가하기
#dict에서 신라면 삭제
del snack["신라면"]
print(snack)

# dict에 참깨라면 추가
snack["참깨라면"] = 1000
print(snack)

#3.dict에서 꼬북칩 가격 변경하기
snack["꼬북칩"] = 1800
print(snack)