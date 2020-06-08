run profile1

df1 = DataFrame(np.arange(1,13).reshape(4,3))
df2 = DataFrame(np.arange(13,19).reshape(2,3))
df3 = DataFrame(np.arange(10,90,10).reshape(4,2))

# 5. 구조 수정
# 1) row 추가
df1.append(df2)
df1.append(df2, ignore_index=True)

# 2) column 추가
df1['a'] = [11,21,31,41]

# 6. 산술연산
df1.columns = ['a','b','c','d']
df3.columns = ['a','b']

df1 + df3    # 서로 같은 컬럼끼리 연산됌(키 불일치는 NA 리턴)

df4 = DataFrame(np.array([100,101,102]).reshape(1,3))
df2 + df4    # 서로 같은 인덱스끼리 연산됌(키 불일치는 NA 리턴)

# 산술연산 메서드(add(+), sub(-), mul(*), div(/))
df2.add(df4)               # df2 + df4 결과와 동일
df2.add(df4, fill_value=0) # NA가 fill_value값으로 치환된 후 연산

# 브로드캐스팅 기능
arr1 = np.arange(1,9).reshape(4,2)
arr1 + arr1[:,0:1]                 # 첫번째 컬럼을 차원유지 방법으로 추출후 연산

df1 = DataFrame(arr1)
df1 + df1.iloc[:,0]    # df1의 키는 [0,1], df1.iloc[:,0] 키는 [0,1,2,3]
df1 + df1.iloc[:,0:1]  # df1의 키는 [0,1], df1.iloc[:,0] 키는 [0]

df1.add(df1.iloc[:,0], axis=0)  # 컬럼끼리의 반복연산(서로 다른 행을 묶어 전달)

# [ 연습 문제 - 브로드캐스팅 ]
# 다음의 데이터 프레임에서 2000년 기준 가격 상승률 출력
df1 = DataFrame({'2000':[1000,1100,1200],
                 '2001':[1150,1200,1400],
                 '2002':[1300,1250,1410]}, index = ['a','b','c'])

df1.sub(df1.iloc[:,0], axis=0).div(df1.iloc[:,0], axis=0) * 100

# [ 연습 문제 ]
# 1. 3 X 4 배열 생성 후 a,b,c,d 컬럼을 갖는 df1 데이터프레임 생성
a1 = np.arange(1,13).reshape(3,4)
df1 = DataFrame(a1, columns=['a','b','c','d'])

# 2. 2 X 4 배열 생성 후 a,b,c,d 컬럼을 갖는 df2 데이터프레임 생성
a2 = np.arange(1,9).reshape(2,4)
df2 = DataFrame(a2, columns=['a','b','c','d'])

# 3. 위 두 데이터프레임 union 후 df3 생성
df3 = df1.append(df2, ignore_index=True)

# 4. df3에서 0,2,4 행 선택해서 새로운 데이터 프레임 df4 생성
df4 = df3.iloc[[0,2,4],:]

# 5. df3에서 'b','d' 컬럼 선택 후 새로운 데이터 프레임 df5 선택
df5 = df3.loc[:,['b','d']]

# 6. df3 - df4 수행(NA 리턴 없이)
df3 - df4
df3.sub(df4, fill_value=0)


# 7. reindex : 인덱스의 재배치
df1.loc[:,['b','c','d','e']]               # 컬럼 reindexing
DataFrame(df1, columns=['b','c','d','e'])  # 컬럼 reindexing
df1.reindex(['b','c','d','e'], axis=1, fill_value=0)

# reindex 활용

# [ 예제 - df1의 df2 승수값 출력(df1**df2), 단 df2값이 없는 경우 1로 수정 ]
df1**df2
df1**df2.reindex(df1.index, fill_value=1)

# 8. 정렬
df1 = DataFrame({'col1':[3,2,4,1], 'col2':['a','c','d','b']})

df1.sort_values(by,                 # 정렬대상
                axis=0              # 정렬방향
                ascending=True,     # 정렬순서
                inplace=False,      # 정렬후 원본 대체 여부
                na_position='last') # NA 배치 순서

