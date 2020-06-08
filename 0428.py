run profile1

s1 = Series([10,2,5,1,6])
s2 = Series([10,2,5,1,1,6])

# ranck :큰 / 작은 순서대로 순위 부여
s1.rank(asxis,
        method = {'average',     # 동순위에 대한 평균값 출력(서로 같은 순위 부여)
                  'min',         # 동순위중 작은 값 출력 (서로 같은 순위 부여)
                  'max',         # 동순위중 큰 값 출력(서로 같은 순위 부여)
                  'first'}       # 동순위중 가장 먼저 배치된 값에 높은 순위 부여(서로 다른)
        ascending = True)        # 정렬 순서


s1.rank()
s2.rank()                    # 4,5번째 관측치가 1,2 순위이므로 그것의 평균 1.5 리턴
s2.rank(method ='min')       # 4,5번째 관측치가 1,2 순위이므로 그중 작은 1 리턴
s2.rank(method ='max')       # 4,5번째 관측치가 1,2 순위이므로 그 중 큰 2 리턴
s2.rank(method ='first')     # 4,5번째 관측치가 1,2 순위이므로 순서대로 1,2 각각 리턴

df1 = DataFrame({'col1':[4,1,3,5], 'col2' : [1,2,3,4]})
df1.rank(axis = 0)  # 행별 순위
df1.rank(axis = 1)  # 열별 순위

# cross-table
 - 행/열별 연산 용이
 - join 불가
 - group by 연산 불가
 - 시각화시 주로 사용
 - multi-index 갖는 구조를 unstack처리해 얻거나 pivot을 통해 얻을 수 있다.
 
 # 1. pivot
 - 각 컬럼의 값을 교차테이블 구성요소로 전달, 교차테이블 완성
 - index, columns, values 컬럼을 각각 전달
 - 요약기능 없음
 
# 2. pivot_table
 - pivot 기능과 유사, 더 많은 옵션 사용 가능
 - index, columns, values 컬럼을 각각 전달
 - aggfunc 옵션 사용해 요약 기능 전달 가능(기본은 평균)
 - fill_value 옵션 사용해 NA값 대체 가능
 
# 예제) 아래 데이터프레임을 각각 교차 테이블 형태로 정리
df1 = pd.read_csv('dcast_ex1.csv', engine = 'python')
df2 = pd.read_csv('dcast_ex2.csv', engine = 'python')
df3 = pd.read_csv('dcast_ex3.csv', engine = 'python')

df1.pivot(index = 'name', columns = 'info',values = 'value')
df1.pivot('name','info')  # values 생략시 언급된 컬럼 외 모든 컬럼 선택

#예2) 년도별 음료 판매현황 정리표
df2.pivot(index = 'year',columns ='name', values = 'qty')
df2.pivot(index = 'year',columns ='name', values = ['qty','price'])

#예3) 년도별 음료수량 정리표
df3.pivot('년도','이름','수량')   # 중복값 에러 발생

df3.pivot_table(index = '년도', columns = '이름', values='수량') # aggfunc 생략시 mean 리턴

df3.pivot_table(index = '년도', 
                columns = '이름', 
                values='수량', 
                aggfunc = sum,   # aggfunc 전달
                fill_value = 0)  # NA 치환옵션

#[연습문제]
# movie_ex1.csv 데이터로부터 연령대별 성별 이용비율의 평균을 교차테이블 형식으로 출력
movie = pd.read_csv('movie_ex1.csv', engine = 'python')
movie.pivot_table(index = '성별',columns = '연령대',values = '이용_비율(%)', aggfunc = 'sum')

movie.pivot_table(index = '성별',columns = '연령대',values = '이용_비율(%)', aggfunc = 'count')
movie.pivot_table(index = '성별',columns = '연령대',values = '이용_비율(%)', aggfunc = len)



# 연습문제
# delivery.csv파일을 읽고
df1 = pd.read_csv('delivery.csv', engine = 'python')

# 1) 각 업종별 통화건수가 많은 순서대로 시군구의 순위 출력
df2 = df1.set_index(['업종','시군구'])['통화건수'].sum(level = [0,1]).unstack(0)
df2.rank(0, ascending = False, method = 'min')
df1.set_index(['업종','시군구'])['통화건수'].sum(level = [0,1]).unstack(0)

# 2) 각 시군구별 업종 비율 출력
#            족발/보쌈  중국음식  치킨
#강남구          31        45      21.5 ....
f1 = lambda x : x/x.sum()*100
df2.apply(f1,axis = 1) # axis =1 , 가로방향

#3) 시간대별 배달월수가 가장 많은 업종 1개 출력
df3 = df1.set_index(['시간대','업종'])['통화건수'].sum(level=[0,1]).unstack()
df3.idxmax(axis = 1)

df1.set_index(['시간대','업종'])['통화건수'].sum(level = [0,1]).unstack()

# merge
 - join 연산 수행
 - equi join만 가능
 - 두 개의 데이터 프레임만 join  가능
 - outer join 가능
 
