run profile1
# =============================================================================
# 파이썬의 날짜 표현
# =============================================================================
from datetime import datetime

# =============================================================================
# #1. 현재 날짜 및 시간
# =============================================================================
d1 = datetime.now()   # in R : Sys.Date(), in Oracle : sysdate

d1.year       # datetime 객체의 년 추출
d1.month      # datetime 객체의 월 추출
d1.day        # datetime 객체의 일 추출
d1.hour       # datetime 객체의 시 추출
d1.minute     # datetime 객체의 분 추출
d1.second     # datetime 객체의 초 추출

# =============================================================================
# #2. 날짜 파싱 (문자 -> 날짜 인식)
# =============================================================================
#2-1) datetime.strptime
# - 두번째 인자(날짜 포맷) 생략 불가
# - 벡터 연산 불가
d2 = datetime.strptime('2020-05-31','%Y-%m-%d')

#2-2)pd.to_datetime
# - 날짜 포맷 생략 가능
# - 벡터연산 가능
pd.to_datetime(['2020/01/01','2020/01/02'])
pd.to_datetime(['01/12/20','01/13/20'], format = '%m/%d/%y')

#2-3)datetime.datetime
datetime(2012,1,2) # 년/월/일 순서

# =============================================================================
# #3. 날짜 포맷 변경
# =============================================================================
d2.strftime('%Y')

# =============================================================================
# #4. 날짜 연산
# =============================================================================
d2-d1            # timedelta object로 출력
(d2-d1).days     # timedelta object의 일 수 출력
(d2-d1).seconds  # timedelta object의 초 수 출력

# d1날짜로부터 7일 뒤 날짜 계산
d1 + 7  # 연산 불가, 묵시적 형 변환 불가

# =============================================================================
# #5. datetime를 사용한 날짜 연산
# =============================================================================
from datetime import timedelta

d1 + timedelta(7)    # 7일 뒤 
d1 + timedelta(1/24) # 1시간 뒤

# =============================================================================
# #6. offset 사용한 날짜 연산
# =============================================================================
import pandas.tseries.offsets
dir(pandas.tseries.offsets)

from pandas.tseries.offsets import Day, Hour, Second

d1 + Day(5)  # timestamp로 출력
d1 + Hour(12)

#[연습문제]
#emp.csv 파일을 읽고
emp = pd.read_csv('emp.csv', engine = 'python')
datetime.strptime(emp.HIREDATE,'%Y-%m-%d %H:%M')  # 벡터연산 불가
emp['HD'] = emp.HIREDATE.map(lambda x : datetime.strptime(x, '%Y-%m-%d %H:%M'))

########
emp.HIREDATE=emp.HIREDATE.str.split(' ').str[0]
emp.HIREDATE = emp.HIREDATE.apply(lambda x : datetime.strptime(x,'%Y-%m-%d'))

#1) 년,월,일 각각 추출
v_year = emp['HD'].map(lambda x : x.year)
v_month = emp['HD'].map(lambda x : x.month)
v_day = emp['HD'].map(lambda x : x.day)

#2) 급여 검토일의 요일 출력(단, 급여 검토일은 입사일 +100일 후 날짜)
emp.HD.map(lambda x : (x+Day(100)).strftime('%A'))

#3) 입사일로부터 근무일 수 출력
(d1 - emp.HD).map(lambda x : x.days)

# =============================================================================
# #7. 날짜 index 생성 및 색인
# =============================================================================
# pd.date_range : 연속적 날짜 출력

pd.date_range(start,     # 날짜 출력
              end,       # 끝 날짜   
              periods,   # 기간(갯수)
              freq)      # 날짜 빈도

pd.date_range(start = '2020/01/01',end = '2020/01/31')
pd.date_range(start = '2020/01/01',end = '2020/01/31', freq = '7D')    # 7D, 7일 간격 
pd.date_range(start = '2020/01/01',end = '2020/01/31', freq = 'W')     # 'W' 매주 일요일 (W-SUN,일요일이 기본값)
pd.date_range(start = '2020/01/01',end = '2020/01/31', freq = 'W-MON') # 'W-MON', 매주 월요일
pd.date_range(start = '2020/01/01', periods = 20)

