#0427부터 시험범위 
run profile1

# =============================================================================
# 파이썬 시각화
# =============================================================================
## figure와 subplot
# - figure  : 그래프가 그려질 창 (도화지 개념)  ( = dev.new())
# - subplot : 창 내부에 실제 그래프 그릴 공간   (par(mfrow=c(,))
# - figure와 subplot에 이름 부여 가능

# =============================================================================
# #1. figure와 subplot 생성
# =============================================================================
import matplotlib.pyplot as plt

#1-1) figure / subplot 각각 생성
fig1 = plt.figure()     # figure 생성 / 이름 부여 시 수정 가능
ax1 = fig1.add_subplot(2,   # figure 분할하려는 행의 수
                       2,   # figure 분할하려는 컬럼 수
                       1)   # 분할된 subplot 위치


#1-2) figure / subplot 동시 생성
fig2,ax = plt.subplots(2,2)  # 2*2의 subplot 할당 (ax = 그룹명)

ax[0,0]  # subplot 색인으로 접근
ax[0,1]
ax[1,0]
ax[1,1]

# =============================================================================
# #2. 선그래프 그리기
# =============================================================================
s1 = Series([1,3,4,7,8,9])
ax1.plot(s1)   # 특정 subplot에 직접 전달해 호출

s1.plot()      # 마지막 호출된 subplot 혹은 새 창에 그림
#=> 열린 figure 없을 경우 figure 한 개 자동 생성
 
# 2-2) DataFrame
# - 컬럼별 서로 다른 선 그래프 출력
# - index는 x축 눈금으로 자동 설정
# - columns은 범례로 자동 전달
# - index name은 x축 이름으로 자동 전달
# - columns name은 범례 이름으로 자동 전달
  
df_price = DataFrame({2000:[1900,2400,2700],
                      2001:[1600,1800,2400]})

df_price.index = ['A','B','C']

df_price.index.name = 'product'  # x축 이름
df_price.columns.name = 'year'   # y축 범례 



.plot() 


#[참고 - 파이썬 프롬프트에서 그래프 팝업 호출 방법]
#cmd
C:\Users\kitcoop> ipython           # 아나콘다 일반모드
C:\Users\kitcoop> ipython --pylab   # pylab(시각화)  모드

In [1]: %matplotlib qt              # 아나콘다 실행 후 pylab모드 전환 방법

#[참고 - spyder에서 그래프 팝업 호출 방법]
#Tools > Preferences > Ipython Console > Graphics > Graphics backend에서
#Backend를 Automatic으로 변경, * spyder restart

#[연습문제]
#cctv.csv를 불러오고 각 년도/ 구역별 검거율 증가추이를 
# 비교할 수 있도록 plot도표 그리기
#[참고 : 그래프 출력 시 한글 깨짐 해결]
plt.rc('font', family = 'Malgun Gothic')

cctv = pd.read_csv('cctv.csv', engine = 'python')

cctv['검거율'] = (cctv['검거'] / cctv['발생']) * 100
cctv2 = cctv.pivot_table(index = '년도',columns = '구', values = '검거율')

cctv2.plot()


# =============================================================================
# #3. 그래프 옵션 전달
# =============================================================================
cctv2.plot(title = '구,년도별 범죄 검거율 현황',   # 그래프 제목
           xticks = cctv2.index,                  # x축 눈금
           ylim = [0,130],                        # y축 범위
           fontsize = 8,                          # 글자 크기
           rot = 30,                              # x축 눈금 회전각    
           style = 'k-')                          # 라인 스타일     

cctv2.plot(title = '구,년도별 범죄 검거율 현황', xticks = cctv2.index, ylim = [0,130],fontsize = 8,rot = 30)
cctv.plot?

#1) x축 이름, y축 이름 설정
plt.xlabel ('발생년도')
plt.ylabel = ('검거율')

plt.xlabel?
#2) 그래프 제목 설정
plt.title('구별 검거율 변화추이')

#3) x,y축 눈금 범위 변경
plt.xlim
plt.ylim([0,130])

#4) x,y축 눈금 변경
plt.xticks(cctv2.index)
plt.yticks

#5) 범례 (범례는 별도로 지정해야한다)
plt.legend(fontsize=6,
           loc = 'best',      # loc = best (default)
           title = '구 이름')


#[참고 : 라인스타일 전달 방식]
#1) style로 색, 라인형태 동시 전달 방식
# r(색상)o(선 모양) --
'r--'  : 붉은 점선
'k-'   : 검정 실선
'ko--' : 검정 점모양 대시선, in R 'o' dash
'k-'   : 검정 

#2) 색과 라인스타일 각각 전달 방식
s1.plot(color = 'red', linestyle = '--')


# =============================================================================
# 4. barplot 그리기
# =============================================================================
# - 컬럼별 서로 다른 그룹
# - 각 컬럼의 데이터들이 각기 다른 막대로 출력(default)
# - stacked = True 설정시 하나로 쌓인 그래프로 출력
# - 컬럼명이 범례로 자동 전달
# - 인덱스명이 x축 눈금으로 전달


df_fr = DataFrame({'apple':[100,110,200],
                  'banana':[150,170,210],
                  'oragne':[50,70,100]})

df_fr.plot(kind = 'bar')
plt.xticks(rotation = 0)  # x축 눈금 회전 전달

#[연습문제]
#kimchi_test.csv 파일을 읽고,
# 월 별 김치 판매량을 비교할 수 있도록 막대그래프로 표현

kim = pd.read_csv('kimchi_test.csv', engine = 'python')

kim2 = kim.pivot_table(index='제품', columns = '판매월', values = '수량', aggfunc = 'sum')

import matplotlib.pyplot as plt
plt.rc('font', family = 'MAlgun Gothic')
kim2.plot(kind = 'bar')

plt.xticks(rotation = 0)
plt.legend(title = '판매월', fontsize = 8)
plt.title('월별 김치 판매량')
plt.ylabel('판매량')

#######
df1 = pd.read_csv('kimchi_test.csv', engine = 'python')
df1.columns

df2 = df1.pivot_table(index = '판매월',columns = '제품', values = '수량', aggfunc = 'sum')
df3 = df1.pivot_table(index = ['판매년도','판매월'],columns = '제품', values = '수량')

df2.plot(kind = 'bar', title = '월 별 김치판매현황')  # 월별 판매현황
df3.plot(kind = 'bar')  # 년도 / 월 별 판매현황


plt.legend(fontsize=6,
           loc = 'best',      # loc = best (default)
           title = '제품')






















