run profile1
#[연습문제 - 위 데이터에서 ]
a1 = np.loadtxt('test3.txt')
df1 = DataFrame(a1)
df1

df1.columns=['20대','30대','40대','50대','60세이상']
np.arange(2000,2014)

f1 = lambda x : str(x)+'년'
df1.index = list(map(f1,np.arange(2000,2014)))

#1. 2000년 기준 증감률
df1.dtypes

(df1 - df1.iloc[0,:]) / df1.iloc[0,:] *100

#2. 20대 기준 증감률

df1 - df1.iloc[:,0:1]                # key값 불일치 -> 브로드캐스팅 불가
df1.sub(df1.iloc[:,0:1], axis = 0)   # 불가, 20대 컬럼이 데이터프레임으로 전달
df1.sub(df1.iloc[:,0], axis = 0)     # 가능, 20대 컬럼이 시리즈로 전달

df1.sub(df1.iloc[:,0], axis = 0).div(df1.iloc[:,0], axis = 0) *100

# =============================================================================
# #[주의 - 데이터프레임의 브로드캐스팅]
# #시리즈(1차원)와 데이터 프레임(2차원)의 연산만 브로드캐스팅 가능(키 일치 시)
# #따라서 데이터프레임 끼리는 산술연산 메서드 사용해도 브로드캐스팅 전달 불가
# =============================================================================

#3. 년도별 연령대가 차지하는 실업률의 비율 (총 합 100)

f5 = lambda x : x/x.sum() * 100

df1.apply(f5, axis = 1)
df1.apply(f5, axis = 1).sum(axis = 1)

pd.read_csv(file,          # 파일명
            sep = ' ',     # 분기구분기호
            header = ,     # 첫번째 행을 컬럼화 할지 여부, None 설정시 value로 전달
            names = ,      # 컬럼명 변경
            index_col = ,  # index 설정 컬럼
            usecols = ,    # 불러올 컬럼 전달
            dtype= ,       # 불러올 데이터 타입 전달, 딕셔너리로 각 컬럼별 전달 가능
            engine = ,     # 'python' 주로 사용(한글, 맨끝 라인 처리)
            skiprows = ,   # 제외할 행 전달
            nrows = ,      # 불러올 행 갯수 전달
            na_values = ,  # NA 처리할 문자열
            parse_dates = ,# 날짜 파싱할 컬럼 전달
            encoding =)    # 인코딩 옵션

pd.read_csv('read_test.csv', parse_dates = ['date'])
pd.read_csv('read_test.csv', header = None, names = ['A','B','C','D','E',])
pd.read_csv('read_test.csv', index_col = 'date')
pd.read_csv('read_test.csv', usecols = ['date','a'])

pd.read_csv('read_test.csv', dtype = 'str').dtypes
pd.read_csv('read_test.csv', dtype = {'a':'str','c':'float'}).dtypes

pd.read_csv('read_test.csv', na_values = ['.','-','?','!'])
pd.read_csv('read_test.csv', na_values = {'a':[',','-'],
                                          'b':['?','!']})  # 컬럼별로 NA 처리 가능(dict형식)

pd.read_csv('read_test.csv', nrows = 10)
pd.read_csv('read_test.csv', skiprows = 5)      # 본문에서 5개 행 skip
pd.read_csv('read_test.csv', skiprows = [1,5])  # skip할 행 list로 선택 가능
                                                # [skiprows] 정수 전달 - 행 수 / 리스트 전달 - 행 번호
                                                

# =============================================================================
# # 적용함수 
# 1. map
#  - 1차원 데이터 셋(list,array,Series) 적용 가능
#  - 리스트로 출력 필요
#  
# map(func, *iterables) : 함수가 요구하는 추가 인자 전달 가능
#   
#  
# 2. map 메서드
#  - 1차원 데이터 셋 (Series, index object)  적용 가능
# 
# df1.col1.map(arg, na_action = None) : 함수가 요구하는 추가 인자 전달 불가
#  
# 3. apply 메서드
#  - 2차원 데이터셋(DataFrame) 적용 가능, 행/열 별 연산 수행
#  - 적용함수에 Series 형태(그룹)로 데이터 전달 (그룹함수와 잘 어울림)
# 
# df1.apply(func, axis = 0, **kwds) : 함수가 요구하는 추가 인자 전달 가능
# 
# 4. applymap 메서드
#  - 2차원 데이터셋(DataFrame) 적용 가능, 원소별 연산 수행
# 
# df1.applymap(func) : 함수가 요구하는 추가 인자 전달 불가
# df1.applymap?
# 
# =============================================================================
                                                
#예제) 다음의 데이터프레임에서 col1 컬럼 천단위 구분기호 제거
df1 = DataFrame({'col1':['1,100','1,200','1,300'],
                 'col2':['2,200','3,300','4,400']})

df1 = df1.applymap(lambda x : int(x.replace(',','')))
df1.dtypes


# 예제) test3.txt를 불러온 뒤 년도별 총 합 구하기
np.loadtxt('test3.txt')               # 공백, 탭 자동 분리
pd.read_csv('test3.txt',sep = '\t')   # 분리구분기호 탭 전달
pd.read_csv('test3.txt',sep = '\s+')  # 분리구분기호(공백) 일정하지 않을떄 사용


df2 = pd.read_csv('test3.txt',sep = '\s+', header = None)

np.arange(2000,2013).astype('str') + '년'   # 시리즈 + 스칼라 => 연산불가

f2 = lambda x : x + '년'
df2.index = Series(np.arange(2000,2014)).astype('str').map(f2)
df2.set_index # 호출

df2.apply(sum, axis = 1)
#index 가공한 데이터로 덮어씀
#set_index 컬럼 데이터를 인덱스로 전달

df1 = pd.read_table('test3.txt', header = None)
f1 = lambda x : str(x)+'년'
df1.index = list(map(f1,np.arange(2000,2013)))
df1.apply(sum, axis = 1)


df2.columns = ['1월','2월','3월','4월','5월']

#[연습문제]
# top(data, n = 5) 함수 생성, 위 데이터에서 각 년도별 값이 큰 월 2개 출력
#(단, 사용자가 n값 전달할 수 있도록)

df2.loc['2000년',:].sort_values(ascending = False)[:1].index.values

def top(data,n=5):
   return Series(data.sort_values(ascending = False)[:n].index.values)

df2.apply(top,axis = 1, n = 3) # apply 적용결과 데이터 프레임으로 보려면 Series로 변경해야한다.

###
df2.loc['2000년',:].sort_values(ascending = False)[:2]
def top(data, n):
    return data.sort_values(ascending = False)[:n]

df2.apply(top,axis = 1, n=3)















