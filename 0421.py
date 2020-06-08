run profile1

#Series 색인
s1 = Series([1,2,3,4], index = ['a','b','c','d'])

s1[0]       # positional indexing
s1['a']     # label indexing
s1[0:2]     # slice indexing
s1[[0,2]]   # list indexing (= feny indexing)
s1[s1 > 2]  # boolean indexing

# pandas NA 확인함수

s2 = Series([NA,2,3,4], index = ['a','b','c','d'])

s2.isnull()     # 메서드 형식
s2.notnull()

pd.isnull(s2)   # 함수 형식
pd.notnull(s2)   


# =============================================================================
# # DataFrame
# =============================================================================
# - 행과 열을 갖는 2차원 구조
# - 서로 다른 데이터 타입 허용, 한 컬럼은 같은 데이터 타입만 허용
# - Key 값은 column 사용
 
#1. 생성
d1 = {'col1':[1,2,3,4], 'col2':[5,6,7,8]}
arr1 = np.arange(1,9).reshape(4,2)

df1 = DataFrame(d1)
df2 = DataFrame(arr1, index = ['a','b','c','d'], columns = ['col1','col2'])

DataFrame(df1, columns = ['COL1','COL2'])  # NA 출력, columns에 있는 값만 출력하라는 의


#2. 기본 메서드
df1.index
df1.columns
df1.dtypes    # 각 컬럼의 데이터 타입 확인, oracle의 desc, R의 str과 비슷
df1.values    # key값 제외, 데이터들만 배열 형식 출력

#3. index 수정
df1.index = [1,2,3,4]
df1.index.name = 'month'      # 인덱스 설명 표시
df1.columns.name = 'columns'  # 컬럼에 의미 부여
df1.name = 'DataFrame'
df1.dtypes

#4. 색인
df1['col1']   # key indexing
df1.col1      # key indexing, (= df1$col1 in R)

df1[0:3]      # slice 값 색인 전달시 행 우선순위 , 색인 가능(선호하지 않음)

df1[0,0]      # 각 행/열 의 번호, 이름 전달 불가, 색인 불가

df1

# iloc, 위치값
df1.iloc[0,0]       # 위치값, positional indexing 
df1.iloc[0,:]
df1.iloc[0:3,0]
df1.iloc[[0,1],[0,1]]

# loc, 이름
df1.loc[1,'col1']   # 이름, label indexing [index명,colums명]
df1.loc[df1.col1 > 3,:]  # 조건 색인은 loc로
df1.loc[df1.col1 > 3]
df1[df1.col1 > 3]



# ix, 위치값과 label(이름) 동시 사용 가능 
df1.ix[1,'col1']     # 1은 행이름으로 해석
df1.ix[1,0]          # 1은 행이름, 0은 컬럼 위치

df3 = DataFrame(np.arange(1,9).reshape(4,2))
df3.ix[0,0]         # 행 이름이 없는 경우 위치값으로 해석

# 삭제
df1
df1.iloc[-1,:]  # 마지막 행 출력
df1.iloc[1:,:]  # 첫 행 제외 후 출력

df1.drop('col1',axis= 1)  # 컬럼 제외
df1.drop(1,axis= 0)       # 행 제외
df1.drop(0,axis= 1)       # 위치값 전달 불가, 이름값만 전달 가능

# =============================================================================
# #[연습문제], 시험문제!!
# =============================================================================
#데이터 프레임 생성
d2 = {'name':['apple','mango','banana','cherry'], 'price':[2000,1500,500,400], 'qty':[5,4,10,NA]}
df2 = DataFrame(d2)

#1.mango의 price, qty 선택
df2.iloc[1,[1,2]]
df2.iloc[1:2,1:3]  # slice 형식으로 전달하면 차원축소 방지된다.

df2.loc[1,['price','qty']]


#2.mango,cherry의 price선택
type(df2.iloc[[1,3],1:2])   # dataframe, 차원축소.
type(df2.iloc[[1,3],1])     # series, 차원축소.

df2.loc[[1,3],:]

