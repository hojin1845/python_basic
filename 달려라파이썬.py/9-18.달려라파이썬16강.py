#자료형 (1) 연습문제

#친구들이 좋아하는 스포츠 리스
sports = ["축구","수영","야구","농구","축구","댄스"]
print(sports)

#2.리스트 값 변경
sports[2] = "달리기" # 야구 ==> 달리기로 변경
print(sports)

#3. 리스트 값 삭제
del sports[4]   # 중복값 축구 삭제
print(sports)

#4.리스트의 길이 구하기
count = len(sports) # 스포츠의  종류 갯수
print(count)