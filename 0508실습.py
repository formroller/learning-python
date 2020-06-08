run profile1
# =============================================================================
# # 1. card_history.csv파일을 읽고
# =============================================================================
df1 = pd.read_csv('card_history.csv',engine = 'python')

######
card = pd.read_csv('card_history.csv',engine = 'python')
card = card.iloc[:,1:]
card = card.applymap(lambda x : int(x.replace(',','')))
# 1) 2018년 1월 1일부터 매주 일요일에 기록된 자료 가정, 인덱스 생성
nrow = df1.shape[0]
vdate = pd.date_range('2018/01/01', periods = nrow, freq = 'W-sun')
df1.index = vdate
df1 = df1.drop('NUM',axis = 1)

########
card.shape
card.index = pd.date_range('2018/01/01',periods = card.shape[0],freq = 'W')

# 2) 월별 각 항목의 지출 비율 출력
df1['식료품'].applymap(lambda x : int(x.replace(',','')))  # Series는 applymap 사용 불가 - map 사용
df1['식료품'].map(lambda x : int(x.replace(',','')))

df1 = df1.applymap(lambda x : int(x.replace(',','')))
df2 = df1.resample('M').sum()

df2.apply(lambda x : x / x.sum() * 100, axis = 1)

######
card1 = card.resample('M').sum()
card2 = (card1 + card1.shift(1))/card1.shift(1)

# 3) 일별 데이터로 변경하고, 각 일별 지출내용은 하루 평균 지출값으로 나타낸다
# 예) 1월 7일 14000원이면 1월 1일~ 1월 7일 각 2000원씩 기록
df1.resample('D').asfreq()  # 1월 7일 이후 데이터 출력 (다운 샘플링일 경우 resample이 좋다) / 1월 1~6일 데이터 출력 불가

vidx = pd.date_range('2018/01/01', '2018/07/29')  # 업샘플링은 reindex가 용이
df3 = df1.reindex(vidx)

(df3.iloc[:7]/7).fillna(method = 'bfill')
(df3/7).fillna(method = 'bfill')

########
a1 = card1.resample('7D').mean()
a1.fillna(method = 'ffill')

# =============================================================================
# # 2. 병원현황.csv 파일을 읽고
# =============================================================================
df4 = pd.read_csv('병원현황.csv', engine = 'python', skiprows = 1)

df4 = df4.set_index(['시군구명칭','표시과목'])
df4 = df4.drop(['항목','단위'],axis = 1)

c1 = df4.columns.str[:4]
c2 = df4.columns.str[6]

df4.columns = [c1,c2]
df4 = df4.drop('계',axis = 0, level = 1)

#############
hos = pd.read_csv('병원현황.csv', engine = 'python', skiprows = 1)
hos = hos.drop(hos.loc[:,['항목','단위']], axis = 1)
hos = hos.loc[hos['표시과목'] != '계',:]
#NA 치환

hos = hos.set_index(['시군구명칭','표시과목'])

year = hos.columns.str.findall('[\d]+').str[0]
qty = hos.columns.str.findall('[\d]+').str[1]

hos.columns = [year,qty]

# 1) 구별 년도별 각 표시과목(진료과목)의 이전년도 대비 증가율 출력
# (단, 각 데이터는 누적데이터로 가정)  / 대비 :shift
df4.xs(4,axis = 1, level = 1)  # key error (컬럼 - 문자/ 문자,숫자 구분하기 때문)
df5 = df4.xs('4',axis = 1, level = 1)
df5 = df5.astype('float')

df5.shift(-1, axis = 1)   # -1 앞으로 당겨온다.
((df5 - df5.shift(-1, axis = 1)) / df5.shift(-1, axis = 1) *100).fillna(0)

# 2) 구별 년도별 병원이 생성된 수를 기반,
# 가장 많은 병원을 각 구별로 5개씩 병원수와 함께 출력
df6 = df5 - df5.shift(-1, axis = 1)

df6.stack() # 년도 stack 처리
df7 = (df6.stack()).groupby(level = [0,2,1]).sum()   # Series는 컬럼 선택 X
f1 = lambda x : x.sort_values(ascending = False)[:5]
df7.groupby(level = [0,1], group_keys = False).apply(f1)
