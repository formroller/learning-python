run profile1
# 1. subway2.csv  파일을 읽고(loadtxt로 불러온 후 데이터프레임 변경)
## 1) 다음의 데이터 프레임 형식으로 변경
# 전체     구분   5시       6시     7시 ...
# 서울역  승차 17465  18434  50313 ...
# 서울역  하차 ....
arr1 = np.loadtxt('subway2.csv', delimiter = ',', dtype = 'str', skiprows = 1)
df1 = DataFrame(arr1)

df1.columns = df1.iloc[0,:]
df1 = df1.drop(0)

# 전체 컬럼 수정
#sol1) 치환 대상만 추출 후 치환
df1.loc[:,'전체'][2] # 빈 문자열 확인 
df1.loc[:,'전체'] == '' #  Series 조건 검색 가능
df1.loc[:,'전체'][df1.loc[:,'전체'] == ''] = NA # 빈 문자열 NA로 치환 / matching 되는 데이터만 치환 (치환 범위가 적어진다.)

#so12) 조건에 따른 치환(전체범위 치환)
np.where(df1.loc[:,'전체'] == '',NA,df1.loc[:,'전체']) # 전체 덮어씀 -> 치환 범위 커진다.

df1.loc[:,'전체'] = df1.loc[:'전체'].fillna(method = 'ffill')

# index(columns) 수정
c1 = df1.columns.values
f1 = lambda x : str(int(x[:2])) +'시'
c1[2:] = Series(c1[2:]).map(f1) # array구조일때 .map 메소드 사용 불가 => Series로 감싸야한다.
c1.type
df1.columns = c1


list(map(f1,c1[2:]))
## 2) 각 역별 하차의 총 합
df1.dtypes # 데이터 타입 확인

# sol1) 벡터연산 가능한 astype 메서드 사용
df1.loc[:,'5시':] = df1.loc[:,'5시':].astype('int')

# sol2) int + applymap을 통한 전체 치환
f2 = lambda x : int(x)
df1.loc[:,'5시':].applymap(f2)

# 하차 추출
df2 = df1.loc[df1.loc[:,'구분'] =='하차',:]
# 인덱스 처리
df2.index = df2.loc[:,'전체'] 
df2=df2.set_index(['전체','구분'])   

df2.sum(axis = 1)
df2.apply(sum,axis = 1)
# =============================================================================
# #[참고 - set_index 메서드]
# #본문에서 특정 컬럼을 index로 전달하고자 할 때, 전달과 동시에 본문에서 해당 컬럼 제외
# #단, 인덱스 설정만 가능하고 컬럼 설정은 불가
# 
# df2.index = df2.loc[:,'전체'] 
# # '전체' 컬럼을 인덱스로 처리, 본문에서 제외
# # 인덱스 처리 후 기준이 되는 인덱스 별도로 제거해야한다.
# 
# df2=df2.set_index(['전체','구분'])   
# # '전체', '구분' 컬럼을 멀티 인덱스 처리
# # 원본에 인덱스 처리 -> 기준이 되는 인덱스 빠진다
# 
# df1.reset_index()   # 이미 설정된 인덱스를 컬럼으로 재배치
# =============================================================================


## 3) 승차의 시간대별 총 합
df3 = df1.loc[df1.loc[:,'구분']=='승차',:]
df3 = df3.set_index('전체')
df3 = df3.drop('구분', axis = 1)
df3 = df3.astype('int')

df3.sum(axis = 0)
df3.apply(sum, axis = 0)

## 4) top(data,n=5) 함수 생성, 각 역별 승차가 많은 top 5 시간대 출력
df3.loc['서울역(1)',:].sort_values(ascending = False)[:5]

def top(data, n = 5):
    return data.sort_values(ascending = False)[:5]

top(df3.loc['서울역(1)',:])

## 5) 하차 인원의 시간대별 각 역의 차지 비율 출력
df2.loc[:,'5시'] / df2.loc[:,'5시'].sum() * 100
df2.loc[:,'6시'] / df2.loc[:,'6시'].sum() * 100
...

f3 = lambda x : x / x.sum() *100
df2.apply(f3,axis = 0)


# [ 참고-fillna 메서드 ]
s1 = Series([1,NA,2,NA,2])
s1.fillna(method='ffill')   # 이전값으로 치환
s1.fillna(method='bfill')   # 이후값으로 치환

