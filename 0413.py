part1. :
    2  : numpy + pandas

# 전역변수 선언(global,  v1 <<- 1 in r)

def f1() :
    v1 = 1
    print(v1)
    
def f2():
    print(v1)


v1 = 10
f1()    # 1 리턴, 함수 내부 선언앖이 더 우선순위
f2()    # 10 리턴, v1이 전역변수 선언되어 있으므로

# 지역변수
def f1() :
    v2 = 1
    print(v2)
    
def f2():
    print(v2)

f1()  # 1
f2()  # name 'v2' is not defined

# 전역변수 선언(global)
def f1() :
    global v2 # 전역변수 선언
    v2 = 1
    print(v2)
    
def f2():
    print(v2)
f1()
f2() 


## 매개변수 전달 방식
#1) * : 가변형 인자 전달 방식, 내부 반복문 필요 (... in R)
def f1(*para) :
    for i in para :
        print(i)

f1(1,2,3,4)

#예제) 함수에 입력된 모든 값의 곱을 출력하는 함수 생성

def f2(*para) :
    result = 1
    for i in para:
        result *=  i
    return result
f2(2,4,6,8)

#2) ** : key - vlaue 인자 전달 방식, 내부 반복문 필요 (... in R)
#para가 dict형식으로 전달된다.
d1 = {'a':1,'b':2,'c':3}
d1.get('a')
d1['a']    # 딕셔너리 key값으로만 구성된 오브젝트 형식
d1.keys()  # 딕셔너리 key값으로만 구성된 오브젝트 형식, 딕셔너리 형태 유지

def f3 (**para):
    for i in para.keys():
        print(f'{i}의 값은 {para[i]}입니다.')

f3(a=1, b=2, c=3)

#3) zip : 동시에 변수를 묶어 전달시 필요
fsum(v1,v2)

def fsum(v1,v2):
    result = []
    for i,j in zip(v1,v2):
        result.append(i+j)
    return result

fsum([1,2,3],[10,20,30])

# 모듈의 생성
# - 모듈 : 함수의 묶음 (패키지 in R)

#정의된 여러개의 함수를 하나의 파이썬 파일(.py)에 저장하면 하나의 모듈 생성됨.

#(연습문제)
#두 수를 전달받아 두 수의 곱을 구하여 리스트에 저장하고
# 숫자가 큰 순서대로 정렬하는 사용자 정의함수 생성.
# 단, 사용자 정의함수에 두 수 이외의 reverse라는 키워드 인자를 입력받도록 하자

fprod(L1,L2,revserse = True)
L1 = [1,2,3,4]
L2 = [10,20,30,40]

def fprod(x,y,**para):
    result = []
    for i, j in zip(x,y):
        result.append(i*j)
    result.sort(reverse=para['reverse'])
    return result

fprod(L1,L2,reverse = True)


def mul1 (v1,v2, reverse = True):
    result = []
    for i,j in zip(v1,v2):
        result.append(i*j)
    return (result)

mul1([1,2,3], [10,20,30])

# 외부파일 불러오기
1. open  : 파일을 열어 메모리상으로 불러오는 작업
2. fetch : 선언된 cursor(임시메모리 공간)에 저장된 data를 한 건씩 불러오기
3. close : 객체 선언 완료 후 cursor에 할당된 메모리 영역 close
           cursor 닫지 않으면 메모리 누수 현상이 발생할 수 있으므로 주의

c1 = open('read_test1.txt') # 커서 선언

v1 = c1.readline()  # readline 한 줄씩 가져온다
print(v1)

v2 = c1.readline()
print(v2)

c1.close()

#--
c1 = open('read_test1.txt') # 커서 선언

while 1 :
    v1=c1.readline()
    if v1 =='':
        break
    print(v1, end = '')
    
c1.close()

#--

c1 = open('read_test1.txt') # 커서 선언
c1 = open('read_test1.txt','r')  # 모드 설정 가능(r/w)

outlist = []
while 1 :
    v1=c1.readline()
    if v1 =='':
        break
    outlist.append(v1)
    
c1.close()

outlist

# readlines 전체 불러온다.
c1= open('read_test1.txt')
 v1= c1.readlines()
c1.close()
v1
 
#[실습과제 : 아래와 같은 함수 생성]
f_read_txt(file,sep=' ', fmt = int)
[[1,2,3,4],[5,6,7,8]]

f_read_txt(file,sep=' ', fmt = str)
[['1','2','3','4'],['5','6','7','8']]

c1 = open('read_test1.txt') # 커서 선언, # 모드 설정 가능(r/w)

v1 = c1.readline()  # fetch

c1.close            # 메모리 정리(메모리 누수 방지)

#--
v1

'1 2 3 4\n'.strip().split(' ')   # \n제거(strip)





