run profile1

df1 = DataFrame(np.arange(1,13).reshape(4,3))
df2 = DataFrame(np.arange(13,19).reshape(2,3))
df3 = DataFrame(np.arange(10,90,10).reshape(4,2))


# 5. 구조 수정
# 1) row 추가
df1.append(df2)                        # 0,1,2,3,0,1(index), index 그대로 유지
df1.append(df2, ignore_index = True)   # 0,1,2,3,4,5 (index), ignore_index = True => 기존 행번호 무시하고 순차적으로 전달

# 2) column 추가
 df1['a']=[11,21,31,41]  # Key 확장 / 'a' columns명, [] values값


# 6. 산술연산
df4 = DataFrame(np.array([100,101,102]))
df1.columns = ['a','b','c']
df3.columns = ['a','b']

df1 + df3  # 서로 같은 컬럼끼리 연산 가능(키 불일치시 NA리턴)

df2 + df4  # 서로 같은 인덱스만 연산 가능 (키 불일치는 NA리턴)
 

# 산술연산 메서드 [add(+), sub(-), mul(*), div(/)] * fill_value
df2.add(df4)  # df2 + df4 결과와 동일
df2.add(df4, fill_value = 0) # NA가 fill_value값으로 치환된 후 계산

# 브로드캐스팅 기능
arr1 = np.arange(1,9).reshape(4,2)
arr1 + arr1[:,0]   # 연산 불가, 브로드캐스팅 기능에 위반된다.
arr1 + arr1[:,0:1] # 연산 가능, 차원유지 방법으로 추출 후 연산
 
df1 = DataFrame(arr1)
df1 + df1.iloc[:,0]    # df1의 키는[0,1,2], df1.iloc의 키는 [0,1]
# => Series로 출력 key -> index/ 컬럼 + 행 연산으로 nan 출력

df1 + df1.iloc[:,0:1] # df1의 키는[0,1,2], df1.iloc의 키는 [0]
# =>  key 일치하지 않으면 반복연산 하지 않는다.

df1.add(df1.iloc[:,0], axis = 0) # axis = 0, 컬럼끼리 반복 연산(서로 다른 행을 묶어 전달)


# =============================================================================
# 연습문제 (브로드캐스팅)
# =============================================================================
# 다음의 데이터 프레임에서 2000년 기준 가격 상승률 출력
df1 = DataFrame({'2000':[1000,1100,1200],
                 '2001':[1150,1200,1400],
                 '2002':[1300,1250,1410]}, index = ['a','b','c'])

df1.sub(df1.iloc[:,0], axis =0) # 차이
df1.sub(df1.iloc[:,0], axis =0).div(df1.iloc[:,0], axis = 0) *100

df1.div(df1.iloc[0,:],axis=1)
df1.iloc[0:,]

# =============================================================================
# #[연습문제]
# =============================================================================
#1. 3*4 배열 생성 후 a,b,c,d 컬럼 갖는 df1 데이터 프레임 생성
df1= DataFrame(np.arange(1,13).reshape(3,4), columns=['a','b','c','d'])

#2. 2*4 배열 생성 후 a,b,c,d 컬럼 갖는 df2 데이터 프레임 생성
df2= DataFrame(np.arange(1,9).reshape(2,4), columns=['a','b','c','d'])

#3. 두 데이터 프레임 union후 df3 생성
df3 = df1.append(df2, ignore_index = True)

#4. df3에서 0,2,4행 선택해 새로운 데이터프레임 df4 생성
df4 = df3.iloc[[0,2,4],:]
df4 = df3.loc[[0,2,4],:]

#5. df3에서 'b','d' 컬럼 선택 후 새로운 데이터프레임 df5 생성
df5 = df3.loc[:,['b','d']]

#6. df3- df4 수행(NA리턴 없이)
df3.sub(df4, fill_value = 0)

# 7. reindex : 인덱스의 재배치
df1.loc[:,['b','c','d','e']]                 # 컬럼 재배치
DataFrame(df1, columns = ['b','c','d','e'])  # 컬럼 reindexing
df1.reindex(['b','c','d','e'], fill_value = 0)  # index 재배치, axis = 0 기본값(행 방향)
df1.reindex(['b','c','d','e'],axis = 1, fill_value = 0) # columns 재배치

# reindex 활용

#[예제 : df1의 df2 승수 값 출력 (df1**df2), 단 df2값이 없는 경우 1로 수정]
df1**df2
df1**df2.reindex(df1.index, fill_value = 1)
df1.pow(df2, fill_value = 1) # float type

