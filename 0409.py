# 중첩 for문을 이용한 리스트의 입출력

L1 = [[1,2,3],[3,4,5],[7,8,9]]

# 위치기반(출력)
for i in range(0,len(L1)):
    for j in range(0,len(L1[i])):
        print(L1[i][j], end = ' ')
    print()
   
# 입력    
z = 1;outlist=[]
for i in range(0,3):
    inlist = []        #초기화 시키기 위해 빈 리스트 내부에 삽입
    for j in range(0,3):
        inlist.append(z)
        z += 1
    outlist.append(inlist)
outlist
 
# 출력
z = 1
for i in range(0,3):
    for j in range(0,3):
        print(z,end = ' ')
        z += 1
    print()
    

i inlist j outlist

# 예제 0부터 3씩 증가하는 4x5 형태의 중첩 리스트 출력
# - 왜 입력과 출력이 나눠진건가
# 밖에 빈 리스트 생성하면 안에 생긴 리스트에 

list1=[]
list2=[]
value = 1

for i in range(0,3):
    for j in range(0,3):
        list1.append(value)
        value += 3
    list2.append(list1)
    list1=[]            # 주석처리 유무로 차이 확인(내부 리스트없으면 분리 되지 않는다.)
#                          => inlist초기화(123 끝나고 초기화, 이후 값(456) 삽입)
list2
# 내부리스트 초기화 없을경우
[1,2,3]
[[1,2,3]]
[4,5,6]

list1=[]
list2=[]
value = 0

for i in range(0,4):
    for j in range(0,5):
        list1.append(value)
        value += 3
    list2.append(list1)
    list1=[]            # inlist 초기화1
list2



# 입력[] 형태
z=0;outlist=[]
for i in range(0,4):
    inlist=[]  
    for j in range(0,5):
        inlist.append(z)
        z += 3
    outlist.append(inlist)  
outlist

#출력.
z = 0
for i in range(0,4):
    for j in range(0,5):
        print('%2d'%z, end = ' ')
        z +=3
    print()


# =============================================================================
# 불규칙한 리스트 만드는 프로그램 작성(과제)
# =============================================================================

## 튜플 ()
# - 읽기 전용 리스트
# - 리스트와 동일한 자료구조(1차원, 서로 다른 데이터 타입 허용)
# - 수정불가(읽기 전용)
# - 수정되면 안되는 참조용 생성시 필요
# - 소괄호() 또는 쉼표, 로 생성
    
## 1. 생성
t1 = (1,2,3) ; t1
t2 = 1,2,3   ; t2
t3 = (10,)   ; t3
t4 = (10)    ; t4

type(t1)  # tuple
type(t2)  # tuple
type(t3)  # tuple
type(t4)  # int

# 참고
a1,a2,a3 = 1,2,3  # 각 변수에 1,2,3 각각 삽입

## 2. 수정
t1[0] = 10 # 'tuple' object does not support item assignment
t1.append(11) # 불가
del(t1[0])    # 삭제 불가
del(t1)       # 전체 삭제는 가능

## 딕셔너리
# - R에서의 리스트와 비슷
# - key : value 형식
# - Series, Dataframe의 기본 구조

## 1. 생성
d1 = {'a':1, 'b':2}
d2 = {'a':[1,2], 'b':[3,4]}
type(d1) # dict

## 2. 색인 
# - key색인 가능
d1['a']
d1.get('a') # 색인 메서드

## 3. 수정
d1['b'] = 22
d1['c'] = 3  # 없는 값도 전달 가능

## 4. 삭제
del(d1['c'])
d1['b'] = NA  # from numpy import nan as NA, nan으로 표시된다.

#[참고 - R에서의 NULL, NA 표현식 대]
from numpy import nan as NA

## 5. 딕셔너리 키 출력
set(d1)

#[참고 - dict와 Seires, Dataframe 관계]
from pandas import Series
from pandas import DataFrame

Series(d1)    # dict의 키가 인덱스로 변환
DataFrame(d2) # dict의 키가 컬럼으로 변환 

Series([1,2,3]) # 인덱스 값 전달받을 대상(key) 없으므로 0 1 2로 표시
DataFrame({'a' :[1,2,3], 'b':[4,5,6]}) # DF로 전달시 {} 묶음

#연습) 다음의 리스트와 딕셔너리를 참고해 전화번호를 완성, 02)345-4958
l1 = ['345-4958','334-0948','394-9050','473-3853']
l2 = ['서울','경기','부산','제주']
area_no = {'서울':'02', '경기':'031','부산':'051','제주':'054'}

'02' + ')' + l1[0]
area_no.get(l2[0]) + ')' +l1[0]
area_no.get(l2[1]) + ')' +l1[1]
area_no.get(l2[2]) + ')' +l1[2]

f1 = lambda x, y : area_no.get(y) + ')' + x
list(map(f1,l1,l2))

tel = []
for i in l1:
    
    for j in l2:
        print('%s)%s' % (area_no.get(j),i))


 
d1 = {'떡볶이':'튀김','짜장면':'만두','라면':'김치','피자':'콜라','치킨':'맥주','삼겹살':'소주'}
value = input('[떡볶이,짜장면,라면,피자,맥주,치킨,삼겹살]중 좋아하는 음식은? ')


if value in d1:
    print('%s의 궁합음식은 %s입니다.'%(value, d1.get(value)))
elif value == '끝': 
    exit(0)
else:
    print('보기에 없습니다.')
        







## 2. 색인 
# - key색인 가능
d1['a']
d1.get('a') # 색인 메서드



