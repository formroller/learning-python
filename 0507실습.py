run profile1
# =============================================================================
# # 1. ncs학원검색.txt 파일을 읽고 다음과 같은 데이터 프레임 형식으로 출력
# =============================================================================
# name        addr        tel         start         end    
# 아이티윌  서울 강남구 02-6255-8001  2018-10-12  2019-03-27
#아이티윌   ( 서울 강남구 ☎ 02-6255-8002 ) 훈련기관정보보기  훈련

c1 = open('ncs학원검색.txt')
list1 = c1.readlines()
c1.close()

s1 = Series(list1).replace('\n',NA).dropna()
import re
pat1 = re.compile('(.+) \( (.+) ☎ ([0-9-]+) \) .+ : ([0-9-]+) ~ ([0-9-]+)')

df1 = s1.str.findall(pat1)

c1 = df1.str[0].dropna().str.get(0).str.strip()
c2 = df1.str[0].dropna().str.get(1).str.strip()
c3 = df1.str[0].dropna().str.get(2).str.strip()
c4 = df1.str[0].dropna().str.get(3).str.strip()
c5 = df1.str[0].dropna().str.get(4).str.strip()

df1 = DataFrame({'name':c1, 'addr':c2, 'tel':c3, 'start':c4, 'end':c5})

df1.loc[df1.addr.str.contain('강남'),:]
df1.loc[df1.name=='아이티윌',:]

#####
c1 = open('ncs학원검색.txt')
li1 = c1.readlines()
c1.close

vstr = Series(li1).str.cat()


#name
na2 = re.compile('([\S]+)[\( ]+[서울]+',flags = re.IGNORECASE)
name = na2.findall(vstr)

#addr
서울 종로구 ☎
addr2 = re.compile('([가-힣 ]+)[☎]+')
add = Series(addr2.findall(vstr))

#tel
tel1 = re.compile('02-[0-9-]+-[0-9]+')
tel = Series(tel1.findall(vstr))
#start
str1 = re.compile('훈련기간 : [0-9]+-[0-9]+-[0-9]+')
start = Series(str1.findall(vstr)).str.split('훈련기간 : ').str[1]

#end
end1 = re.compile('~ [\d]+-[\d]+-[\d]+')
end = Series(end1.findall(vstr)).str.split('~ ').str[1]



df1 = DataFrame({'name' : name,'addr' : add, 'tel':tel,'start':start,'end':end})
# =============================================================================
# # 2. oracle_alert_testdb.log 파일을 읽고 
# =============================================================================
c2 = open('oracle_alert_testdb.log')
list2 = c2.readlines()
c2.close()

s2 = Series(list2)
pat2 = re.compile('ORA-([0-9:]+) (.+)', flags = re.IGNORECASE)

s2 = s2.str.findall(pat2).str[0].dropna()
c1 = s2.str.get(0).str.strip().str.replace(':','')
c2 = s2.str.get(1).str.strip().str.replace(':','')

df2 = DataFrame({'code':c1,'error':c2})
##########
c1 = open('oracle_alert_testdb.log')
li2 = c1.readlines()
c1.close()
li3 = Series(li2).str.cat()

# 1) 아래처럼 데이터 프레임 작성(ORA-00000)
# code   error
# 00312  online log 1 thread 1

code1 = re.compile('ORA-([0-9]+):')
code = code1.findall(li3)

error1 = re.compile('ORA-[0-9]+: ([\w]+.+)')
error = error1.findall(li3)


error1 = re.compile('ORA-[\d]+: ([\D]+[\d]+[\D]+)')
error = error1.findall(li3)

df2 = DataFrame({'code':code,'error':error})
# 2) 각 코드별 발생횟수 확인
df2.groupby('code')['code'].count().sort_values(ascending = False)

df2.groupby('code').count()
df2.loc[df2.code=='00312',:]

# =============================================================================
# # 3. 교습현황.csv파일을 읽고
# =============================================================================
df3 = pd.read_csv('교습현황.csv', engine = 'python',skiprows = 1)
pat3 = re.compile('.+\(([가-힣]+)[,)]')
df3['동'] = df3['교습소주소'].str.findall(pat3).str[0]

df3.dtypes
df3 = df3.set_index(['동','교습과정'])
df3 = df3.iloc[:,4:]

df3 = df3.applymap(lambda x : int(x.replace(',','')))


#########
df3 = pd.read_csv('교습현황.csv', engine = 'python',skiprows = 1)
df3=df3.set_index(['교습소명','교습과정','교습소주소'])
df3 = df3.iloc[:,2:]

m1 = df3.columns.str.findall('[\d]+').str[1].astype('int')
c1 = pd.cut(m1, bins = [1,3,6,9,12], include_lowest = True, labels = ['1분기','2분기','3분기','4분기'])

df3.groupby(c1, axis = 1).sum().groupby(level = 1).sum()
df3['교습소주소']=df3['교습소주소'].str.findall('\(([가-힣]+동)').str[0]
# 1) 동별 분기별 총 보습금액 출력
pat4 = re.compile('[0-9]+\(([0-9]{1,2})\)')
v1 = df3.columns.str.findall(pat4).str[0].astype('int')

q1 = pd.cut(v1, bins = [1,3,6,9,12], include_lowest = True, labels = ['1Q','2Q','3Q','4Q'])

df3.groupby(level = 0).sum().groupby(q1,axis =1).sum()

# 3) 동별 보습액 총 액이 가장 높은 2개의 보습과정을 보습액과 함께 출력
df33 = df3.groupby(level = [0,1]).sum().sum(axis = 1)

f1 = lambda x : x.sort_values(ascending = False)[:2]
df33.groupby(level = 0, group_keys = False).apply(f1)



