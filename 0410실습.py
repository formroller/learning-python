# =============================================================================
#  오라클 만료 대처
# 1. orange 다른버전 설치(DBA,일반 버전)
# 2. 기타 툴 사용
#  - toad(평가판 무료)
#  - sql - devlolper(무료)
#  
# # cmd sqlplus scott/oracle >> ed - '\'로 수행
# =============================================================================



# =============================================================================
# # 1.  translate 함수 생성
# f_translate('abcdea','abc','ABC') ->'ABCdeA'
# =============================================================================


def f_translate(data, old, new):
    for i in range(0,len(old)):
        data = data.replace(old[i], new[i])
    return data
    
f_translate('abcdea','abc','ABC')


def f_translate(data, old, new):
    for i in range(0,len(old)):
        if i +1 > len(new):
            data = data.replace(old[i], '')
        else:
            data = data.replace(old[i], new[i])
    return data
f_translate('abcdea','abcd','ABC')
f_translate('abcdea','ab','ABC')



# =============================================================================
# # 2. oracle instr과 같은 함수 생성 (없으면 -1 생성)
# f_instr(data,pattern, start = 0, n =1)
# 
# =============================================================================
'abcde'.find('a')
'abcade'.find('a',1)
'abcadea'.find('a',1)

찾을문자열 시작위치 발견횟수 위치
a           1         1       0
a           0+1       2       3
a           1+1       3       6


def f_instr(data, pattern, start = 0, n = 1):
    if data.count(pattern) < n :
        position = -1
    else : 
        for i in range(0,n):
            position = data.find(pattern,start)
            start = position +  1
    return position

f_instr('abababc','a',start = 0,n =3)

'abababc'.count('a')

# =============================================================================
# # 3. 1-100까지 누적합 계산시 최초로 누적합이 1000 넘는 숫자 출력
# =============================================================================

vsum = 0 #더하기에 영향 없애기 위해 초기값 0으로 설정

for i in range(1,101):
    vsum += i
    if vsum >= 1000:
        break

vsum


