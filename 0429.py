run profile1
# subway2.csv 데이터를 이용해
sub = pd.read_csv('subway2.csv', engine = 'python', skiprows = 1)
sub.iloc[:,0] = sub.iloc[:,0].fillna(method = 'ffill')
sub = sub.set_index(['전체','구분'])
sub.columns = sub.columns.str[:2].astype('int')


#1) 시간대별 승차의 최대/최소 동시 출력
sub2 = sub.xs('승차', axis = 0, level = 1)
sub2.max(0)
sub2.min(0)

sub2.apply(lambda x : Series([x.max(),x.min()], index=['max','min']), axis = 0)

#2) 시간대별 하차가 가장 많은/적은 역 동시 출력
sub3 = sub.xs('하차',axis = 0, level = 1)

sub3.idxmax(0)
sub3.idxmin(0)

sub3.apply(lambda x : Series([x.idxmax(),x.idxmin()], index=['max','min']), axis = 0).T

# 데이터의 결합
#1. merge
# - 조인연산
 
#2. concat***
# - 분리된 데이터의 union 처리
# - 상하결합(axis = 0), 좌우결합(level = 1)가능, axis = 0 디폴트
# - outer join이 기본 연산, 서로 다른 key값도 NA로 출력

s1 = Series([1,2,3,4])
s2 = Series([5,6,7,8,9])

pd.concat([s1,s2],axis = 0)                    # 상하 결합, 묶을 대상이 여럿이기 때문에 list로 묶음.
pd.concat([s1,s2], ignore_index =True)         # 상하 결합
pd.concat([s1,s2], axis = 1)                   # 좌우 결합, 같은 key끼리 묶임
 pd.concat([s1,s2], axis = 1, join = 'inner')   # 양쪽에 존재하는 key만 출력

df1 = DataFrame(np.arange(1,5).reshape(2,2), columns = ['a','b'])
df2 = DataFrame(np.arange(5,9).reshape(2,2), columns = ['a','b'])
df3 = DataFrame(np.arange(9,13).reshape(2,2), columns = ['a','c'])

pd.concat([df1,df2])              # axis = 0, 같은 컬럼일 경우 결합(세로)
pd.concat([df1,df3])                
pd.concat([df1,df2], axis = 1)    # axis = 1, 같은 인덱스일 경우 결합(가로)
pd.concat([df1,df3], axis = 1)


#3. combine_first 
# - df1.combine_first(df2)
# - 분리된 두 데이터 병합
# - 같은 key를 갖는 경우 NA 수정
# - 서로 다른 key를 갖는 경우 df2의 key를 df1에 추가
 
df1.iloc[1,1] = NA
df1.combine_first(df2)  # df1의 NA는 df2의 동일 key 값의 value로 대체
df1.combine_first(df3)  # df1에 없는 df3의 key 데이터 추가


# df1의 NA를 df2로 수정
np.where(df1.b.isnull(),df2.b,df1.b)
df2.b

#[참고 - chunksize를 지정한 데이터 부분 불러오기]
df_test = pd.read_csv('read_test.csv',chunksize = 30)


#1) 건수 지정, 차례대로 출력
df_test1 = df_test.get_chunk(10)
df_test2 = df_test.get_chunk(10)
...

#2) for문을 사용한 print
df_test = pd.read_csv('read_test.csv', chunksize = 30)
for i in df_test:
    print(i)

#3) for문을 사용한 concat***
df_test = pd.read_csv('read_test.csv', chunksize = 30)

df_new = DataFrame()

for i in df_test:
    df_new = pd.concat([df_new,i])
  
df_new
    
# pandas 중복 관련 메서드
## Series
s1 = Series([1,1,2,3,4])

s1.duplicated()          # 순차적 접근, 중복여부 출력
s1[s1.duplicated()]      # 중복값 확인
s1[~s1.duplicated()]     # 중복값 제거

s1.drop_duplicates()     # 중복값 제거

##DataFrame
df1 = DataFrame({'col1':[1,1,2,3,8,8], 'col2':[5,6,7,7,9,9]})

df1.drop_duplicates('col1')           # 컬럼별 전달 가능
df1.drop_duplicates(['col1','col2'])  # 동시 중복 컬럼 제













