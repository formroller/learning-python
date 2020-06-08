run profile1
# =============================================================================
# # 1. card_history.txt 파일을 읽고
# =============================================================================
card = pd.read_csv('card_history.txt', sep = '\t')
card = card.set_index('NUM')

card.str.replace(',','')  # 에러,데이터프레임(2차원)에 적용 불가 [1차원 ]

f1 = lambda x: int(x.replace(',',''))
card = card.applymap(f1)


# [참고 - python에서 replace 메서드의 여러 형태]
'1,100'.replace(',','')                         # 패턴치환 (문자열 메서드)
card.loc[:,'식료품'].replace('22,200','test')   # pd.replace, 일치 값 치환(벡터연산 가능 )
card.loc[:,'식료품'].str.replace(',','')        # .str.rplace, pandas 문자열 메서드 (문자열 메서드 벡터연산 가능)


df1 = pd.read_csv('card_history.txt', sep = '\t', index_col = 'NUM')

# 1) 각 일별 지출품목의 차지 비율 출력(식료품 : 20%, 의복 : 45%, ....)
f2 = lambda x : x / x.sum() * 100
card.apply(f2, axis = 1)

###
f1 = lambda x : int(x.replace(',',''))
df1 = df1.applymap(f1)

f2 = lambda x : str(x)+'일'
df1.index = list(map(f2, np.arange(1,31)))

f3 = lambda x : x / x.sum() * 100
df1.apply(f3,axis=1)

# 2) 각 지출품목별 일의 차지 비율 출력(1일 : 0.7%, 2일 : 1.1%, ....)
card.apply(f2, axis = 0)

df1.apply(f3,axis=0)

# 3) 각 일별 지출비용이 가장 높은 품목 출력
card.apply(top, axis = 1, n= 1)
card.iloc[0,:].argmax() # 최댓값을 갖는 인덱스 출력(1일)
card.iloc[0,:].idxmax() # pd.idxmax(), 최댓값 메서드 (apply 기능을 갖는다.)
card.idxmax(axis = 1)

###
df1.loc['23일',:].sort_values(ascending = False)[:1]

f4 = lambda x,y=1 : x.sort_values(ascending = False)[:y]

df1.apply(f4,y=1,axis = 1)
df1.sort_values(ascending = False)[:-1]

# 4) 각 일별 지출비용이 가장 높은 두 개 품목 출력
card.apply(top, axis = 1, n= 2)

###
df1.apply(f4,y=2,axis = 1)


# =============================================================================
# # 2. 'disease.txt' 파일을 읽고 
# =============================================================================
dis = pd.read_table('disease.txt', engine = 'python', sep = '\s+')
###
df2 = pd.read_table('disease.txt', engine = 'python', sep = '\s+')
df2 = pd.read_table('disease.txt', engine = 'python', sep = '\s+',header = 0, index_col = '월별')
# 1) 월별 컬럼 인덱스 설정
dis = dis.set_index('월별')
###
df2 = df2.set_index(['월별'])

# 2) index와 column 이름을 각각 월, 질병으로 저장
dis.index.name = '월'
dis.columns.name = '질병'
###
df2.index.names = ['월별']
df2.columns.names = ['질병']

# 3) NA를 0으로 수정(치환! 시험문제!!)
a1 = NA

str(a1.replace(NA,'0'))  # 문자열 replace 메서드는 NA를 치환 불가 / NA로 치환 불가

dis.replace(NA,0)   # 값 일치(문자값), NA 치환 가능 (pd.replace), 2차원 적용 가능
dis.replace(6,NA)   # 값 일치(문자값), NA로 치환 가능 (pd.replace), 2차원 적용 가능

dis.fillna(0)       # 2차원 데이터셋에서 사용 가능, NA 치환 가능

np.where(dis==NA,0, dis)                                # 2 차원 데이터 셋 치환 가능 (출력이 array)
np.where(dis.loc[:,'콜레라']==NA,0, dis.loc[:,'콜레라']) # 1차원 데이터 셋 치환 가능

dis.iloc[:,:] = np.where(dis==NA,0,dis)

###
f5 = lambda x : int(0) if pd.isnull(x) ==True else int(x)
df2 = df2.applymap(f5)

# 4) 천단위 구분기호 제거


# 5) 대장균이 가장 많이 발병한 달을 출력
dis.loc[:,'대장균'].sort_values(ascending=False)[:1]

df2.loc[:,'대장균'].sort_values(ascending=False)[:1]

# 6) 각 질병 별 발병횟수의 총 합을 출력
df2.apply(sum,axis=0)

# =============================================================================
# # 3. student.csv 데이터를 불러들여
# =============================================================================
df3 = pd.read_csv('student.csv', engine = 'python', sep =',')
# 1) 지역번호 컬럼 생성

pd.unique((list(map(lambda x : x.split(')')[0],df3.loc[:,'TEL']))))

loc = {'055':'외곽1', '051':'외곽2', '053':'외곽3','02':'서울','031':'인천'}

f2 = lambda x : loc.get(str(x.split(')')[0]))
df3['LOC']= df3.loc[:,'TEL'].apply(f2)


# 2) id에 'a'가 포함된 학생의 정보 출력

f3 = lambda x : 'a' in x

df3[:3]

  df3[:,df3.apply(f3,df3.loc[:,'ID'])]

df3.loc[:,'ID'].map(f3)





