run profile1

# =============================================================================
# ## 최대/최소를 갖는 인덱스 리턴 메서드(whichmax, whichmin in R)
# =============================================================================
## 1. numpy의 argmax, argmin
# - array 적용 가능 (다차원 가능)
# - Series 적용 가능 (idxmax로 대체 추천), DataFrame에는 적용 불가
# - axis 사용해 행/열 별 최대/최소를 갖는 위치값 리턴

## 2. pandas의 idxmax, idxmin
# - Series, DataFrame 적용 가능
# - axis를 사용해 행,열별 최대/최소를 갖는 index값 리턴
 
# 예제) 다음의 배열, 데이터프레임에서 각각 최댓값을 갖는 위치/index 리턴

arr1 = np.array([[3,2,9],[10,2,1],[2,4,3]])
df1 = DataFrame(arr1)

arr1.argmax(axis = 0)
arr1.argmax(axis = 1)

df1.iloc[:,0].argmax() # 연산 가능, 추천X
df1.argmax()           # 연산 불가, DataFrame 적용 불가

df1.iloc[:,0].idxmax() # 연산 가능, Series 적용 가능 (최댓값 갖는 index)
df1.idxmax(axis = 0)   # 연산 가능, DataFrame 적용 가능



# =============================================================================
# ## replace 메서드(치환 메서드)
# =============================================================================
## 1. 문자열 메서드 형태 (기본 파이썬 제공)
 - 'abc'.replace('a','A')
 - 문자열 치환이므로 첫번째 인자(old value)에는 문자열만 올  수 있음
 - 문자열 리턴이므로 두번째 인자(old value)에는 문자열만 올  수 있음
 - 숫자, NA값의 치환 불가
 - 숫자, NA값으로 리턴 불가
 - 벡터연산 불가 -> 적용 함수 필요
 
## 2. pandas 값치환 메서드 형태(pandas 제공)
 - df1.replace(100,1000)
 - 첫번째 인자(old value)와 정확히 일치하는 값을 두번째 인자(new value)로 리턴
 - 값 치환이므로 숫자, NA값의 치환 가능
 - 숫자, NA값으로 리턴 가능
 - 벡터 연산 가능(Series, DataFrame 적용 가능)
df1.iloc[0,:].replace


## 2-1) pandas 문자열 메서드 형태(pandas 제공)
 - Series(['abc','bcd']).str.replace('a','A')
 - 문자열의 일부(패턴) 치환만 가능, 값 치환 불가
 - 문자열 메서드 형태와 기능 동일, 벡터연산 가능(Series만 적용 가능)
 
#[예제]
df1 = DataFrame({'a':[10,NA,9,1], 'b':['abc','bcd','efc','add']})

#1) 10의 값을 100으로 수정 (값 치환)
df1.replace(10,100)

#2) NA값을 0으로 수정 (값 치환)
df1.replace(NA,0)

#3) d를 D로 수정 (시험문제)
# (치환 가능 )
df1['b'].str.replace('d','D')               # 벡터연산 가능
df1['b'].map(lambda x : x.replace('d','D')) # 벡터연산 불가, map 적용 필요
df1['b']= Series(df1.iloc[:,1]).str.replace('d','D')

# (치환 불가)
df1.replace('d','D')             # 치환 불가
df1.str.replace('d','D')         # 치환 불가, str메서드는 데이터프레임 적용 불가

# =============================================================================
# ## multi-index 
# =============================================================================
# - index가 계층(level)적 구조를 갖는 경우
# - 상위레벨(level= 0), 하위레벨(level = 1, ...)
# - index, columns 모두 설정 가능
 
# =============================================================================
# # 1. multi-index 생성
# =============================================================================
#         col1    col2
# A    a    1       2
#      b    3       4  A가 있으므로 생략되었다.
# B    a    6       6
#      b    7       8

