run profile1
# stack / unstack 
 - stack : 컬럼의 인덱스화
 - unstack : 인덱스의 컬럼화
 - long <-> wide 형태의 변환
 - mulit-index의 컬럼화, 컬럼의 mumti-index 화
 
s1 = Series([1,2,3,4], index = [['A','A','B','B'],['a','b','a','b']])
s1

s1.unstack()           # 하위 index의 컬럼화 / 가장 하위의 레벨이 선택(기본값)
s1.unstack(level = 0)  # 선택 level에 따라 컬럼화 가능 


s2 = s1.unstack(level = 0)
s2.stack()            # 컬럼의 인덱스화
s2.stack(level = 0)   # 특정 columns의 index화

s2.loc['b','B'] = NA
s2.stack()                # stack처리 시 NA 생략(기본값 / dropna = True)
s2.stack(dropna = False)  # stack처리 시 NA 남김

#[연습문제]
# sales2.csv 파일을 읽고 형태 만들기
sales = pd.read_csv('sales2.csv', encoding = 'cp949')
# 1) 다음과 같은 형태로 만들어라
#                 냉장고          tv             세탁기         에어컨
#                 출고 판매 반품  출고 판매 반품  출고 판매 반품  출고 판매 반품
# 2018-01-01  c1  

sales = sales.set_index(['날짜','지점','품목'])
sales.unstack().sort_index(axis= 1, level =[1,0]).swaplevel(0,1,axis =1)

sales2 = sales.stack().unstack(level = [2,3])

# 2) 위의 데이터 프레임에서 아래와 같은 현황표로 출력(총합)
# 출고  ---
# 판매  ---
# 반품  ---

sales2.sum(axis = 1, level = 1).sum()

# 3) 날짜별 품목별 출고량의 총합을 아래와 같이 출력
#                     냉장고   TV    세탁기      에어컨
# 2018-01-01
sales2.sum(axis = 0, level = 0).sum(axis = 1, level = 0)


# 4) 지점별 각 판매 현황을(총 합) 아래와 같이 출력
#         출고  판매   반품  
# c1
# c2
# c3
sales2.sum(axis =0 , level = 1).sum(axis = 1, level =1)


# =============================================================================
# [참고] multi-index에서 산술연산 시 동시에 여러 level 전달 가능
sales.sum(level = [0,1], axis = 0)
# =============================================================================

# [연습문제]
#movie_ex1.csv 파일을 읽고
movie = pd.read_csv('movie_ex1.csv', engine = 'python')
#1)지역 - 시도별, 성별 이용비율의 평균을 정리한 교차테이블 생성
movie2 = movie.set_index(['지역-시도','성별'])['이용_비율(%)']

movie2.mean(level = [0,1]).unstack()
.
#2)일/연령대 별 이용비율의 평균을 정리한 교차테이블 생성
movie3 = movie.set_index(['일','연령대'])['이용_비율(%)']
movie3.mean(level = [0,1]).unstack()

# python - oracle 연동
#1. module 호출
1. pip install cx_Oracle (os에서 설치)
cx_Oralce : 오라클과 통신을 가능케하는 파이썬 패키지
# c:\user\KITCOOP\ > pip install cx_Oralce

#2. module 호출
import cx_Oracle 

#3. connection 생성
con1 = cx_Oracle.connect('scott/oracle@localhost:1521/testDB')


#4. sql 실행
pd.read_sql('select * from emp',con = con1 )


#[참고 - oralce sid 및 서비스 포트 확인 방법]
# C:\user\KITCOOP\lsnrctl status

#[참고 - oracle 연동시 한글 깨짐 현상]
import os
os.putenv('NLS_LANG','KOREAN_KOREA.KO16MSWIN949') # connection 생성 전 실행

#[연습문제 : 다음의 함수 생성]
f_sql('select * from emp', ip = '192.168.0.86', port = '', id= 'scott',passwd='oralce')









