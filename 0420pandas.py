## pandas
# - DataFrame 생성 및 전처리에 필요한 기본 함수 내장된 모듈
# - 주로 NA에 대한 연산이 빠르고 쉽게 되어있음
# - 산술연산에 대해 벡터 연산 가능
# - 문자열 처리 벡터연산 불가 => mapping처리 (map,apply,applymap)
 
 # Series 
# - DataFrame을 구성하는 기본 구조
# - 1차원, 하나의 데이터 타입만 허용
# - Key - vlaue 형식의 자료구조, key는 index를 의미(행번호)
# - 주로 DataFrame의 컬럼을 표현
run profile1 
# 1. 생성
s1 = Series([1,2,3,4])
s2 = Series([1,2,3,4,'5'])
s2 # 'object' => str일 경우 object 출력

s3 = Series([1,2,3,4], index = ['a','b','c','d'])
s4 = Series([10,20,30,40], index = ['a','b','c','d'])
s5 = Series([10,20,30,40], index = ['A','b','c','d'])

# 2. 연산
s1 + 1     # Series와 scalar 연산 가능
s1 + s1    # 서로 같은 index 갖는 Series 연산 가능
s3 + s5    # 서로 다른 index 갖는 경우 full outer join식 연산처리


# 3. 색인
s1[0]
s1[0:3]
s1[[0,3]]
s1[s1>2]

# 4. 기타매서드
s1.dtype    # Series 구성 데이터 타입
s2.dtypes   # 복수형 가능

s1.index    # Series의 key값 (index)
s2.vlaue    # Series의 value

# 5. reindex
s1 = Series([1,2,3,4],index = ['a','b','c','d'])
# key값 없는 경우 index 부여

s2 = Series(s1, index = ['A','B','C','D'])  # reindex
s1[['A','B','C','D']]
# key값 있는 경우 해당 인덱스 값에 맞게 재배치 


#[예제]
#다음의 리스트를 금,화,수,월,목,일,토 인덱스 값을 갖도록 시리즈 생성 후 월~일 순서로 재배치
L1 = [4,3,1,10,9,5,1]
s1 = Series(L1, index = ['금','화','수','월','목','일','토'])
Series(L1, index = ['월','화','수','목','금','토','일']) # label indexing key값 / positional indexing, 위치값
s1.index

# 6. index 수정
s1.index = ['월','화','수','목','금','토','일'] # 데이터 순서 유지하며 인덱스 값만 변경

s1.index         # index object type
s1.index.values  # index => array 객체로 변경
s1.index[0] = 'a'        # 인덱스 일부 수정 -> index object에 대한 수정 금지
s1.index.values[0] = 'a' # 수정 가능

#[연습문제: 다음 시리즈의 첫번째 인덱스 값을 10으로 수정]
s1 = Series([1,2,3,4])
s1.index  # Rangeindex, 범위로 설정된 인덱스

s1.index[0] = 10          # 에러, index object 직접 수정 불가
s1.index.values[0] = 10   # 에러X, 원본에 직접 반영 불가
                          # 자동으로 생성된 rarangeindex의 경우 원본 수정 안됨

a1 = s1.index.values     # index값을 갖는 새로운 객체 생성 후
a1[0] = 10               # 수정
s1.index = a1            # index에 다시 덮어쓰는 방식


s1 = Series([1,2,3,4],index = [0,1,2,3])
s1.index # int
#=> 자동으로 부여된 인덱스는 수정해도 원본이 변경되지 않는다. (전체수정 필요)

# 1) 인덱스별 수정
s1.index = [10,2,3,4]  

# 2) 분리 copy, 수정 후 덮어쓰기
a1 = s1.index.values
a1[0] = 10
s1.index = a1
# => 인덱스 일부 수정은 불가, 덮어쓰기는 가능 





-