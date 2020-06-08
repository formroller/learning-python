run profile1
# =============================================================================
#  정규식 패턴
# =============================================================================
# - 약속된 기호를 사용한 패턴 확인 및 추출
# - 문자열 함수, 메서드에도 사용 가능(일부)
# - re 모듈 호출 필요
# - findall 메서드로 정규식 패턴과 일치하는 패턴 추출 가능
# - 자주 쓰는 정규식 패턴은 compile로, 변수화 가능
 
# [예제 - 다음 문자열에서 이메일 주소를 정규 표현식 패턴으로 추출]
v_email = 'abc 12 | abc@naver.com aaa ... 11 Abbb@hanmail.net'

import re
pat1 = re.compile('[a-z]+@[a-z]+.',flags=re.IGNORECASE)
pat2 = re.compile('[a-z]+@[a-z]+.[a-z]+',flags=re.IGNORECASE)

# findall
# 패턴.findall(문자열)
pat1.findall(v_email)
pat2.findall(v_email)

# 연습문제) 다음의 메소드에서 '문자열+숫자' 패턴 추출
txt2 = '''a a1. _12
abc+123 ax1 df Ax+000'''

pat3 = re.compile('[a-z]+\+[0-9]+',flags = re.IGNORECASE)
pat3.findall(txt2)                         

# 정규식 패턴 그룹핑 기능 
# [예제 - 다음 문자열에서 id, 검색엔진을 각각 정규 표현식 패턴으로 추출]
v_email = 'abc 12 | abc@naver.com aaa ... 11 Abbb12@hanmail.net'

# () 그룹핑, 추출할 패턴 지정=> 패턴 내부의 특정 패턴 추출시 사용
pat4 = re.compile('([a-z0-9]+)@([a-z]+)\.[a-z]{2,4}',flags=re.IGNORECASE)
pat4.findall(v_email)

v_email1 = 'abc 12 | abc@naver.com aaa ... 11 Abbb12-1@hanmail.net'
pat5 = re.compile('([a-z0-9-]+)@([a-z]+)\.[a-z]{2,4}',flags=re.IGNORECASE) 
#=> 대괄호 안에 특수기호는 일반 기호로 추출
Series(pat5.findall(v_email1)).str[0]
Series(pat5.findall(v_email1)).str[1]


#[연습문제]
# shoppingmall.txt에서 쇼핑몰 웹 주소만 출력(총25개)
# 힌트 : 각 행을 문자열로 불러온 후 하나의 문자열로 결합 후 진행

c1 = open('shoppingmall.txt')
list1 = c1.readlines()
c1.close()

# 리스트로 불러온 각 행 데이터-> 하나의 문자열로 결합
# 1) for문
vstr = ''
for i in list1:
    vstr += i
       
vstr

# 2) 결합메서드 (cat/join)
vstr = Series(list1).str.cat()

# 패턴 추출
# http://www.gaenso.com 

pat1 = re.compile('http://[a-z]+\.[a-z]+\.[a-z.]+',flags = re.IGNORECASE)
pat2 = re.compile('http://[a-z0-9./-]+',flags = re.IGNORECASE)
pat3 = re.compile('http:.+',flags = re.IGNORECASE) # 공백도 같이 표현된다는 단점이 있다.
pat1.findall(vstr) 
pat2.findall(vstr) 
pat3.findall(vstr) 


#[참고 : 정규식 패턴 . 사용시 주의사항]
vstr2 = 'http://www.wemakeprice.com nnnn\n\n광고집행기간 '
pat3.findall(vstr2)  # ['http://www.wemakeprice.com nnnn'] .은  \n제외한 모든 기호,문자등을 출력한다.(주의)

#한글 추출 : [가-힣]


# str.findall() : 패턴추출 메서드
# - Series만 적용 가능
# - 벡터연산 내장
# - Series(대상).str.findall(패턴)

s1 = Series(['abc abcd123@andkk.ole df ','dfw dkfj@dfjkls.con xxx'])
pat1 = re.compile('.+@.+')
pat2 = re.compile('[a-z0-9]+@[a-z.]+')

s1.str.findall(pat1) # .+ 은 공백을 포함하므로 모든 문자 출력된다.
s1.str.findall(pat2) # 공백 이전까지 출력(리스트 형태)

s1.str.findall(pat2).str[0] # 리스트 없이 출력

#[연습문제 : 위 예제에서 이메일 아이디, 엔진 각각 추출 데이터 프레임 생성] 
s1
pat3 = re.compile('([a-z0-9]+)@([a-z.]+)')

id1 = s1.str.findall(pat3).str.get(0).str[0]
engine1 = s1.str.findall(pat3).str[0].str[1]

DataFrame({'id':id1, 'addr':engine1 })

#[연습문제]
#project_songpa_data.csv 파일을 읽고 동별 LAT와 LON의 평균
df1 = pd.read_csv('project_songpa_data.csv', engine = 'python')

df1.name = df1.name.str.findall('[가-힣]').str.join('')  # 원소별로 합친다 join
df1.name.unique()

df1.name = df1.name.str.findall('[가-힣]+[동역]').str[0]
df1.name.unique()

df1.groupby('name')[['LAT','LON']].mean()

############
pro = pd.read_csv('project_songpa_data.csv', engine = 'python')
pro = pro.iloc[:,1:]
patt1 = re.compile('[가-힣]+')
pro['name']= pro['name'].str.findall(patt1).str[0]

pro.groupby('name')[['LAT','LON']].mean()

# =============================================================================
# # np.random.randint
# =============================================================================
# - sampling 함수
# - data에서의 sampling은 불가, sampling number 추출
 
np.random.randint(low,    # 시작값
                  high,   # 끝 값  
                  size)   # 추출 사이즈

#[참고 : sampling in R]
sample(c('a','b','v','r'), size =1) # 문자벡터에서 추출 가능
sample(1:150, size = 1)             # 1-150 숫자벡터에서 추출

#예제) cancer.csv 파일에서 train, test data set을 7:3 비율로 랜덤추출
cancer = pd.read_csv('cancer.csv')

# 행과 열의 크기
rownum = cancer.shape[0] # 569행
colnum = cancer.shape[1] # 32열

# sample number 획득
rn = np.random.randint(0, rownum, size=round(0.7*rownum)) # size는 float type 불가. round로 반올림

# train, test data set 분리
cancer_train = cancer.iloc[rn]
cancer_test = cancer.drop(rn)

# =============================================================================
# # dummy variable (더미변수)
# =============================================================================
# - factor형 변수를 0과 1을 사용해 구분하는 방법
# - 주로 class의 갯수 또는 하나 작은 변수로 분할하는 방법 선택
# - pd.get_dummies
# - 딥러닝은 학습시 문자형 받지 않기 때문에 dummy 형태로 변경해야한다

#case1) 1,0으로 factor형 만든 변수
x_y1 = ['Y','N','Y','Y']
pd.get_dummies(x_y1)

    Y
Y   1
N   0
Y   1
Y   0

    Y_y    Y_n
Y    1      0
N    0      1
Y    1      0
Y    1      0

#case2)
x_y2 = ['A','B','C','A']
pd.get_dummies(x_y2,prefix = 'Y')

    Y_A    Y_B    Y_C
A    1      0      0 
B    0      1      0 
C    0      0      1 
A    1      0      0 

    Y_A    Y_B    
A    1      0      
B    0      1      
C    0      0     

A    1      0     


#예제) cancer 데이터의 Y값 더미변수
df_dumm= pd.get_dummies(cancer.diagnosis, prefix = 'Y')

cancer.join(df_dumm)








