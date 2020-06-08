import numpy as np
# asarray
# - array로의 형 변환 함수
# - 얕은 복사 수행(deep copy 발생X)

L1 = [1,2,3,4]
arr1 = np.array(L1)
arr2 = np.array(arr1, dtype = 'float')
arr3 = np.asarray(arr1, dtype = 'float') # 기존데이터의 형변환시 새로운 객체로 생성

arr1[0] = 10
arr2           # 변경X, deep copy 발생O
arr3           # 변경X, deep copy 발생O
#arr2,3은 기존 1과 타입이 다르기때문에(분리됨) deep copy 수행 => 별도의 객체


# 같은 데이터 타입을 갖는 배열 재생성
L1 = [1,2,3,4]
arr1 = np.array(L1)
arr2 = np.array(arr1)
arr3 = np.asarray(arr1)

arr1[0] = 10  
arr2          # 변경X, deep copy 발생 O
arr3          # 변경O, deep copy 생성 X


#1) 형변환 함수(벡터연산 불가)
arr1.astype('float')

#예제) 다음의 배열의 타입을 실수로 변경
arr1 = np.array([1,2,3,4])
float(arr1)                           # 불가
list(map(lambda x : float(x), arr1))  # mapping 처리 필요
# float, 함수형식 형 변환 함수는 여러개가 올 수 없다.(=스칼라만 올 수 있다.)

#2) 형변환 메서드 사용(벡터연산 가능)
arr1.astype('float')
# astype는 array 이상 가능

#[연습문제 : 다음의 값에서 10% 인상된 값 출력]
arr2 = np.array(['1,100','2,200','3,300'])

f2 = lambda x : int(x.replace(',',''))*1.1            # 가능
f3 = lambda x : x.replace(',','').astype('int')*1.1 # 불가

list(map(f2,arr2))
list(map(f3,arr3))  # 속성에러,  문자열에 astype메서드 호출불가

[int(i.replace(',',''))*1.1 for i in arr2]

# 산술연산 함수 및 메서드
arr1 = np.arange(1,10).reshape(3,3)

arr1.sum()  # 합
arr1.mean() # 평균
arr1.var()  # 분산
arr1.std()  # 표준편차

np.sum(arr1)
np.mean(arr1)
np.var(arr1)
np.std(arr1)

np.sum(arr1,axis=0) # axis =>(서로다른) 행별 총 합(컬럼 합), array([12,15,18])
#=> 컬럼 고정, 서로다른 행끼리 묶어라 ( 0 -> 세로방향)


#[참고 : 축 번호 ]
in python
 층  행  열
     0   1   # 2차원
 0   1   2   # 3차원  


in R 
 행  열  층
 1   2       # 2차원
 1   2   3   # 3차원
 
# [참고 : 축 방향]
# 행 별 : 서로 다른 행끼리 묶어 고정, 컬럼 고정 (in python)
# 열 별 : 서로 같은 행끼리 묶어 고정, 컬럼 고정(in R)

#예제)
arr3 = np.arange(1,25).reshape(2,3,4)
np.sum(arr3,axis = 0)  # axis = 0, 층 별 
arr3.sum(axis = 0)

#(연습문제)
#다음의 배열에서 각 행/열별 총합, 평균, 분산을 구하여라
#단, 분산은 분산함수를 사용하지 않고 직접 구하여라
arr4 = np.arange(1,10).reshape(3,3)

arr4.sum(axis = 0) # array([12, 15, 18])
arr4.sum(axis = 1) # array([6, 15, 24])

arr4.mean(axis = 0) # array([4, 5, 6])
arr4.mean(axis = 1) # array([2, 5, 8])

np.mean((arr4 - arr4.mean(axis = 0))**2, axis = 0)

np.mean((arr4 - arr4.mean(axis = 1).reshape(3,1))**2, axis = 1
np.mean((arr4 - arr4.mean(axis = 1))**2, axis = 1)

np.var(arr4, axis = 0)  # 행 분산
np.var(arr4, axis = 1)  # 열 분산


#[참고 = pandas에서의 분산 / 표준편차 계산식]
from pandas import DataFrame
df1 = DataFrame(arr4)
df1.var(axis = 0)  # pandas에서의 분산은 편차제곱의 합/(n-1)로 계산
df1.var(axis = 1)  #                     편차제곱의 합 / (n- ddof)

df1.var(axis = 0, ddof = 0)  # ddof를 0으로하여 편차제곱의 합/(n)으로 계산
df1.var(axis = 1, ddof)      #                   numpy에서의 분산식과 동일

df1.var?
ddof , 자유도 : 추정된 값의 모수 갯수
numpy var = /n
pandas var = /n-1

#[참고 - 분산 구하는 식]
#분산 = 편차(y-ybar)제곱의 평균

1,2,3
1-2 실제값 - 평균 (편차)
((1-2)**2 + (2-2)**2 + (3-2)**2)/3 

#[행 별]
a1= ((i-i.mean())**2+(i-i.mean())**2+ (i-i.mean())**2/)i.mean()
[a1 for i in arr4]
    
    
arr4.sum(axis = 0) 
arr4.mean(axis = 0)
((1-4)**2  + (4-4)**2 + (7-4)**2/3) # 12.0
((2-5)**2  + (5-5)**2 + (8-5)**2/3) # 12.0
((3-6)**2 + (6-6)**2 + (9-6)**2/3)  # 12.0
arr4. var(axis = 0)    # 6., 6., 6.

#[열 별]
arr4.sum(axis = 1)
arr4.mean(axis = 1)
((1-2)**2 + (2-2)**2 + (3-2)**2/3) # 1.33
((4-5)**2 + (5-5)**2 + (6-5)**2/3) # 1.33
((7-8)**2 + (8-8)**2 + (9-8)**2 /3)# 1.33
arr4.var(axis = 1)  # 0.67, 0.67, 0.67
















