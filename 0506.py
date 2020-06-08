run profile1

# =============================================================================
# #pd.cut
# =============================================================================
# - 연속형 변수의 구간 분할

pd.cut(
    x,                     # 연속형 변수를 갖는 객체
    bins,                  # 나눌 구간을 갖는 리스트 
    right=True,            # 오른쪽 닫힘 여부, {열림(,미만]닫힘} 디폴트
    labels=None,           # 각 구간의 이름 부여 
    include_lowest=False   # 최솟값 포함 여부
    )

s1 = Series([1,2,3,5,7,10])
pd.cut(s1, bins = [1,5,10])  # => 1초과 5이하 (right = True) * ] = 포함  / 5초과 10 미만
pd.cut(s1, bins = [1,5,10], include_lowest = True) # 첫번째 값을 최솟값에 포함하기 위해 최솟값의 범위 변경
pd.cut(s1, bins = [1,5,10], include_lowest = True,labels = ['A','B'])    # 그룹의 이름 부여


#[연습문제]
#subway2 파일을 읽고 각 역 별 승,하차 오전/오후 인원 수 출력
sub = pd.read_csv('subway2.csv',skiprows = 1, engine = 'python')

# 역 이름 NA 치환 
sub['전체'] = sub['전체'].fillna(method = 'ffill')

# 멀티 인덱스 설정
sub = sub.set_index(['전체','구분'])

# 천단위 구분기호 제거(전 범위)
sub = sub.applymap(lambda x : int(x.replace(',','')))

# 컬럼 명 숫자형 시간 정보로 변경
sub.columns = sub.columns.str[:2].astype('int')

# 시간정보(컬럼) stack 처리
sub2 = sub.stack()

# 인덱스의 컬럼화
sub3 = sub2.reset_index()
sub3.columns = ['역', '구분', '시간', '인원수']

# 시간 컬럼 오전, 오후 변경
sub3['시간대'] = pd.cut(sub3['시간'], bins = [0,12,24], include_lowest = True, labels = ['오전','오후'])

# pivot
sub3.pivot_table(index = ['역','구분'], columns = '시간대', values = '인원수', aggfunc = sum)

#[참고 - multi index에서 특정 level 선택 (get_level_values(위치,이름))]
sub2.index.get_level_values(2)

####
df1 = pd.read_csv('subway2.csv', engine = 'python', skiprows=1)
df1.iloc[:,0] = df1.iloc[:,0].fillna(method = 'ffill')
df1 = df1.set_index(['전체','구분'])
df1.columns = df1.columns.str[:2].astype('int')

# 하차
df2= df1.xs('하차',axis = 0, level = 1)
 
df2.columns = pd.cut(df2.columns, bins = [4,12,25], labels = ['오전','오후'])
df2.xs('오전',axis = 0, level = 0).sum()

df2.loc[:,'오전'].apply(sum, axis = 1)
df2.loc[:,'오후'].apply(sum, axis = 1)

# 승차
df3 = df1.xs('승차',axis = 0, level = 1)

df3.columns = pd.cut(df3.columns, bins = [4,12,25], labels = ['오전','오후'])

df3.loc[:,'오전'].apply(sum, axis = 1)
df3.loc[:,'오후'].apply(sum, axis = 1)


# =============================================================================
# groupby() , 메서드
# =============================================================================
 # 분리 - 적용 - 결합
# 특정 컬럼의 값 또는 인덱스를 group화
 # groupby만 적용시 분리만 수행, 별도의 적용함수로 전달
 
emp = pd.read_csv('emp.csv')
emp.groupby('DEPTNO')               # 출력 X, 분리데이터 셋 저장만 한 상태
emp.groupby('DEPTNO').sum()         # 숫자 컬럼 전체 연산 대상
                                    # groupby 컬럼은 인덱스로 출력

emp.groupby('DEPTNO')['SAL'].sum()     # 연산 컬럼 선택 (Series 출력)
emp.groupby('DEPTNO')[['SAL']].sum()   # 연산 컬럼 선택 (DataFrame 출력)