df1.sort_values('col1', ascending=False)                 # 원본 수정 안됌
df1.sort_values('col1', ascending=False, inplace=True)   # 원본 즉시 수정
df1.sort_values(['col1','col2'], ascending=[False,True]) # 컬럼별 정렬순서 전달


#[ 연습문제 ]
# 1. 'test3.txt' 파일을 읽고 다음과 같은 데이터 프레임 형태로 변경
# 	     20대	30대 40대 50대 60세이상
# 2000년	  7.5	3.6	 3.5  3.3	1.5
# 2001년	  7.4	3.2	 3	  2.8	1.2
# 2002년	  6.6	2.9	 2	  2	    1.1
# ..............................................
# 2011년	  7.4	3.4	 2.1  2.1	2.7
# 2012년	  7.5	3	 2.1  2.1	2.5
# 2013년	  7.9	3	 2	  1.9	1.9
a1 = np.loadtxt('test3.txt')
df1 = DataFrame(a1)

df1.columns = ['20대','30대','40대','50대','60세이상']

f1 = lambda x : str(x) + '년'
df1.index = list(map(f1, np.arange(2000,2014)))

# 2. 2010년부터의 20~40대 실업률만 추출하여 새로운 데이터프레임을 만들어라
df2 = df1.loc['2010년': ,'20대':'40대'] 

# 3. 30대 실업률을 추출하되, 소수점 둘째자리의 표현식으로 출력
df1.loc[:,'30대']

'%.2f' % 3.6                # 스칼라의 형식 변경
'%.2f' % df1.loc[:,'30대']  # 벡터연산 불가

f2 = lambda x : '%.2f' % x
df1.loc[:,'30대'] = list(map(f2, df1.loc[:,'30대']))

# 4. 60세 이상 컬럼 제외
df1 = df1.drop('60세이상', axis=1)

# 5. 30대 컬럼의 값이 높은순 정렬
df1.loc[:,'30대'] = df1.loc[:,'30대'].astype('float')
df1.sort_values('30대', ascending=False)

# 적용 메서드 : 함수의 반복 처리를 도와주는 메서드*****
# 1. map      : 1차원 구조에 적용 가능, 원소별 적용
# 2. apply    : 2차원 구조에 적용 가능, 행별 또는 컬럼별 적용(그룹연산에 주로 사용)
# 3. applymap : 2차원 구조에 적용 가능, 원소별 적용

df1.loc[:,'30대'].map(f2)

df1.apply(sum, axis=0)
df1.apply(sum, axis=1)

df1.applymap(f2)

# [ 연습 문제 - 위 데이터에서 ]
# 1. 2000년 기준 증감률
df1.dtypes

(df1 - df1.iloc[0,:]) / df1.iloc[0,:] * 100

# 2. 20대 기준 증감률
df1 - df1.iloc[:,0:1]            # 키값 불일치로 브로드캐스팅 불가
df1.sub(df1.iloc[:,0:1], axis=0) # 불가, 20대 컬럼이 데이터프레임으로 전달
df1.sub(df1.iloc[:,0], axis=0)   # 가능, 20대 컬럼이 시리즈로 전달

df1.sub(df1.iloc[:,0], axis=0).div(df1.iloc[:,0], axis=0) * 100

# [ 주의 - 데이터프레임의 브로드캐스팅 ]
# 시리즈(1차원)와 데이터프레임(2차원)의 연산시만 브로드캐스팅이 가능(키 일치 시)
# 따라서 데이터프레임과 데이터프레임끼리는 산술연산 메서드를 통해서도
# 브로드캐스팅 전달 불가

# 3. 각 년도별 각 연령대가 차지하는 실업률의 비율 리턴
#              20대        30대        40대        50대      60세이상
# 2000년  38.659794  18.556701  18.041237  17.010309   7.731959
f5 = lambda x : x / x.sum() * 100
df1.apply(f5,axis=1)