pd.merge(left,                 # 첫번째 데이터프레임   
         right,                # 두번째 데이터프레임 
         how = {'left',    # 조인연산 방법, left outer join , 왼쪽 기준 오른쪽 데이터 출력
                'right',   # right outer join
                'outer',   # full outer join, 양쪽 모두 출력
                'inner'},  # inner join (조인조건 성립만 출력) * 기본값
         on = ,               # 조인컬럼  (=by)
         left_on = ,          # 왼쪽 데이터(첫 번째) 조인컬럼
         right_on =,          # 오른쪽 데이터(첫번째) 조인컬럼
         left_index = False,  # 왼쪽 데이터(첫번째) 인덱스 값으로 조인 엽
         right_index = False) # 오른쪽 데이터(첫번째) 인덱스 값으로 조인 엽

df1 = DataFrame({'col1':['a','b','c'],
                 'col2':[1,2,3]})

df2 = DataFrame({'col11':['a','b','d'],
                 'col22':[10,20,30]})

pd.merge(df1,df2,left_on='col1',right_on='col11',how='outer')

# -- index를 갖는 경우 조인 연산
df11 = df1.set_index('col1')
df22 = df2.set_index('col11')

pd.merge(df11, df22, left_on='col1',right_on='col11')   # 에러발생
pd.merge(df11, df22, left_index=True, right_index=True) # 조인가능 (index를 join key로 사용)

# 연습문제
# emp데이터를 데이터베이스에서 직접호출, 
# 각 직원의 이름,연봉, 상위관리자명을 출력하되 상위관리자명 없을경우 본인이름 출력
import cx_Oracle
con1 = cx_Oracle.connect('scott/oracle@localhost:1521/testDB')
emp = pd.read_sql('select * from emp', con = con1)

pd.merge(emp,emp, left_on = 'MGR', right_on = 'EMPNO', how = 'left')[['ENAME_x','ENAME_y','SAL_x']].fillna(axis = 1, method ='ffill')

# 벡터가 내장된 문자열 메서드***
#(=>벡터화 내장된 문자열 메서드)
L1 = ['a;b;c','A;B;C']
s1 = Series(L1)

#1. 기본적으로 제공되는 문자열 메서드의 벡터 연산 활용 예제
L1.split(';','')               # 적용 불가
[i.split(';')[0] for i in L1]  # 리스트 내포 표현식 처리
list(map(lambda x : x.split(';')[0],L1))
# 1) split()
s1.str.split(';')               # 벡터 연산 가능
# 2) replace()
s1.str.replace(';','|')         # 패턴치환 가능 / 값 치환 불가
                                # DF적용 불가/Series만 적용 가능
# 3) 대소치환
s1.str.uppre()
s1.str.lower()
s1.str.title()
# 4) 패턴 여부
s1.str.startswith('a')     # 'a'로 시작 여부
s1.str.endswith('c')       # 'c'로 끝나는지 여부
s1.str.contains('a')       # 'a' 포함 여부
# 5) 갯수
s1.str.count('a')          # 'a'의 포함 횟수
s1.str.len()               # 각 문자열의 길이
# 6) 제거함수
s2 = Series([' ab ',' AB '])
s2.str.strip().str.len()

s2.str.rstrip().str.len()
s1.str.lstrip('a')
# 7) 색인
s1.str.split(';').str[0]     # 벡터화된 색인 
s1.str.split(';').str.get(0) # str.get() / 벡터화된 색인 메서드
# 8) 위치값 출력
s1.str.find('b')             # 각 원소별 위치값 출력 (없으면 -1)
# 9) 문자열 결합
s2.str.cat(sep = ';')        # 시리즈의 원소를 구분기호로 모두 결합 
s2.str.join(sep=';')         # 문자열의 각 글자를 구분기호로 모두 결합
# 10) pad : 글자 삽입
s1.str.pad(width,            # 총 자릿수
           side = 'both',    # 삽입 방향
           fillchar = ' ')   # 삽입 문자
s1.str.pad(10,'both','-')

#[연습문제]
professor.csv 파일을 읽고
pro = pd.read_csv('professor.csv', engine = 'python')

#1) email-id 출력
pro['EMAIL'].str.split('@').str.get(0)
pro.EMAIL.str.split('@').str.get(0)
[x.split('@')[0] for x in pro.loc[:,'EMAIL']]

#2) 입사년도 출력
pro['HIREDATE'].str[:4]
pro.HIREDATE.str.split('/').str.get(0)

#3) ID의 두번재 값이 a인 직원 출력
pro.loc[pro['ID'].str[1]=='a',:]
pro.loc[pro.ID.str.get(1)=='a',:]


##[ 날짜 파싱 및 포맷 변경]##
from datetime import datetime

a1 = '2011/01/11'

#1. strptime 
# - 문자 -> 날짜
# - datetime 내 함수 형식으로 사용
# - 벡터연산 불가
 
datetime.strftime
datetime.strfpime

L1 = ['2011/01/01','2012/12/31']
a1.strptime('%Y/%m/%d')                # 적용 불가
v1 = datetime.strptime(a1,'%Y/%m/%d')  # datetime.datetime(2011, 1, 11, 0, 0) 년, 월,일,시,분 (날짜 타입)
v2 = datetime.strptime(L1,'%Y/%m/%d')  # 에러발생, 벡터 연산 불가



[datetime.strptime(i,'%Y/%m/%d') for i in L1]

#2. strftime 
# - 날짜 -> 문자 (날짜의 형식 변경)
# - 메서드, 함수 형식 모두 가능
# - 벡터연산 불가
  
v1.strftime(v1,'%A')
datetime.strftime(v1,'%A')
datetime.strftime(v2,'%A')   # 에러발생, 벡터연산 불가
















