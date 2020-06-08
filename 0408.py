# 리스트 in R
v1 <- c(1,2,3,4)
v1[c(1,3)]      # 벡터색인 가능
v1[v1 < 2]      # 조건색인 가능

# 리스트 in python
L1 = [1,2,3,4,5]
L1[1:4]           # 슬라이스 색인
L1[[1,3]]         # 벡터 색인 (여러값을 묶어 색인값으로 전달)
L1==2             # 비교연산 불가
L1 + 2            # 연산 불가

list(map(lambda x : x < 2, L1))  # (T/F 만 출력) map 함수 사용해 각 원소별 비교
L1[list(map(lambda x : x < 2, L1))] # 조건색인 불가 (조건의 결과를 갖는 리스트를 색인값으로 전달받을 수 없다.)

# Series in Python
# -  => DF에 컬럼을 구성하는 요소(같은 타입만 허용)
# => Series에 문자열 처리(split, replace...) 직접 적용 불가
from pandas import Series  # Series()
s1 = Series([1,2,3,4,5])

s1[[1,3]]  # 벡터 색인 가능 (= 여러개 묶어서 색인)
s1 < 2     # 조건 전달 가능
s1[s1<4]   # 조건 색인 가능 
s1 + 1     # 벡터연산 가능

#s1.mean()
#np.mean()
#pd.mean()

#import pandas
# # 모듈 내 함수 여부 확인 (모듈관리) - 추후 과제
#dir(pandas) # 출력 결과가 리스트이다.

# 리스트 주요 메서드
L1 = [1,2,3,4,5]
L2 = [1,5,2,3,4]
L1
L1.append(6) ; L1    # 원소 추가 (값이 들어간다)
L1.extend([7]) ; L1  # 원소 추가 (List 확장으로 추가된다)
L1.insert(0,10); L1  # 0번째 위치에 10 삽입

L1.remove(3) ; L1  # 특정 원소 삭제
L1.pop(); L1       # 마지막 원소 삭제

L1.count(1)        # 원소 포함 횟수

L1.index(4)        # 원소 위치
L1.index(3)        # 원소에 값이 없을 경우 에러 출력  / find, 없을경우 -1 출력
 

L2.sort(reverse=False) ;L2 # 정렬된 결과 추출, 즉시 반영

len(L1)   # 리스트 사이즈 (원소 갯수)

# for문 
for i in range(0,6) : 
    print(i)

for i in range(0,6,2) :
    print(i)
    
for i in L1 : 
    print(i)

for i in L1 :
    print(i, end ='') #print의 end값 없으므로 일렬로 출력
    
# (연습) 
#jumin = ['8812111223928','8905042323343','90050612343432'] 에서
#각 성별을 나타내는 숫자를 추출(for문 사용)
jumin = ['8812111223928','8905042323343','90050612343432']

L2 = []
for i in jumin: 
    L2.append(i[6])
L2

for i in jumin:
    print(i[6])

연습) 2 - 300, 3씩 증가시키는 값의 합계 구하기
v1 = int(input('시작값: '))
v2 = int(input('끝 값 : '))
v3 = int(input('증가값 : '))

vsum = 0
for i in range(v1,v2+1,v3) :
    vsum += i
    
print('%d에서 %d까지 %d씩 증가시킨 값의 합 : %d' % (v1,v2,v3,vsum)
vsum = [v1+v3 for v1 in  range(v2+1)]
vsum
# 중첩 for문
L1 = [1,2,3]
L2 = [[1,2,3],[4,8,45],[71,80,19]]

for i in L1 :
    print(i, end = ' ')

for i in L2 :
    print(i, end = ' ')

for i in L2 :
    for j in i:              # 1. 리스트를 묶은 i(1,2,3) j에 할당 (4.반복)
        print(j, end = ' ')  # 2. 원소 분리 , => ' '
    print()    # for문 끝난 다음 출력 3.줄바꿈

 # 위치값 기반
for i in range(0,3):
    for j in range(0,3) : 
        print(L2[i][j], end = ' ')
    print()

#연습) 불규칙한 리스트의 2차원 형식 출력
L3 = [[1,2],[1,2,3],[4,5,6]]

for i in L3:
    for j in i:
        print(j, end = ' ')
    print()
 # 위치기반
for i in range(0,len(L3)) :
    for j in range(0,len(L3[i])):
        print(L3[i][j], end = ' ')
    print()

for i in L3:
    for j in i:
        print(j, end = ' ')
    print()

# while 문
i=0
while i < 11:
    print(i)
    i = i + 1

# 유니코드
print('\u2605'*3)
print('\u260E')


# if 문
for i in L1 :
    if i > 3 :
        print(i)

# (연습문제, 1-100까지 짝수 합 출력) 
 # 1. 기본 while 구문
vsum = 0; i = 1
while i < 101:
    if i % 2 == 0:
        vsum += i
    i += 1
print(vsum)

 # 2. continue구문
vsum = 0; i = 0
while i < 101:
    i += 1
    if i % 2 != 0:
        continue   # R에서의 next구문과 동일
    vsum += i
print(vsum)

i = 0
while i < 101:
   if i % 2 == 0:
       print(i)
       i += 1
        
 
vsum = 0
for i in range(1,101):
    if i % 2 == 0:
        vsum +=  i
print(vsum)
    
# 반복 제어문 : break, continue

#구구단)

for i in range(2,10):
    for j in range(1,10):
        print('{} x {} = {}'.format(i,j,i*j))
    print()
    


    
    
    
    