emp.groupby('DEPTNO')['SAL','COMM'].sum() # 여러개 컬럼 연산 시  (그룹 - 연산), 모든 데이터 그룹지어 연산해 처리 속도 느려진다.
emp['SAL'].groupby('DEPTNO').sum()      # key error
emp['SAL'].groupby(emp['DEPTNO']).sum()   # 연산 컬럼 먼저 호출 시(연산 - 그룹)
emp.groupby(['DEPTNO','JOB'])[['SAL']].sum() # 여러 컬럼 groupby시


emp2 = emp.groupby(['DEPTNO','JOB'])[['SAL']].sum() 
emp2.groupby(level = 0).mean()            # index의 특정 레벨 groupby 가능

## [참고 : index화 시킨 groupby 컬럼을 다시 컬럼으로 배치]
emp.groupby('DEPTNO')[['SAL']].sum().reset_index()
emp.groupby('DEPTNO',as_index=False)[['SAL']].sum()


# groupby 수행 시 여러 연산 함수 전달. agg()
emp.groupby('DEPTNO')[['SAL']].sum().agg(['sum','mean'])
emp.groupby('DEPTNO')[['SAL','COMM']].sum().agg(['sum','mean'])
emp.groupby('DEPTNO')[['SAL','COMM']].sum().agg({'SAL':'sum','COMM':'mean'})  # 컬럼별 서로 다른 함수 전달

#in oralce)
#select sum(sal), mean(comm)
#  from emp 
# group by deptno;

#in R)
#ddply(emp, .(DEPTNO), summaries, SAL = sum(SAL), COMM = mean(COMM))

#연습문제)
#1. sales 데이터 불러와서
sales = pd.read_csv('sales.csv', engine = 'python')
pro = pd.read_csv('product.csv', engine = 'python')

#1) 각 날짜별 판매량의 합계 출력
sales.groupby('날짜')['판매량'].sum()

#2) 각 code별 판매량 합계 출력
sales2 = pd.merge(sales,pro)
sales['qty']*sales2['qty']*sales2['price']
sales2.groupby(['date','code'])[['sum']].sum()


#3) product 데이터를 이용해 각 날짜별, 상품별 매출의 합 출력
sales2 = pd.merge(sales,pro)
sales['qty']*sales2['qty']*sales2['price']
sales2.groupby(['date','code'])[['sum']].sum()

# 사용자 정의 그룹핑**
df1 = DataFrame(np.arange(1,26).reshape(5,5), columns = ['a','b','c','d','e'])

# 1) 각 행/컬럼 별 그룹명 리스트로 순차적 전달 => 같은 그룹이름 별로 묶임
df1.groupby(['g1','g1','g2','g2','g2']).sum()         # index

df1.groupby(['g1','g1','g2','g2','g2'],axis=1).sum()  # columns

# 2) 각 행/컬럼명에 매칭되는 딕셔너리 형식으로 전달
df1.groupby({'a':'g1','b':'g1','c':'g2','d':'g2','e':'g2'},axis=1).sum() # dict 형식으로 전달 가능

#[연습문제]
#2. delivery파일을 읽고 
deli = pd.read_csv('delivery.csv', engine = 'python', parse_dates=['일자'])
deli.dtypes

de = pd.read_csv('delivery.csv', engine = 'python')
#1) 요일 / 업종별 통화건수 총 합 출력
from datetime import datetime
deli['요일'] = deli['일자'].map(lambda x : x.strftime('%A')).str.upper()
deli['통화건수'].groupby(deli[['요일','업종']]).sum() # 불가, 
deli.groupby(['요일','업종'])['통화건수'].sum()       # 가능, groupby 컬럼이 많아질 경우 나열해야한다.
# [] Series / [[]] DataFrame

de.groupby(['일자','업종'])['통화건수'].sum()

#2) 평일, 주말(금/토/일) 각 그룹별 시군구 통화건수 총 합 출력
deli2 = deli.groupby(['요일','시군구'])['통화건수'].sum().unstack()   #  Series Valuse로 통화건수 배치된다.
deli.groupby(['요일','시군구'])[['통화건수']].sum().unstack()         # 비추 ,통화건수컬럼 살아있어(데이터프레임) 인덱스 값이 하위 레벨로 배치된다.(멀티컬럼)

deli2.groupby(['평일','평일','주말','주말','평일','평일','평일']).sum()

