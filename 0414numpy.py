#[실습과제 : 아래와 같은 함수 생성]
#f_read_txt(file,sep=' ', fmt = int)
[[1,2,3,4],[5,6,7,8]]

#f_read_txt(file,sep=' ', fmt = str)
[['1','2','3','4'],['5','6','7','8']]

c1 = open('read_test1.txt') # 커서 선언, # 모드 설정 가능(r/w)

v1 = c1.readline()  # fetch

c1.close            # 메모리 정리(메모리 누수 방지)

#--
v1
fmt1 = int
fmt2 = 'int' # int가 문자열로 파싱 불가.
L1 = '1 2 3 4\n'.strip().split(' ')   # \n제거(strip)

int(['1,2,3,4'])  # 형 변환함수 리스트 적용 불가(= int는 여러 원소 받지 못한다)
int('1')          # 형 변환함수 스칼라 적용 가능

L1 = '1 2 3 4\n'.strip().split(' ')  

[int(i) for i in L1]

[fmt1(i) for i in L1]  # 함수 기능 그대로 유지된다(fmt1)
[fmt2(i) for i in L1]  # 'int'(i), str객체를 전달받을 수 없다. 문자열 가공해 실행시켜야한다
# => eval('int' + '(' +'1' + ')')

# 1. fmt 인자를 '함수명' 형태로 전달 
def f_read_txt(file, sep = ' ', fmt = int):
    c1 = open('read_test1.txt','r') # 커서선언
    v1 = c1.readlines()               # fetch
    c1.close()
    
    outlist = []
    
    for i in v1 :
        L1 = i.strip().split(sep)
        outlist.append([fmt1(i) for i in L1])
    return outlist    

f_read_txt('read_test1.txt',sep=' ', fmt = 'int')  # 불가
f_read_txt('read_test1.txt',sep=' ', fmt = int)    # 가능
f_read_txt('read_test1.txt',sep=' ', fmt = float)  # 가능

# 2. 문자열 가공후 실행.
def f_read_txt(file, sep = ' ', fmt = int):
    c1 = open('read_test1.txt','r') # 커서선언
    v1 = c1.readlines()               # fetch
    c1.close()
    
    outlist = []
    
    for i in v1 :
        L1 = i.strip().split(sep)
        outlist.append([eval (fmt2 + '(' + i + ')' )for i in L1])    # 'int' +'(' + i + ')'
        
    return outlist    

f_read_txt('read_test1.txt',sep=' ', fmt = 'int')  # 가능

# 객체를 외부 파일로 보내기
L1 = [[1,2,3,4],[5,6,7,8]]    

c1 = open('write_test.txt','w') # 쓰기모드 커서 선언
c1.writelines(L1)               # 에러 발생, 리스트 쓰기 불가
c1.close()

#--
c1 = open('write_test.txt','w')     # 쓰기모드 커서 선언
c1.writelines(str(L1))              # 리스트 그대로 저장
c1.close()

#--
c1 = open('write_test2.txt','w')  # 쓰기모드 커서 선언

for i in L1:
    c1.writelines(str(i)+'\n')         # 리스트 각각 출력
    
c1.close()
c1

#z = 1
#for i in range(0,3):
#    for j in range(0,3):
#        print(z,end = ' ')
#        z += 1
#    print()


# =============================================================================
# # numpy : 다차원 배열 생성 및 연산을 위한 패키지(모듈)
# =============================================================================
import numpy as np
##  array
# - 다차원
# - 동일한 데이터 타입만 허용
 
# 1. 생성

a1 = np.arange(1,10)  # (seq in R), 1:10 => 1 ~ 9
a2 = np.arange(1,19, dtype = 'float')
type(a1)              # numpy.ndarray (nd -> 다차원)

a3 = np.array([1,2,3,4])     # 1차원
a4 = np.array([[1,2],[3,4]]) # 2차원

# 2. 배열과 관련된 주요 메서드
a1.dtype         # 배열을 구성하는 데이터 타입
a2.dtype

a1.shape         # 다차원 배열의 사이즈 (n*n)

a1.reshape(3,3)   # 배열의 사이즈 변경
a2.reshape(2,3,3) # 2층, 3행, 3열의 배열 변경

