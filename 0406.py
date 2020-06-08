# print함수
print(1)
print('%d' % 1)         # 정수형식 출력     (%d)
print('%.2f' % 10 )     # 실수 형식 출력    (%f)
print('%s' % 'abcde')   # 문자열 형식 출력  (%s)

print('%d+ %d = %d ' % (1,1,2))
print('%d더하기 %d는  %d입니다. ' % (1,1,2))


#5,8,12,13 => 05,08,12,13
to_cahr(대상,'09') # oracle
sprintf(대상,'%02d')
print('%02d'% 1)
print('%5.2f' % 10) # 10.00 5자리, 공백 삽입 없음
print('%7.2f' % 10) # 10.00 7자리, 공백(2칸) 삽입
print('%.2f' % 10)  # 10.00 총 자리수 없이 소수점만 적용한다.

# 색인, 시작은 0부터
v1= 'abcdefg'

v1[1] # 문자열 색인 가능(R에서는 불가) 
v1[1:2] # 1 ~ 2전까지 추출 (끝 범위 다음 번호 추출해야한다.)
v1[1:3]

# escape 문자
print('\')   # 출력 에러
print('\\')  # '\'를 일반 기호화 하기위해 '\'사용
print('a\nc')

#.format
#{0:d} {1:5d} {2:05d}  자릿수:포멧 전달한다.(순서변경이 가능해진다.)
print('%d %5d %05d' % (123, 123,123))
print('{0:d} {1:5d} {2:05d}'.format(123,123,123))
print('{0:d} {1:.2f} {2:s}'.format(123,123,'1000'))
print('{2:d} {0:.2f} {1:s}'.format(123,'123',1000)) # 문자를 정수로 표현 불가
 a = 'My name is {0}. I am {1} years old.'.format('Mario', 40) 
a
 
#산술연산 함수
round(1.23)
round(1.23,1)

import math
math.trunc(1.23)

dir(math) #[]여러 결과 담기 위해 list 사용
math.factorial(6)
5**2     # 제곱 연산자(**)
pow(5,2) # 제곱 연산 함수

# 문자열 사용
v1='select ename
      from emp'    # enter 삽입으로 인해 에러발생
v1='''select ename
      from emp'''  # enter 삽입시 ''' ''' 묶음

'a' + 'b' # 문자열 결합 ,'a'||'b'
          # paste('a','b',sep='') in R
          # stringr::str_c('a','b',sep='')

'a' in 'abcde' # in 문자열 포함 여부
'abcde' in 'a' # False
# =>'찾을 문자' in '찾을 문자열'

a1='abcde'
a2 = ' abc ' 
a3 = 'a;b;c'
# 1) startswith  str_detect(a,'^2')
a1.startswith(prefix, # 시작값 확인
              start,  # 검사 시작 위치(생략가능)
              end)    # 검사 끝 위치 (생략 가능)

a1.startswith('a')    # 'a'로 시작하는지 여부
a1.startswith('a',1)  # 두번째 글자가 'a'로 시작하는지 여부

# 2) endswith  str_detect(a,'2$')
a1.endswith(suffix,   # 끝 값 확인 문자열
            start,    # 검사 시작 위치(생략 가능)
            end)      # 검사 끝 위치( 생략 가능)

a1.endswith('e')
a1.endswith('e',1,3)  # a1[1:3] 'e'로 끝나는지 여부
a1.endswith('c',1,3)  # a1[1:3] 'c'로 끝나는지 여부

# 3) strip
a2.lstrip()      # (제거함수) a2왼쪽에서 공백제거
a1.lstrip('a')   # 문자 제거 가능 (중간에 있는 문자는 삭제 불가)
a2.rstrip()      # (제거함수) a2오른쪽에서 공백제거
a2.strip()       # (제거함수) 양쪽 공백 제거

# 4) replace  
a1.replace('a','A')  # a1에서 'a'를 'A'로 변환
a1.replace('a','')   # a1에서 'a' 삭제

# 5) split
a3.split(';')       # a3에서 ';'기준으로 분리
a3.split(';')[1]    # 색인 가능 

# 6) 대소치환
a1.upper()    # 대문자로 
a1.lower()    # 소문자로
a1.title()    # camel 표기법 (맨 앞글자만 대문자로) (=initcat in oracle)
a1.title(a1)

# 7) find
a1.find('a')  # a 위치
a1.find('A')  # -1 (없는대상)

# 8) count
a1.count('a')   # a1에 'a'포함된 횟수

# 9) format
'{0:d} + {1:d} = {2:.2f}'.format(1,2,3)

# 연습문제
ename = 'smith'
tel = '02)345-7839'
jumin = '901213-2224928'
vid = 'abc1234!'

#1) ename의 두번째 글자가 m으로 시작하는지 여부
ename[1]=='m'
ename.startswith('m',1)

#2) tel에서 국번(345) 출력
v1 = tel.find(')')
v2 = tel.find('-')
tel[v1+1 : v2]

tel.split(')')[1].split('-')[0]

tel[3:6]

#3) jumin에서 여자인지 여부 출력
jumin.split('-')[1][1]=='2'
jumin[7] == '2'
jumin.startswith('2',7)

#4) vid에서 '!' 포함 여부
'!' in vid
vid.find('!') != '-1'


#[참고, 주석처리]
# ctrl + 1 , 문장 주석
# =============================================================================
# ctrl + 4 , 문단 주석
# ctrl + 5 , 주석 해제
# =============================================================================


L1 = ['abc','bcd','cds']
L1.sartwith('a') # 속성에러, 리스트는 startwith 메소드를 전달할 수 없다.

input 
# - 사용자가 입력한 값 가져오기(readlines in R)
# - 문자형으로 전달

a1 = input()
a1

a1 = input('값을 입력하세요 : ') # input은 문자타입으로 전달

# 형 변환 함수
1 + '1'     # 형 불일치, 연산 불가

1 + int(1)  # int() 정수 형 변환
1 + float(1) # float() 실수 형 변환
1 + str(1)  # 문자 형 변환


# 사용자로부터 두 수를 전달받아 다음과 같은 형식으로 출력
'4 + 10 = 14입니다.'
n1 = int(input('숫자 : '))
n2 = int(input('숫자 : '))
result = int(n1) + int(n2)

print('{0} + {1} = {2}입니다.'.format(n1,n2,result))
print('%d + %d = %d입니다.'.format(n1,n2,n1+n2))


#
map
apply
applymap






