# 8. 정렬
df1 = DataFrame({'col1':[3,2,4,1], 'col2':['a','b','c','d']}) 

df1.sort_values(by,                    # 정렬대상
                axis=0,                # 정렬방향
                ascending = True,      # 정렬순서 , True(내림차순)
                inplace = False,       # 정렬 후 원본 대체 여부 
                na_position = 'last')  # NA 배치 순서
    

df1.sort_values('col1', ascending = False)                  # 원본 수정 안 됨.
df1.sort_values('col1', ascending = False, inplace = True)  # 원본 즉시 수정
df1.sort_values(['col1','col2'], ascending = [False,True])  # 컬럼별 정렬순서 정렬

# =============================================================================
# #[연습문제]
# #'test3.txt'파일을 읽고 다음과 같은 데이터 프레임 형태로 변경
# =============================================================================
a1 = np.loadtxt('test3.txt')
df1 = DataFrame(a1)
df1

df1.columns=['20대','30대','40대','50대','60세이상']
df1.index = 
np.arange(2000,2014)

f1 = lambda x : str(x)+'년'
df1.index = list(map(f1,np.arange(2000,2014)))
df1

#def f_read_txt(file,sep=' ', fmt=int) :
#    c1 = open(file,'r')   # 커서 선언
#    v1 = c1.readlines()               # fetch 
#    c1.close()
#    
#    outlist = []
#    
#    for i in v1 :
#        L1 = i.strip().split(sep)
#        outlist.append([fmt(i) for i in L1])
#    
#    return outlist
#    
#df1 = DataFrame(f_read_txt('test3.txt', sep = '\t', fmt = float),columns = ['20대','30대','40대','50대','60대'])
#df1
#
#a1= df1.index.values
#a1 = [str(i)+'년' for i in a1]
#df1.index = a1
#df1
 
#2. 2010년부터 2-40대 실업률만 추출해 새로운 데이터 프레임 생성
df1.loc['2010년':,'20대':'40대']

#3. 30대 실업률을 추출하되, 소수점 둘째자리의 표현식으로 출력
df1.loc[:,'30대']
'%.2f' % 3.6                 # 스칼라의 형식 변경
'%.2f' % df1.loc[:,'30대']   # 벡터연산 불가

f2 = lambda x : '%.2f' % x
df1.loc[:,'30대'] = list(map(f2,df1.loc[:,'30대']))

df1.iloc[:,[1]]

#4. 60세 이상 컬럼 제외
df1.drop('60세이상', axis = 1)

df1.loc[:,df1.columns !='60대']
df1.iloc[:,0:4]

#5. 30대 컬럼의 값이 높은 순으로 정렬
df1.loc[:,'30대'] = df1.loc[:,'30대'].astype('float')

df1.sort_values('30대', ascending = False)  # 30대 문자형 -> 자릿수 다를 경우 문제 발생할 수 있다 (*주의)

# =============================================================================
# ## 적용메서드 : 함수의 반복처리 돕는 메서드**********
# =============================================================================

#1. map      : 1차원 구조에 적용 가능, 원소별 적용
#2. apply    : 2차원 구조에 적용 가능, 행별 또는 컬럼별 적용 (그룹연산에 주로 사용)
#3. applymap : 2차원 구조에 적용 가능, 원소별 적용

df1.loc[:,'30대'].map(f2) # 1차원 - Series
df1.apply(sum, axis = 0)  # axis = 0, 서로 다른 행끼리(세로방향, 컬럼으로 묶는다.)
df1.apply(sum, axis = 1)  # 출력 결과 - series/ 원소별 적용 불가

df1.applymap(f2)  #=> apply(,c(1,2),) in R

#[연습문제 - 위 데이터에서 ]
#1. 2000년 기준 증감률
df1.apply(sum ,axis = 1)

df1.sub(df1.iloc[0,:],axis=1).div(df1.iloc[0,:],axis =1)*100

#2. 20대 기준 증감률
df1.iloc[:,0]


df1.sub(df1.loc[:,'20대'],axis = 0).div(df1.loc[:,'20대'], axis = 0) *100

#3. 년도별 연령대가 차지하는 실업률의 비율 (총 합 100)
df1.applymap(sum)



pd.read_table('여아신생아.txt', engine = 'python')  # 파일 endline 인식 못 할때 engin = 'python' 사용
















