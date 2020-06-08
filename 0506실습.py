run profile1
# =============================================================================
# # 1. kimchi_test.csv 파일을 읽고
# =============================================================================
df1 = pd.read_csv('kimchi_test.csv', engine = 'python')

kim = pd.read_csv('kimchi_test.csv', engine = 'python')

# 1) 각 년도별 제품별 판매량과 판매금액의 평균
kim.groupby(['판매년도','제품'])[['수량','판매금액']].mean()

# 2) 년도별 제품의 판매처와 판매량, 판매금액 평균

kim.groupby(['판매년도','제품','판매처'])['수량','판매금액'].mean()

# 3) 각 김치별로 가장 많이 팔리는 월과 해당 월의 판매량을 김치이름과 함께 출력
#3-1) 김치의 월별 판매량 정보 시리즈 출력
df11= df1.groupby(['제품','판매월'])['수량'].sum()
df11= df1.groupby(['제품','판매월'])['수량'].sum()
v_idx = df12.groupby(level = 0).idxmax()
df12.loc[v_idx]   # 출력, v_idx가 Series이므로 values값이 색인 값으로 전달.

#3-2) 김치의 월별 판매량 정보 데이터프레임 출력
df12= df1.groupby(['제품','판매월'])[['수량']].sum()
v_idx = df11.groupby(level = 0).idxmax()
df11.loc[v_idx] # 에러, v_idx가 데이터프레임으로 key값이 색인값으로 전달

#=>시리즈는 컬럼 키가 없어 values만 전달되나
#  데이터 프레임은 키가 있으므로 key-values 형식으로 전달돼 에러 발생

#3-3) 김치 판매량이 큰 순서로 정렬, 1개 추출
df11.sort_values(ascending = False) # Series, values만 존재하므로 by값 불필요. 
df12.sort_values(ascending = False) # dataframe, by값 요구

df11.sort_values(ascending = False)[0:1]
f1 = lambda x : x.sort_values(ascending = False)[0:1]

df11.groupby(level = 0).apply(f1)                      # 그룹키 중복된 상태로 출력
df11.groupby(level = 0, group_keys = False).apply(f1)  # 중복된 그룹키 제거

kim.groupby('제품')['수량','판매월'].agg({'수량':'sum', '판매월':'max'})




# =============================================================================
# # 2. taxi_call.csv 데이터를 사용하여
# =============================================================================
df2 = pd.read_csv('taxi_call.csv', engine = 'python')

taxi = pd.read_csv('taxi_call.csv', engine = 'python')
# 1) 구별 택시콜이 많은 시간대를 출력
df21= df2.groupby(['발신지_시군구','시간대'])['통화건수'].sum()
v_idx2 = df21.groupby(level = 0).idxmax()
df21.loc[v_idx2]

taxi.groupby('발신지_시군구')['시간대','통화건수'].max()

# 2) 다음의 시간대별 시군구 통화건수의 총 합 출력 
#20 - 03시(야간),03-08시(심야), 08-15시(오전), 15-20시(오후)
v_bins = [10,3,8,15,20] 
pd.cut(df2['시간대'], bins = v_bins)  # 컷팅 객체 불연속이므로 에러 (bins must increase monotonically.)

v_bins= [0,3,8,15,20,24] # right = True => [0,3],(3,8], (8,15],(15,20],(20,24]
c1 = pd.cut(df2['시간대'], bins = v_bins, include_lowest = True, 
       labels = ['야간','심야','오전','오후','야간1']) # '야간' 중복 , 그룹 정보는 중복될 수 없다.

c1 = c1.str.replace('[0-9]','')

df2.groupby(c1)['통화건수'].sum()


#######################################
taxi.groupby('시간대')['통화건수'].sum()
taxi.groupby(['시간대','발신지_시군구'])['통화건수'].sum()



# =============================================================================
# # 3. 교습현황.csv 파일을 읽고
# =============================================================================
df3 = pd.read_csv('교습현황.csv',engine = 'python', skiprows = 1)

df3 = df3.set_index(['교습소명','교습과정'])
df3 = df3.iloc[:,3:]

df3 = df3.applymap(lambda x : int(x.replace(',','')))


piano = pd.read_csv('교습현황.csv',engine = 'python', skiprows = 1)

# 1) 교습과정별 분기별 교습 금액의 총 합 출력
m1 = df3.columns.str.split('(').str.get(1).str.replace(')','').astype('int')  # 월 추출 , str.get() 색인에 대한 벡터처리
c1 = pd.cut(m1, bins = [1,3,6,9,12], include_lowest = True, labels = ['1분기','2분기','3분기','4분기']) # 분기 labeling

df3.groupby(c1, axis = 1).sum().groupby(level = 1).sum()
df3.columns.str[:4]



piano['교습소명']=piano['교습소명'].map(lambda x : x.replace('교습소',''))
col1 = piano.columns.map(lambda x : x[:5].replace('(',''))
col2 = piano.columns.map(lambda x : x[5:].replace(')',''))


piano.columns = [col1,col2]
piano = piano.drop(['교습소주소','분야구분','교습계열'], axis = 1)

piano = piano.set_index(['교습소명','교습과정'])
piano2 = piano.stack()

piano2.index


piano3 = piano2.reset_index()

pd.cut(piano3['level_2'],bins = [0,3,6,9,13], include_lowest = True, labels = ['1분기'])
pd.cut(sub3['시간'], bins = [0,12,24], include_lowest = True, labels = ['오전','오후'])

paino3.columns = ['교습소명', '교습과정', '월', '교습금액']




piano.xs('월', axis = 1, level = 1)
pd.cut(piano, bins = [1,5,10], include_lowest = True,labels = ['A','B'])



