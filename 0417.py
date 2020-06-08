import numpy as np
# deep copy
arr1 = np.arange(1,10)
arr2 = arr1[0:5]        # 슬라이스 객체는 deep copy 발생 X
arr1[0] = 10
arr2                    # arr2도 같이 변경된다.


arr3 = arr1[0:5].copy()  # deep copy 발생, 완전한 백업
arr1[1] = 20
arr1
arr2
arr3

## 조건 색인 (boolean indexing)
# - 리스트에서는 불가
L1 = [1,2,3,4,5]
L1 > 3  # 불가 
L1[[True,False,False,False,False]]

# - array 조건 색인 가능
arr1 = np.arange(1,10).reshape(3,3)
arr1[arr1 > 5]

# 예제 )세번째 컬럼의 값이 6인 행 선택
arr1[:,2] == 6
arr1[arr1[:,2] == 6,:]

# 예제 )세번째 컬럼의 값이 6이 아닌 행 선택(조건의 부정)
arr1[:,2] != 6
arr1[arr1[:,2] != 6,:]
arr1[~(arr1[:,2] == 6),:]  # not 연산자는 ~ 기호로 표시 가능



## np.where
#- 조건의 벡터연산
#- R의 ifelse 구문과 비슷
# - 조건에 대한 단순 리턴만 가능

#예제) 다음의 배열에서 5보다 크면'A', 작거나 같으면 'B'리턴
arr3 = np.arange(1,10)
np.where(arr3 >5,'A','B')

#연습문제)
#1)emp.csv파일의 부선번호를 사용, 부서 이름 출력
#  10: 인사부 20: 총부무 30 : 재무부
L1 = f_read_txt('emp.csv' , sep = ',' , fmt = str)
import numpy as np
arr1 = np.array(L1)
arr1 = arr1[1:,]
arr1[:,7]

np.where(arr1[:,-1] =='10','인사부', np.where(arr1[:,-1]=='20','총무부','재무부'))


#2) 1 - 25, 5*5 배열 생성 후 짝수는 그대로, 홀수는 0으로 치환
arr2 = np.arange(1,26).reshape(5,5)
np.where(arr2 % 2 == 0,arr2, 0)

## 전치 메서드
#1) T : 행열 전치
arr2
arr2.T
#2) transpose : 축번호 전달, 원하는 축의 이동, 축번호 전달 순서 중요 (위치대로 전달)
arr2.transpose(0,1) # 변화 없다.
arr2.transpose(1,0) # 열,행 형태로 전환

#3) swapaxes : 2개의 축 번호를 전달, 원하는 두 축의 전치, 축번호 전달 순서 중요하지 않음.
arr2.swapaxes(0,1) # 행열 전치
arr2.swapaxes(1,0) # 행열 전치 

#[연습문제] 시험범위!!
#2*3*4 배열에서 층과 행 바꾸어 출력 =>3층, 2행 4열
arr3 = np.arange(1,25).reshape(2,3,4)
arr3.swapaxes(0,1)
arr3.transpose(1,0,2)
arr3.reshape(3,2,4)

## 누적합, 누적곱 연산
arr2.cumsum(axis = 0) # axis 0, 세로방향
arr2.cumsum(axis = 1) # axis 1, 가로방향

arr2.cumprod(axis = 0) 
arr2.cumprod(axis = 1)

## 최대/최소 연산
arr2.min(axis = 0)
arr2.max(axis = 0)

arr2.argmin(axis = 0)  # 최소를 갖는 포지션 출력, (whichmin in R)
arr2.argmax(axis = 1)  # 최대를 갖는 포지션 출력, (whichmax in R)

## 불리언 배열 메서드
(arr2 > 10).sum()  # 조건에 만족하는 값의 갯수
(arr2 > 10).any()  # 조건을 만족하는 값이 하나라도 있는지 여부
(arr2 > 10).all()  # 모든 값이 조건을 만족하는지 여부


#[연습 문제]
#다음의 구조를 갖는 array 생성
#1     500     5
#2     200     2
#3     200     7
#4      50     9

l1 = np.array([[1,2,3,4],[500,200,200,50],[5,2,7,9]])
l2 = l1.swapaxes(0,1)

#1) 위 배열에서 두번째 컬럼값이 300 이상인 행 선택
l2[l2[:,1] > 300,:]

#2) 세번째 컬럼 값이 최댓값인 행 선택
l2[l2[:,2].argmax(),:]

## sort : 정렬
arr2.sort(axis = 0)

arr3 = np.array([[3,1,4,15,2],
                 [6,7,8,1,2]])
arr3.sort(axis = 1)

## 집합 연산자 [1(숫자)d]
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])

#1. union1d      : 합집합
np.union1d(arr1,arr2)

#2. intersect1d  : 교집합
np.intersect1d(arr1,arr2)

#3. setdiff1d    : 차집합
np.setdiff1d(arr1,arr2)

#4. in1d         : 포함연산자
np.in1d(arr1,[1,2])
np.in1d(arr1,arr2)

#5. setxor1d : 대칭 차집합 => (A-B) U (B-A)
np.setxor1d(arr1,arr2)

#6. unique
np.unique(np.array([1,1,1,2]))

#[연습문제]
#1 - 25의 값을 갖는 5*5 배열을 생성 후 2의 배수와 3의 배수를 추출
a1 = np.arange(1,26).reshape(5,5)

a2 = a1[a1 % 2 == 0]
a3 = a1[a1 % 3 == 0]

a1[np.in1d(a1,np.union1d(a2,a3))]  # 1차원이기 때문에 에러 발생
a1[np.in1d(a1,np.union1d(a2,a3)).reshape(5,5)]

## [참고 : reshape 시 배열 순서]
# 'C' 순서 : 행 우선 순위
# 'F' 순서 : 컬럼 우선 순위

a1 = np.arange(1,10)
a1.reshape(3,3,order = 'C') # C순서가 기본값
a1.reshape(3,3,order = 'F')

1) 행 우선순위 ('C'순서)
123
456
789

2) 열 우선순위 ('F'순서)
147
258
369