# 멀티 인덱스
df1 = DataFrame(np.arange(1,9).reshape(4,2))     
df1.index = [['A','A','B','B'],['a','b','a','b']]
df1.columns = ['col1','col2']

df1.index  # MultiIndex
df1.index.names = ['상위인덱스','하위인덱스']  # 'A','B' : 상위 인덱스 / 'a','b' 하위 인덱스

# 멀티 인덱스 - 컬럼

df2 = DataFrame(np.arange(1,17).reshape(4,4))
df2.index = [['A','A','B','B'],['a','b','a','b']]
df2.columns = [['col_a','col_b','col_a','col_b'],
               ['col1','col2','col3','col4']]

# =============================================================================
# # [연습문제 - multi-index 파일을 읽고 멀티 인덱스 설정]
# =============================================================================
df3 = pd.read_csv('multi_index.csv', engine = 'python')

# setp1) 첫번째 컬럼(지역) NA치환
df3.iloc[:,0] = df3.iloc[:,0].fillna(method = 'ffill')

# setp) 1,2 컬럼 멀티인덱스 처리
df3 = df3.set_index(['Unnamed: 0','Unnamed: 1'])

# step3) column값 변경 -> 냉장고 냉장고 TV TV
a1 = df3.columns.map(lambda x : np.where('Unnamed' in x, NA, x)) 
a1.fillna(method = 'ffill')
# => np.array 결과가 array로, 하나의 데이터 타입만 허용(문자형으로 출력)

a2 = df3.columns.map(lambda x : NA if 'Unnamed' in x else x )
#=> 문자, NA 그대로 출력 (list - 서로 다른 데이터 타입 허용) / fillna 메서드 사용 가능
df3.columns = Series(a2).fillna(method = 'ffill')

# step4) 멀티 컬럼 설정
df3.columns = [df3.columns, df3.iloc[0,:]]

# setp5) 첫번째 행 제거
df3.iloc[0,:]

df3 = df3.drop(NA,axis = 0, level = 0)
# drop은 행이나 컬럼을 제거할 수 있는  제거 메서드 (이름을 전달받는다.)
# 멀티 인덱스 중 어느 level을 지울 것인지 추가 인자 전달해야한다.

# step6) index / column 명 변경
df3.index.names = ['지역','지점']
df3.columns.names = ['품목','구분']


###
df4 = pd.read_csv('multi_index.csv', engine = 'python')

# 멀티인덱스 설정

df4.iloc[:,0] = df4.iloc[:,0].fillna(method = 'ffill') # 첫번째 컬럼만(조건) 치환
df4 = df4.set_index(['Unnamed: 0','Unnamed: 1'])

#df4 = df4.fillna(method = 'ffill')
#df4 = df4.set_index([df4.iloc[:,0],df4.iloc[:,1]])  *set_index[컬럼명], 위치 기반시 기준 컬럼 없어지지않는다.

df4.index.names = ['지역','지점']


# 멀티 컬럼 설정
df4.columns
a3 = df4.columns.map(lambda x : NA if 'Unnamed' in x else x)
df4.columns = Series(a3).fillna(method = 'ffill')
df4.columns = [df4.columns,df4.iloc[0,:]]

df4 = df4.drop(NA, axis = 0, level = 1)
df4.columns.names = ['품목','구분']


# =============================================================================
# # 2. multi-index 색인
# =============================================================================
# - ix, loc, iloc : 기본은 상위 레벨의 값만  색인 가능
# - ix, loc, iloc : 튜플 전달시 하위 레벨의 값 색인 가능
# - xs : 하위 레벨 직접 색인 가능한 메서드

df3['냉장고']  # 상위 레벨의 컬럼은 키 색인으로 추출 가능
df3['price']   # 하위 레벨의 컬럼은 키 색인으로 추출 불가

# (컬럼)
df3.loc[:,'냉장고'] # 가능
df3.loc[:,'price']  # 불가, key error