#3. 전체과일의 price만 선택
df2.loc[:,'price':'price'] # 차원축소 방지, 문자부터 문자까지(이름슬라이싱) 'price':'qty'(마지막 범위 포함), dataframe
df2.loc[:,'price']         # 차원 축소, 시리즈 출력

df2.iloc[:,-2]
df2.price

#4. qty평균
df2.qty.mean()   # NA를 무시, 3개 값의 평균만 구함. pd.mean 
np.mean(df2.qty) # pd.mean 호출 

# =============================================================================
# #[참고]
 arr1 = np.array([5,4,10,NA])
 
 arr1.mean()                       # nan, np.mean 호출 -> null 무시 못 한다.
 Series(arr1).mean()               # 6.33, pd.mean 호출 -> null 무시.
 Series(arr1).mean(skipna=False)   # nan, pd.mean 호출 -> null 무시 못 한다.
 
 df2.qty.mean?
# 
# =============================================================================

#5. price가 1000 이상인 과일명 출력
df2.loc[df2.price >= 1000,'name']


df2.loc[df2.price >= 1000,:]

#6. cherry, banana, mango, apple순 출력
df2.iloc[[3,2,1,0]]  # 위치값 기반


#7. qty -> QTY 수정 ** 

# 7-1) 일부 수정
df2.columns[2] = 'QTY'  # index object 수정 불가
df2.columns.values[2] = 'QTY' # 수정 가능하나, 추천X

# => QTY 수정했으나 index object에 반영이 안될경우 NaN 출력된다.(종종 발생한다)
# => 새로운 index로 복사해 덮어쓸 경우 위 문제 발생하지 않는다.
 #  위 수정방식은 index object에 반영이 되지 않기때문에 
 #  데이터 프레임의 index와 index object의 값들의 불일치 발생할 수 있다.


# 7-2) 전체 덮어쓰기 (index object 수정 방식)
a1= df2.columns.values
a1[2] = 'QTY'
df2.columns = a1


# 7-3)rename 메서드
df2.rename({'price':'Price'}, axis = 1)


#8. name에 'a'를 포함하는 행 출력
f1 = lambda x : 'a' in x

vbool = list(map(f1,df2.name))

df2.loc[vbool,:]

#in 연산자 => 문자열 : 문자열 시 포함 연산자로 취급
# a. 문자열 : 문자열
df2.name in 'a'  # 불가
'a' in 'apple'    # apple에 'a'패턴 포함 여부
'a' in 'cherry'

# b. 문자열 : list
'b' in ['bc','bd']                     # 'b' == 'bc' or 'b' == 'bd', 벡터연산 불가
np.in1d(np.array(['b']),['bc','bd'])   # 'b' == 'bc' or 'b' == 'bd', 벡터연산 가능


# =============================================================================
# #[연습문제] 시험!!
d2 = {'name':['apple','mango','banana','cherry'], 'price':[2000,1500,500,400], 'qty':[5,4,10,NA]}
df1 = DataFrame(d2)
# #1. df1의 이름이 apple 또는 cherry인 행을 선택 (in / in1d 연산자 사용)
'apple' in ['apple','cherry']

f1 = lambda x :  x in ['apple','cherry']         # 기본 in 연산자, mapping 필요
vbool = list(map(f1,df1.name))
df1.loc[vbool,:]

df1.loc[np.in1d(df1.name,['apple','cherry']),:] # in1d, numpy용 in 연산자

df1.loc[df1.name.isin(['apple','cherry']),:]    # isin, pandas용 in 연산자

# #2. name에 'o' 포함된 행 선택
f2= lambda x : 'o' in x
vbool1 = list(map(f2,df1.name))
df1.loc[vbool1,:]

# =============================================================================


#9. name값을 rowname으로 설정 후 name 컬럼 제외
df2.index = df2.name
df2 = df2.drop('name',axis = 1)

df2.index = df2.name
df2.drop('name',axis = 1)


#10. apple과 cherry 행 삭제
df2 = df2.drop(['apple','cherry'], axis = 0)
df2


# 5. 구조 수정
# 1) row 추가
# 2) column 추가

# 6. 산술연산









