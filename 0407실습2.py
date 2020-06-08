# 다음의 문제를 lambda + map문을 사용하여 출력
# 1) ename = ['smith','allen','king'] 에서 s로 시작하는 여부 출력
ename = ['smith','allen','king']

f1 = lambda x : x.startswith('s')
list(map(f1,ename))
ename[list(map(f1,ename))]         # 조건 출력 불가
Series(ename)[list(map(f1,ename))] # 조건 출력 가능, ename을 Seires로 변경해 벡터 연산

f1= lambda x : x[0] == 's'
list(map(f1,ename))

# 2) jumin = ['8812111223928','8905042323343','90050612343432'] 에서 
#    성별 숫자 출력
jumin = ['8812111223928','8905042323343','90050612343432']
'8812111223928'[6]  # 문자열 추출 가능
jumin[6]            # 각 리스트 원소의 추출로 해석, 추출 불가

f2 = lambda x : x[6]
list(map(f2,jumin))    

# 3) ename에서 smith 또는 allen 인지 여부 출력 [True,True,False]

ename == 'smith'
('smith' == 'smith') or ('allen' == 'allen')
'smith' in ['smith','allen']

f3 = lambda x :  x in ['smith','allen']

list(map(f3, ename))                 # 조건 색인 불가
Series(ename)[list(map(f3, ename))]  # 조건 색인 가능

f3 = lambda x : 'allen' in x or 'smith' in x
list(map(f3, ename))

# 4) tel=['02)345-4958','031)334-0948','055)394-9050','063)473-3853'] 에서
#    다음과 같이 국번 XXX 치환 (02)345-4958 => 02)XXX-4958)
tel=['02)345-4958','031)334-0948','055)394-9050','063)473-3853']

'02)345-4958'.replace('02)345-4958'.split(')')[1].split('-')[0],'xxx')

f4 = lambda x : x.replace(x.split(')')[1].split('-')[0],'xxx')
list(map(f4,tel))

f4 = lambda x : x[-8:-5].replace('^d','x')
f4 = lambda x : x.split(')')[0] +')xxx-'+x.split('-')[1]
list(map(f4,tel))


# 5) vid=['2007(1)','2007(2)','2007(3)','2007(4)']에서 
# 각각 년도와 분기를 따로 저장

# 2007(1)  2007  1
# 2007(2)  2007  2
#
vid=['2007(1)','2007(2)','2007(3)','2007(4)']

f5 = lambda x : x[:4]
f6 = lambda x : x[5]
vyear = list(map(f5,vid)) # 년도
vqt = list(map(f6,vid)) # 분기

f5 = lambda x : x.split('(')[0]
f6 = lambda y : y.split('(')[1].replace(')','') 
year= list(map(f5,vid))
qty = list(map(f6,vid))
f7 = lambda x ,y : x  +' ' +  y
list(map(f7,year, qty))
# 기존  => 년도 분기