a2.reshape(2,3,3).ndim  # .ndim -> 차원확인  
a4.ndim

#[참고 : 다차원을 나타내는 순서]
#            행 열 층 ... (R)
#      ...층 행 열        (python)


# 3. 연산
a5 = np.array([10,20,30,40]).reshape(2,2)
a6 = np.array([10,20])
a7 = np.array([10,20,30])

a4 + 1    # 스칼라 연산 가능
a4 + a5   # 서로 같은 크기 갖는 배열끼리 연산 가능
a4 + a6   # 서로 다른 크기 갖는 배열 연산 가능
a4 + a7   # (2,2) + (3,) => (2,2) + (1,3)하나의 행만 갖는다.

## broadcast : 배열의 반복 연산
# 1) 양쪽 배열에 크기를 나타내는 숫자가 동일해야한다.[(a1,a2) + (b1,b2), a1=b1 or a2=b2]
# 2) 작은쪽 배열의 크기를 나타내는 나머지 숫자는 반드시 1이 된다. (ex) 2*2 + 2*1
# 3) 같은 크기를 나타내는 숫자는 반드시 같은 위치에 있어야한다.

arr1 = np.arange(1,9).reshape(2,4)  # 2*4
arr2 = np.array([10,20])            # 1*2
arr3 = np.array([10,20,30,40])      # 1*4

arr1 + arr2                # 연산 불가 (2*4) + (1*2) [조건3에 위배]
arr1 + arr2.reshape(2,1)   # 연산 가능 (2*4) + (2*1)
arr1 + arr3                # 연산 가능 (2*4) + (1*4)


#[연습문제]#
# 아래 배열이 연산 가능하도록 만들어라
a10 = np.arange(1,25).reshape(2,3,4)
a20 = np.arange(1,13)
a30 = np.array([10,20,30])

#1) a10 + a20
a10 + a20.reshape(3,4)

#2) a10 + a30
a10 + a30.reshape(1,3,1)

# 4. 색인
L1= [[1,2,3],[4,5,6],[7,8,9]]
arr1 = np.array(L1)
arr2 = np.arange(1,25).reshape(2,3,4)

L1[1,1]      # 불가
L1[1][1]     # 가능

arr1[1,1]    # 원소 색인
arr1[0,:]    # 첫번째 행 추출, 컬럼범위 생략 가능
arr1[:,0]    # 첫번째 컬럼 추출, 행범위 생략 불가
arr1[:,0:1]  # 첫번째 컬럼 추출,(차원축소 방지, drop=F in R)


arr1[[0,2],:] # 리스트를 색인값으로 전달 가능 (벡터색인)
arr1[1:3,:]   # 슬라이스 객체를 색인값으로 전달 가능

#예제) arr1에서 5,6,8,9 추출
arr1[[1,2],[1,2]]          # 불가 / 5,9 => p(1,1), p(2,2)  포인트로 해석
 
arr1[1:3,1:3]              # 가능
arr1[[1,2],1:3]            # 가능
arr1[np.ix_([1,2],[1,2])]  # nu.ix_ 위치값으로 전환
arr1[[1,2],:][:,[1,2]]     # 가능

#예제2) 4,7 출력
arr1
arr1[[1,2],0]        # 가능
arr1[[1,2],:][:,0]   # 가능
arr1[:,0][[1,2],:]   # 불가, 앞의 차원에 따라 뒤의 차원도 같아야한다.
arr1[:,0][[1,2]]     # 가능
arr1[1:3,0:1]

 
#예제) 다음의 arr2에서 
arr2 = np.arange(1,21).reshape(5,4)

#1) 10,11,14,15,18,19 출력
arr2[2:5,1:3]
arr2[np.ix_([2,3,4],[1,2])]
arr2[[2,3,4],:][:,[1,2]]

#2)6,7,8 출력
arr2[1,1:4]
arr2[1,[1,2,3]]

#예제) 다음의 arr3에서 첫번째 컬럼값을 추출, 각 컬럼마다 값을 더해 출력
arr3 = np.arange(1,10).reshape(3,3)

arr3 + arr3[:,0:1]

 

    



