#연습문제) 1부터 연속적인 값을 갖는 Series 생성,
#2020년 매주 일요일 날짜를 인덱스로 갖도록 설정
d1 =  pd.date_range(start = '2020-01-01' , end = '2020-12-31', freq = 'W')
s1 = Series(np.arange(1,len(d1)+1), index= d1)

###
a1 = np.arange(1,len(sun1)+1)
sun1 = pd.date_range(start = '2020-01-01' , end = '2020-12-31', freq = 'W-SUN')

pd.Series(a1, index = sun1 )

# datetime 객체를 인덱스로 생성 시 날짜값 색인 가능
s1['2020']    # 특정 년도(2020) 데이터 출력
s1['2020-12'] # 2020년 12월에 대한 데이터 출력

# truncate : 날짜 인덱스를 갖는 경우 날짜 선택
s1.truncate(after = '2020-11-01')
s1.truncate(before = '2020-11-01')

s1[:'2020-11-01'] : # 날짜를 슬라이스 색인값으로 사용가능, end 범위에 포함
    
    
# =============================================================================
# #8. resample     : 날짜의 빈도수 변경
# =============================================================================
# - upsampling   : 더 많은 날자수로 변경 (주 -> 일별)
# - downsampling : 더 작은 날짜수로 변경 (일 -> 월별)

s1.resample('D', fill_method = 'ffill')   # upsampling시 fill_method 필요
s1.resample('D', fill_method = 0)         # fill_method는 값으로 치환 불가
s1.resample('D').asfreq()                 # .asfreq(), upsampling시 새로 생긴 날짜의 value NA로 출력

s1.resample('M').sum()        # downsampling시 그룹함수 전달 필요 ('M' 매 월 마지막 일 출력)
s1.resample('M', how = 'sum') # downsampling시 그룹함수 전달 필요 

# 예제 s1을 일별 데이터로 정리, value는 0으로 표현
s1.resample('D').sum()

#[연습문제]
#부동산_매매지수.csv 파일을 읽고
df1 = pd.read_csv('부동산_매매지수.csv', engine = 'python', skiprows = [0,2])
# NA삭제
#1)
df1.iloc[0,0] = NA
df1 = df1.dropna(axis = 0, how = 'all')  # all, 모든 컬럼이 na일 경우 삭제해라.

#2) 
df1.iloc[0].isull().any()   # NA가 한개라도 포함되있는지
df1.iloc[0].isull().all()   # 전체가 NA인지
df1.iloc[0].isull().sum()   # NA 포함된 갯수

df1.loc[df1.apply(lambda x : x.notnull().all(), axis = 1),:]


###########
sale = pd.read_csv('부동산_매매지수.csv', engine = 'python', skiprows = 1)
sale = sale.dropna(0)
sale = sale.iloc[1:,:]
sale.applymap(lambda x : int(x))


#1) 2008년 4월 7일 부터 관찰된 매 주의 구별 매매지수라고 할 때, 날짜컬럼 추가
df1.shape  # 행, 열의 갯수
df1.index = pd.date_range('2008/04/07', periods = df1.shape[0], freq = '7D')  # resample 기능 활용하기 위해 index로 지정

##########
date1= pd.date_range(start = '2008/04/07', periods=len(sale), freq = 'W')
sale['date'] = date1

#2) 2017년 기준 전년도 대비 상승률 상위 10개 구, 상승률과 함께 출력
df11 = df1.resample('Y').mean()

df11['2017'] - df11['2016']  # key값 있기 때문에 NA출력된다

df11['2017'].values - df11['2016'].values / df11['2016'].values *100

# 날짜의 이동
#모든 행이 이전행에 대해 연산 가능
df11.shift(periods=1,        # 이동 범위
           freq=None,        # 년/월 등의 기간 설정
           axis=0,           # 디폴트는 이전 행
           fill_value=None)  # 이전값 없는 경우 NA대신 채울 값

df11.shift(1)
df22 = (df11 - df11.shift(1))/ df11.shift(1) *100

df22['2017'].T.sort_values(ascending = False, by = '2017-12-31') # 데이터 프레임일경우 by값에 컬럼명 지정해야한다.

























