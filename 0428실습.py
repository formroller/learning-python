run profile1
# 1. 부동산_매매지수현황.csv파일을 읽고
df1 = pd.read_csv('부동산_매매지수현황.csv', engine='python', skiprows =1)

s1 = Series(df1.columns.str.split(' ').str[0])
col1 = s1.replace('Unnamed:',NA).fillna(method = 'ffill')
df1.iloc[0]

# multi-columns 설정
df1.columns = [col1,df1.iloc[0]]

# 불필요한 행 제거
df1 = df1.drop([0,1])

# 년,월,일 3-level multi-index 설정
year = df1.iloc[:,0].str[:4]
mon = df1.iloc[:,0].str[5:7]
day = df1.iloc[:,0].str[8:]

df1.index = [year,mon,day]

# 첫번째 컬럼(날짜컬럼) 제거
df1.drop(NA,axis =1, level = 0) # na로 된 컬럼 제거 불가
df1 = df1.iloc[:,1:]             # 위치값 기반 제거

# index, columns 이름 변경
df1.index.names = ['year','month','day']
df1.columns.names = ['city','act']

# 데이터 타입 변경
df1 = df1.astype('float')


# 1) 각 월별 지역별 활발함/한산함 지수의 평균을 각각 출력
df1.mean(axis = 0, level =1)


# 2) 지역별 활발함지수가 가장 높은 년도 출력
df1_1 = df1.mean(axis = 0, level = 0).xs('활발함', axis = 1, level = 1)
df1_1.idxmax()

# 2. gogak, gift 테이블을 각각 파이썬에 불러와서 각 고객이 가져갈 수 있는 최대 상품 출력
# (oracle에서 데이터만 불러 온후 파이썬으로 풀이)
import os
import cx_Oracle
os.putenv('NLS_LANG','KOREAN_KOREA.KO16MSWIN949')
con1 = cx_Oracle.connect("scott/oracle@localhost:1521/orcl")

gogak = pd.read_sql('select * from gogak', con = con1)
gift= pd.read_sql('select * from gift', con = con1)

gift.loc[(gift['G_START'] <= 90000 ) & (980000 <= gift['G_END']),'GNAME']           # 리턴 결과 : Series
gift.loc[(gift['G_START'] <= 90000 ) & (980000 <= gift['G_END']),'GNAME'].iloc[0]   # 리턴 결과 : string
gift.loc[(gift['G_START'] <= 90000 ) & (980000 <= gift['G_END']),'GNAME'].values    # 리턴 결과 : array 
gift.loc[(gift['G_START'] <= 90000 ) & (980000 <= gift['G_END']),'GNAME'].values[0] # 리턴 결과 : string

f1 = lambda x : gift.loc[(gift['G_START'] <= x ) & (x <= gift['G_END']),'GNAME'].iloc[0]

gogak['POINT'].map(f1)


# 3. movie_ex1.csv 데이터로부터 연령대별 요일별 이용률의 평균을 출력
movie = pd.read_csv('movie_ex1.csv', engine = 'python')

datetime.strptime('2018228','%Y%m%d')
datetime.strptime('201821','%Y%m%d')
datetime.strptime('2018/2/1','%Y/%m/%d')

# sol1)
vdate = movie['년'].astype('str')+'/'+movie['월'].astype('str')+'/'+movie['일'].astype('str')

vdate.map(lambda x : datetime.strptime(x,'%Y/%m/%d').strftime('%A'))

# sol2) 사용자 정의함수를 통한 문자열 결합 (다수인자 전달 방식)
f2 = lambda x,y,z : str(x) + '/' + str(y) + '/'  + str(z)

movie['년'].map(f2,movie['월'],movie['일'])              # map 메서드는 추가인자 전달 불가
L1 = list(map(f2,movie['년'],movie['월'],movie['일']))   # map 함수, 추가인자 전달 가능

Series(L1).map(lambda x : datetime.strptime(x,'%Y/%m/%d').strftime('%A')) # list 객체에 map 메서드 사용불가 -> Series로 변경

# sol3-중요) apply를 사용한 다수인자 전달 방식 (pandas 적용 메서드)*****
 # - 추가인자 전달(applymap)
 movie.apply(f2,axis, movie['년'],movie['월'],movie['일'])       # 불가
 
 f3 = lambda x : str(x[0]) + '/' + str(x[1]) + '/' + str(x[2])
movie.apply(f3,axis=1)


movie

# =============================================================================
# 
# =============================================================================




run profile1
# 1. 부동산_매매지수현황.csv파일을 읽고
df1 = pd.read_csv('부동산_매매지수현황.csv', engine='python', )
df1 = df1.drop(1, axis = 0)
# 인덱스
df1['data'] = df1.iloc[:,0].str.split('-').str.get(0)
df1['month'] = df1.iloc[:,0].str.split('-').str.get(1)
df1['day'] = df1.iloc[:,0].str.split('-').str.get(2)
df1.fillna('1')
df1 = df1.set_index(['data','month','day'])
#전처리
df1.iloc[0,:] = df1.iloc[0,:].str.split(' ').str.get(0).fillna(method = 'ffill')
df1 = df1.drop('Unnamed: 0', axis =1)

#컬럼
df1.columns = [df1.iloc[0,:], df1.iloc[1,:]]
df1.columns.names = ['loc','act']

df1 = df1.drop(NA,axis=0,level=0 )



# 1) 각 월별 지역별 활발함/한산함 지수의 평균을 각각 출력
df1.pivot_table('date','loc')
df1.unstack()


# 2) 지역별 활발함지수가 가장 높은 년도 출력


# 2. gogak, gift 테이블을 각각 파이썬에 불러와서 각 고객이 가져갈 수 있는 최대 상품 출력
# (oracle에서 데이터만 불러 온후 파이썬으로 풀이)

# 3. movie_ex1.csv 데이터로부터 연령대별 요일별 이용률의 평균을 출력