# (인덱스)
df3.loc['seoul',:]  # 가능
df3.loc['A',:]      # 불가

# 예) 모든 품목의 price 선택
df3.xs('price',     # 이름
       axis = 1,    # 색인 방향(index : 0 / columns :1), 0가 디폴트
       level = 1)   # 인덱스 level(상위:0 / 하위 : 1) , 0가 디폴트

# 예) A 지점의 price 선택
df3.xs('price', axis = 1, level = 1).xs('A',axis = 0, level = '지점')


# 예) seoul의 B 지점 선택
df3.loc[('seoul','B'),:] # 튜플 전달시 하위 레벨의 값 색인 가능

# 예) 냉장고의 price 선택
df3.loc[:,('냉장고','price')]
df3.iloc[:,0]

# 예) seoul의 B선택
df3.iloc[1,:]


#예) 냉장고의 price, TV의 qty 선택
df3.iloc[:,[0,3]]
df3.loc[:,[('냉장고','price')],[('TV','qty'])]
df3.loc[:,[('냉장고','price'),('TV','qty')]]

# =============================================================================
# 1. multi_index_ex1.csv 읽고 다음 수행
# =============================================================================
df1 = pd.read_csv('multi_index_ex1.csv', encoding = 'cp949')

#1) 각 인덱스와 컬럼을 multi-index를 갖도록 설정
df1 = pd.read_csv('multi_index_ex1.csv', encoding = 'cp949')

# 1-1. 멀티컬럼 설정
df1.columns = [df1.columns.map(lambda x : x[:2]), df1.iloc[0,:]]

# 1-2.첫번째 행 제외
df1 = df1.iloc[1:,]
df1.drop(0, axis = 0)

# 1-3.멀티 인덱스 설정
df1.index = [df1.iloc[:,0],df1.iloc[:,1]]
df1 = df1.iloc[:,2:]

# 1-4. 인덱스명 설정
df1.index.names = ['구분','상세']
df1.columns.names = ['지역','지점']


#2) 서울지역 컴퓨터  판매량 출력
df1 = df1.astype('int')
df1.loc['컴퓨터','서울']


#3) 서울지역 컴퓨터의 세부항목별 판매량의 합계 출력
df1.loc['컴퓨터','서울'].sum(1)
df1.loc['컴퓨터','서울'].apply(sum,1)

#4) 지역별 A지점의 TV 판매량 출력
 .xs('A', axis = 1, level = 1).xs('TV', axis = 0, level = 1)

#5) 지역별 C지점의 모바일 세부 항목별 판매량 평균 출력
df1.xs('C', axis = 1, level = 1).loc['모바일',:].mean()

#6) 서울 'A'지점의 노트북 판매량 출력
df1.loc[:,('서울','A')]
df1.iloc[:,0]

# =============================================================================
# ## 3.산술연산
# =============================================================================
#1) multi-index의 axis 전달 시 
# =>  multi-index와 상관없이 각 행/열 별 연산
df1.sum(0)
df1.sum(1)

#2) multi-index의 axis,level 전달 시 
# => multi-index의 각 레벨이 같은 값별로 묶어 그룹연산 (행/열별 전달 가능)
#예) 지역별 판매량 총 합
df1.sum(1, level = 0)
#예) 지점별 판매량 총 합
df1.sum(1, level = 1)
#예) 구분(컴퓨터, 가전, 모바일)별 판매량 총 합
df1.sum(0, level=0)

# =============================================================================
# #4. multi-index의 축 치환 및 정렬
# =============================================================================
df1.swaplevel(0,1, axis = 1)  # 지역이 같은 값끼리 묶이지 않음.

# 다음과 같은 형식으로 인덱스 인자 전달 후 swaplevel을 수행해야함
서울  경기  강원  서울  경기  강원  서울  경기  강원
 A     A     A     B    B     B     C     C     C
 
 
df1.sort_index(axis = 1, level = 1).swaplevel(0,1, axis = 1)
