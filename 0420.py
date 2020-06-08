import numpy as np

# NA
from numpy import nan as NA
np.nan                      # R 에서의 NA와 비슷하나 실수형 자료

arr1 = np.array([1,2,3,4])
arr1[0] = NA                # 수정 불가 / array 내부 데이터는 정수로 NA(실수) 넣을 수 없어 오류

float (arr1)  # 스칼라만 허용하는 함수 -> mapping처리 필요

# 시험문제
list(map(lambda x : float(x), arr1)) 
arr1 = arr1.astype('float')
arr1[0] = NA                # 수정 가능 -> 내부 데이터 타입이 실수이기때문에

# NA 확인
np.isnan(arr1).any()
np.isnan(arr1).sum()

# array입출력

np.loadtxt(fname,         # 파일명
           dtype,         # 데이터 형식
           delimiter,     # 분리구분기호
           skiprows,      # skip할 행 (스킵할 로우 갯수, 1부터 시작)
           usecols)       # 불러올 컬럼 (컬럼 번호, 0부터 시작)

np.loadtxt('test1.txt', dtype='str', delimiter = ':', skiprows = 2, usecols = [0])

np.savetxt(fname,         # 파일명
           X,             # 저장할 객체
           delimiter,     # 분리구분기호
           fmt = '%.2f')  # 출력할 포맷

#[참고 : profile 만들기]
# 파이썬 실행시 기본으로 불러와야 할 모듈을 .py 파일로 생성, 
# 'run file명'을 통해 모듈을 동시 호출 

run profile1       # profile1.py 파일이 실행
Series([1,2,3,4])

#[연습문제]
# 1. 1부터 증가하는 3 X 4 X 5 배열 생성 후
arr1 = np.arange(1,3*4*5+1).reshape(3,4,5)
a1= np.arange(1,61).reshape(3,4,5)

# 1) 모든 값에 짝수는 *2를 홀수는 *3을 연산하여 출력
np.where(a1 % 2 == 0,a1*2,a1*3)

# 2) 각 층의 첫번째 세번째 행의 두번째 네번째 컬럼 선택하여 NA로 치환
a1 = a1.astype('float')

a1[np.ix_([0,1,2],[0,2],[1,3])] = NA
a1[:,[0,2],:][:,:,[1,3]] = NA        # 중복 색인된 결과는 수정 불가


# 3) 위의 수정된 배열에서 NA의 갯수 확인
np.isnan(a1).sum()

# 4) 층별 누적합 확인
a1.cumsum(axis = 0)


# 2. emp.csv 파일을 array 형식으로 불러온 뒤 다음 수행(컬럼명은 제외)
emp = np.loadtxt('emp.csv', dtype='str', delimiter = ',', skiprows = 1)

# 1) 이름이 smith와 allen의 이름, 부서번호, 연봉 출력
emp[:,1] in ['SMITH','ALLEN'] # 불가

# sol1) in 연산자
'SMITH' in ['SMITH','ALLEN']  # 가능 ,벡터연산 불가, mapping 필요

vbool = list(map(lambda x : x in['SMITH','ALLEN'],emp[:,1]))
emp[np.ix_(vbool,[1,-1,-3])]

# sol2) in1d 연산자
vbool2 = np.in1d(emp[:,1],['SMITH','ALLEN'])  # 벡터연산 가능한 포함연산자
emp[np.ix_(vbool2,[1,-1,-3])]


# 2) deptno가 30번 직원의 comm의 총 합
emp[:,-2]= np.where(emp[:,-2]=='','0',emp[:,-2])

(emp[emp[:,-1] =='30',-2]).astype(int).sum()
