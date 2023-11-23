name="모범생"
score1, score2 = 90, 98
avg=(score1+score2)/2

print("**형식지정문자와 format 형식 출력하기**")
#%형식지정문자 중 문자열과 정수를 사용하기
print("%s님 컴사의 중간과 기말 성적은 각각 %d,%03d입니다." %(name,score1, score2))
#형식지정문자 중 문자열과 실수를 사용하기
print("%s님 컴사 과목 시험 평균은 %6.2f 입니다." %(name, avg))

#format형식을 이용해 표현하기
print("{}님의 컴사 중간과 기말 성적은 각각 {},{}입니다.".format(name,score1,score2))
print("{0}님의 컴사 중간과 기말 성적은 각각 {1},{2}입니다.".format(name,score1,score2))

print("{0}님 컴사 과목 시험 평균은 {1}입니다.".format(name,avg))
