run profile1
# 1. employment.csv 파일을 읽고
df1 = pd.read_csv('employment.csv', encoding = 'cp949')

df1 = df1.set_index('고용형태')
#df1 = pd.read_csv('employment.csv', engine = 'python',na_values ='-', index_col = '고용형태')

# =============================================================================
# # 1) 년도와 각 항목(총근로일수, 총근로시간...)을 멀티 컬럼으로 설정
# =============================================================================
col1 = df1.columns.map(lambda x : x[:4])
col2 = df1.iloc[0,:].map(lambda x : x.split(' ')[0])
df1
df1.columns = [col1,col2]
df1 = df1.drop('고용형태', axis = 0)

df1.index.names
df1.columns.names = ['년도','고용형태']

df1.dtypes

df1 = df1.replace('-',0)
df1 = df1.applymap(lambda x : str(x).replace(',',''))
df1 = df1.astype('float')

#df1.columns = [df1.columns.map(lambda x: x[:4]),df1.iloc[0,:]]
#df1 = df1.iloc[1:,:]
#df1= df1.replace(NA,0)
#
#df1.columns.names = ['년도','근로사항']
#df1[-1:].apply(f2,axis = 1)
#f2= lambda x : int(x.replace(',',''))
#
#df1[:].replace(',','').astype('float')
#df1['b'].map(lambda x : x.replace('d','D')


# 2) 정규근로자의 월급여액을 년도별로 출력
df1.xs('월급여액', axis = 1, level = 1).loc['정규근로자',:]

df1.iloc[1,:]
a1 = df1.xs('월급여액 (천원)', axis = 1, level = 1).loc['정규근로자',:]

# 3) 각 년도별 근로자의 총근로일수의 평균 출력
df1.xs('총근로일수', axis = 1, level = 1).mean(0)

df1.xs('총근로일수', axis = 1, level = 1)

# 4) 각 년도별 정규근로자와 비정규근로자의 월급여액의 차이 계산
v1= df1.xs('월급여액', axis = 1, level =1).loc['정규근로자',:]
v2= df1.xs('월급여액', axis = 1, level =1).loc['비정규근로자',:]

v2-v1


a1 = df1.xs('월급여액 (천원)', axis = 1, level = 1).loc['정규근로자',:]
a2 = df1.xs('월급여액 (천원)', axis = 1, level = 1).loc['비정규근로자',:]
df1

# 2. 병원현황.csv 파일을 읽고 
df2 = pd.read_csv('병원현황.csv',encoding = 'cp949', skiprows = 1)

df2 = df2.drop(['항목','단위'], axis = 1)
df2 = df2.loc[df2['표시과목'] != '계',:]
# 1) 다음과 같은 데이터프레임으로 만들어라
#                   2013               
#                 1 2 3 4
# 신경과 강남구
#       강동구
#        ....

df2 = df2.set_index(['시군구명칭','표시과목'])

col1 = df2.columns.map(lambda x : x[:4])
col2 = df2.columns.map(lambda x : x[6])

df2.columns = [col1,col2]

df2 = df2.sort_index(axis = 1, level = [0,1],ascending = [False, True])

# 2) 성형외과의 각 구별 총 합을 출력
df2.xs('성형외과',axis = 0, level = 1).sum(1)

# 3) 강남구의 각 표시과목별 총 합 출력
df2.loc['강남구',:].sum(1)

# 4) 년도별 총 병원수의 합 출력
df2.sum(axis= 1, level = 0).sum(0)