#[참고 - 딕셔너리 생성 시 하나씩 매핑 모두 전달]
{'monday':'평일','TUESDAY':'평일',...,'SUNDAY':'주말'}  # 하나씩 매핑 가능 
{['monday','TUESDAY']:'평일',,...,['SUNDAY']:'주말'}    # 리스트로 동시 매핑 불가


# 3) cutting object 전달
#예제) emp 데이터에서 각 연봉의 등급별 연봉 평균 출력
#단, 연봉의 등급은 3000이상 A, 1500이상 B, 미만은 c  [이상 / 미만)
# [0,1500), [1500,3000), [3000, ~ )  * right = False

c1 = pd.cut(emp['SAL'],[0,1500,3000,10000], right = False, labels = ['C','B','A'])

emp.groupby(c1)['SAL'].mean() # 함수를(cut) 사용해 행별로 그룹명 가공하는 방법


# 3 student, exam_01 파일을 읽고
#1) 각 성별 A,B,C그룹에 해당되는 학생 수 (count) 출력
# 단, A그룹은 시험 성적이 90이상, B그룹은 70이상, C그룹은 나머지
stu = pd.read_csv('student.csv', engine = 'python')
ex = pd.read_csv('exam_01.csv', engine = 'python')
std2= pd.merge(stu,ex, on = 'STUDNO')

std2['JUMIN'].str[6]                  # error, JUMIN value => int type이므로 str 사용 불가
std2['JUMIN'].astype('str').str[6]    # 앞이 Series이므로 astype사용, str로 형 변환

v1 = std2['JUMIN'].astype('str').str[6].replace({'1':'남','2':'여'})  # replace -> dict으로 여러 인자 변환 가능
c1 = pd.cut(std2['TOTAL'],[0,70,90,101],right = False, labels = ['C','B','A'])

std2.groupby([v1,c1]).count()
std2.groupby([v1,c1])['STUDNO'].count()

# =============================================================================
# groupby의 tranform 메서드
# =============================================================================
# - R의 ddply 내부함수 transform과 유사 
# - transform : 기존 데이터 프레임 행 갯수 유지하며 행마다 그룹 정보 출력
 
emp.groupby('DEPTNO')['SAL'].mean()             # 요약정보
emp_1 = emp.groupby('DEPTNO')['SAL'].transform('mean')  # 전체 행 기준 그룹핑 정보

emp.join(emp_1,lsuffix = '_x', rsuffix = '_y')  # 중복된 컬럼은 접미어 붙여줘야 연산 가능하다.(중복된 컬럼에 추가 문자 삽입 필요)

pd.merge(emp, emp_1, left_index = True, right_index = True) # 위와 같은 결과 출력 / 중복된 컬럼에 알아서 추가문자 삽입된다.

## groupby의 apply 메서드로 사용자 정의 함수 전달.
# = groupby의 사용자 정의 함수(apply로 수행)

f1 = lambda x : x.sum()

emp.groupby('DEPTNO')['SAL'].sum()
emp.groupby('DEPTNO')['SAL'].apply(f1)

#[예제 : 데이터프레임을 전달 받아 SAL 컬럼 역수 정렬, 가장 큰 2개 행 추출 함수 생성]
f_sort = lambda x : x.sort_values('SAL',ascending = False)[:2]

#1) 전체에서 SAL이 큰 두 명 출력
emp.sort_values('SAL',ascending = False)[:2]
emp.sort_values('SAL',ascending = False).iloc[:2,:] # 슬라이스 색인 : 행 우선 순위 추출로 메서드 없어도 추출 가능하다

#2) 부서별 SAL이 큰 두 명 출력
emp.groupby('DEPTNO').apply(f_sort)

emp.groupby('DEPTNO',group_keys = False).apply(f_sort)  # group_keys= False : groupby 컬럼 사라진다(groupby 컬럼이 함수의 결과와 중복된 경우 사용)

#[참고 - group_keys= False 옵션의 사용]
#  groupby 연산 결과와 groupby 컬럼이 중복일 경우
# 종종 key 중복으로 groupby 연산 자체에 에러 발생할 수 있음
# 이 경우 본문에 있는 groupby 연산 컬럼의 index로의 출력을 방지하고 출력 할 수 있다.

