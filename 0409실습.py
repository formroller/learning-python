# =============================================================================
# 0. 음식 궁합.
# =============================================================================
d1 = {'떡볶이':'튀김','짜장면':'만두','라면':'김치','피자':'콜라','치킨':'맥주','삼겹살':'소주'}
flist = set(d1)

input(f'{flist} 중 좋아하는 음식은? ')
str(flist) +'중 좋아하는 음식은?'

'치킨' in flist

while True :  # 원하는 답이 선택될때 까지 무한 반복
    ans = input(str(flist)+' 중 좋아하는 음식은?')
    if ans in flist :
        print(f'{ans} 궁합 음식은 {d1.get(ans)}입니다')
 #       print('<%s> 궁합 음식은 <%s>입니다' % (ans, d1.get(ans)))
    elif ans == '끝':
        print('프로그램 종료')
        break
    else :
        print('그런 형식이 없습니다')




value = input('[떡볶이,짜장면,라면,피자,맥주,치킨,삼겹살]중 좋아하는 음식은? ')


if value in d1:
    print('%s의 궁합음식은 %s입니다.'%(value, d1.get(value)))
elif value == '끝': 
    exit(0)
else:
    print('보기에 없습니다.')
# =============================================================================
# 1. 불규칙한 리스트의 입력과 출력
# =============================================================================

i = 1
value = 1
outlist = []

# 입력
while 1 :
    ans = input(f'{i}번째 생성할 리스트 수를 입력하세요 : ')
    if ans == 'z' :
        break
    inlist = []
    for j in range (0,int(ans)):
        inlist.append(value)
        value += 3
    outlist.append(inlist)
        
# 출력 (위치기반 or *object 기반)

for i in outlist :
    for j in i :
        print('%2d' % j, end = ' ')
    print()

# =============================================================================
#     
# =============================================================================

result = [i+j for i in range(5) for j in range(4) ]

L1 = [[1,2,3],[3,4,5],[7,8,9]]
# 출력
z = 1
for i in range(0,3):
    for j in range(0,3):
        print(z,end = ' ')
        z += 1
    print()


non = int(input('숫자 입력 : '))
outlist = []
for i in range(0,non):
    inlist = []
    for j in range(0,non):
        inlist.append(non)
        non += 1
    outlist.append(inlist)
outlist


for i in range(0,non):
    for j in range(0,non):
        print(non, end = ' ')
        non += 1
    print()

z = 1
for i in range(0,3):
    for j in range(0,3):
        print(z,end = ' ')
        z += 1
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



# =============================================================================
# 2. 계산기 프로그램 작성
# =============================================================================
print('계산기 프로그램입니다')
ans =  int(input('1. 입력한 수식 계산 \n2. 두 수 사이의 합계 \n 메뉴를 입력하세요: '))

if ans == 1 :
    ans2 = input('계산할 수식을 입력하세요: ')
    #print(f'{ans2} 결과는 {eval(ans2).1f} 입니다')
    print('%s 결과는 %.1f입니다' % (ans2, eval(ans2)))
else :
    ans3 = int(input('첫 번째 숫자를 입력하세요'))
    ans4 = int(input('두 번째 숫자를 입력하세요'))
    vsum = 0
    for i in range(ans3, ans4+1):
        vsum += i
    
    print(f'{ans3} + ... + {ans4}는 {vsum}입니다.')




import re
from pandas import Series
ans1 = re.findall("\d+",ans)
ans2 = re.findall('\D+',ans).split(',')
ans1

for i in ans1:
    for j in ans2:
        print(f'{i} {j}')
    print()
    


type(ans1)
for i in ans1:
    print(i)

eval(ans)
import pandas
dir(pandas)


# =============================================================================
# 3. 모듈이름과 함수 패턴 전달시 매칭되는 함수명 출력
# =============================================================================
def 함수명(인자1, 인자2,...) :
    본문
    return 리턴대상


import numpy
'zeros' in dir(numpy)  # 스칼라 in 리스트 , 일치여부 Ture
'ze' in dir(numpy)     # 일치여부 False
# => 포함연산자 필요
'ze' in 'zero'  # 문자 in 문자시 패턴 일치여부


def find_funct(mname, fname):
    flist= dir(mname)  # flist 함수 목록
    outlist=[]
    for func in flist : # func 함수 명
        if fname in func :  # 문자 내 같은 패턴 확인 여부
            outlist.append(func)
    return(outlist)
     

find_funct(numpy, 'na')


# =============================================================================
#  로또 생성 프로그램
# =============================================================================
import random
print('로또번호 추첨기')

lotto = []
while len(lotto) < 6 :
    v1 = random.randrange(1,47)
    if v1 in lotto :
        pass 
    else :
        lotto.append(v1)
lotto.sort()   
# print(f'추첨된 로또 번호 => {lotto}')
 
print('추첨된 로또 번호 => ', end = '')
for vno in lotto:
    print(vno, end = ' ')
    

# 난수 6개 생성, 중복허용
 test1= [random.randrange(1,47) for i in range(0,7)]; test1 

r1= random.randrange(1,47,6);



Number = []
r1= random.randrange(1,47)
for i in range(0,6):
    while r1 in Number : 
        r1= random.randrange(1,47)
        Number.append(r1)
    print(Number)











