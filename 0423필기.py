# 외부 파일 입출력 함수
pd.read_csv(file,         # 파일명
            sep=',',      # 분리구분기호
            header=,      # 첫 번째 행을 컬럼화 할지 여부, None설정시 value로 전달
            names=,       # 컬럼이름 변경
            index_col=,   # index 설정 컬럼
            usecols=,     # 불러올 컬럼 전달
            dtype=,       # 불러올 데이터 타입 전달, 딕셔너리로 각 컬럼별 전달 가능
            engine=,      # 'python' 주로 사용(한글, 맨끝라인 처리 가능)
            skiprows=,    # 제외할 행 전달
            nrows=,       # 불러올 행 개수 전달
            na_values=,   # NA 처리할 문자열
            parse_dates=, # 날짜 파싱할 컬럼 전달
            encoding=)    # 인코딩 옵션

pd.read_csv('read_test.csv', parse_dates=['date'])
pd.read_csv('read_test.csv', header=None, names=['A','B','C','D','E'])
pd.read_csv('read_test.csv', index_col='date')
pd.read_csv('read_test.csv', usecols=['date','a'])

pd.read_csv('read_test.csv', dtype='str')
pd.read_csv('read_test.csv', dtype={'a':'str','d':'float'}).dtypes

pd.read_csv('read_test.csv', na_values=['.','-','?','!'])
pd.read_csv('read_test.csv', na_values={'a':['.','-'],
                                        'b':['?','!']})


pd.read_csv('read_test.csv', nrows=5)
pd.read_csv('read_test.csv', skiprows=5)      # 정수 전달시 행 수로 전달
pd.read_csv('read_test.csv', skiprows=[1,5])  # 리스트 전달시 행 번호로 전달

# 적용함수
1. map 함수
- 1차원 데이터 셋(list, array, Series) 적용 가능
- 리스트로 출력 필요
- map(func, *iterables) : 함수가 필요로하는 추가 인자 전달 가능 

2. map 메서드
- 1차원 데이터 셋(Series, index object) 적용 가능
- df1.col1.map(arg, na_action=None) : 함수가 필요로하는 추가 인자 전달 불가

3. apply 메서드
- 2차원 데이터 셋(DataFrame) 적용 가능, 행별 열별 연산 수행
- 적용함수에 Series 형태(그룹)로 데이터를 전달, 그룹함수와 잘 어울림
- df1.apply(func, axis=0, **kwds) : 함수가 필요로하는 추가 인자 전달 가능

4. applymap 메서드
- 2차원 데이터 셋(DataFrame) 적용 가능, 원소별 연산 수행
- df1.applymap(func) : 함수가 필요로하는 추가 인자 전달 불가

# 예제) 다음의 데이터 프레임에서 col1 컬럼 천단위 구분기호 제거
df1 = DataFrame({'col1': ['1,100','1,200','1,300'], 
                 'col2': ['2,200','3,300','4,400']})


df1 = df1.applymap(lambda x : int(x.replace(',','')))
df1.dtypes

# 예제) test3.txt를 불러온 뒤 년도별 총 합 구하기
np.loadtxt('test3.txt')              # 공백, 탭 자동 분리
pd.read_csv('test3.txt', sep='\t')   # 분리구분기호 탭 전달
df2 = pd.read_csv('test3.txt', sep='\s+', header=None)

f2 = lambda x : x + '년'
df2.index = Series(np.arange(2000,2014)).astype('str').map(f2)

df2.apply(sum, axis=1)
df2
df2.columns = ['1월','2월','3월','4월','5월']

# [ 연습 문제 ]
# top(data, n=5) 함수 생성, 위 데이터에서 각 년도별 값이 큰 2개 월 출력
# (단, 사용자가 n의 값을 전달할 수 있도록)

        0      1
2000년  1월   2월
2001년  1월   2월











