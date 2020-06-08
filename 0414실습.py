# 1. f_write_txt(vname,           # 저장할 변수명(2차원 리스트)
#                fname,           # 저장할 파일명
#                sep=' ',         # 분리구분기호
#                fmt='%.2f')      # 변경포맷

L1 = [[1,2,3,4],[5,6,7,8]]


def f_write_txt(vname, fname, sep=' ' , fmt= '%.2f'):
    c1 = open(fname,'w')
    for i in vname:
        vstr=''
        for j in i:
            j = fmt % j
            vstr = vstr + j + sep
        vstr = vstr.rstrip(sep)    
        c1.writelines(vstr + '\n')
    c1.close()

f_write_txt(L1,'write_text4.txt')
f_write_txt(L1,'write_text4.txt',sep = '*',fmt='%02d')


'%.2f' % 1
'%.2f' % [1,2,3,4]  # list에 즉시 적용 불가

vstr = ''
for j in [1,2,3,4]:
    vstr += str(j)+';'
vstr.rstrip(';')

# vstr -> 1;2;3;4;
# vstr.rstrip(';')


#연습문제]
#disease.txt 파일을 읽고(컬럼명 생략) 맨 마지막 컬럼 데이터를 
#소수점 둘째 자리로 표시 후 새로운 파일에 저장
def f_read_txt(file, sep = ' ', fmt = int):
    c1 = open(file,'r')
    v1 = c1.readlines()
    c1.close
    
    outlines = []
    
    for i in v1:
         L1 = i.strip().split(sep)
         outlist.append([fmt(i) for i in L1])
    return outlist  


def f_read_txt(file,sep=' ', fmt=int) :
    c1 = open(file,'r')   # 커서 선언
    v1 = c1.readlines()               # fetch 
    c1.close()
    
    outlist = []
    
    for i in v1 :
        L1 = i.strip().split(sep)
        outlist.append([fmt(i) for i in L1])
    
    return outlist

L1 = f_read_txt('disease.txt',sep='\t', fmt =str)
L1

#step2) 컬럼 선택을 위한 array로 변경
arr1 = np.array(L1); arr1
arr1[:,-1]

#step3) NA 치환
arr1[:,-1].replace('NA',0) # replace는 array에 적용 불가

f1 = lambda x: x.replace('NA','0')
list(map(f1,arr1[:,-1]))

#step4) 형식 변경
f1 = lambda x: '%.2f'%int(x.replace('NA','0'))
arr1[:, -1] = list(map(f1,arr1[:,-1]))

#step5) 외부파일에 저장
f_write_txt(arr1, 'disease2.txt',sep=' ' ,fmt = '%s')



# 2.  5*4 형태의 배열을 생성한 후 
import numpy as np
arr1 = np.random.randn(5,4)

a1 = np.arange(1,21).reshape(5,4)
# 1) p(1,0), p(3,1) 의 값을 출력
arr1 [[1,3],[0,1]]
a1[[3,1],[1,0]]
a1[[1,0],[3,1]]

# 2) 위의 배열에서 arr[1:3,2:4]의 형태와 동일하게 리스트색인을 통해 출력
arr1[1:3,2:4]
arr1[np.ix_([1,2],[2,3])]
arr1[[1,2],:][:,[2,3]]

a1[1:3,2:4]

# 3. 2부터 시작하는 짝수로 구성된 5X5 배열을 만들고
# 참고 : np.arange(start,end,by)
arr2 = np.arange(2,51,2).reshape(5,5)

a2 = np.arange(2,51,2).reshape(5,5)

# 1) [[24,26],
#     [34,36]] 출력
arr2[2:4,1:3]
arr2[np.ix_([2,3],[1,2])]

a2[2:4,1:3]

# 2) [14, 28] 출력 => P(1,1), P(2,3)
arr2[[1,2],[1,3]] # 떨어진 점은 포인트 출력

a2[[1,2],[1,3]]


# 3) [2,6,10] 출력
arr2[0,[0,2,4]]

a2[0][[0,2,4]]


# 4) [[24,28,30],
#      44,48,50]] 출력
arr2[np.ix_([2,4],[1,3,4])]

a2[[2,4],1:5] # 출력 결과 다름

# 4. a2=np.arange(1,25).reshape(2,3,4)를 만들고
arr3=np.arange(1,25).reshape(2,3,4)

a3=np.arange(1,25).reshape(2,3,4)

# 1) [[7,8],
#     [11,12]] 출력
arr3[0,1:3,2:4]   # 차원축소 (2차원 출력)
arr3[0:1,1:3,2:4] # 차원축소 방지(3차원 출력)

arr3[0,[1,2],[2,3]]   # 포인트 추출 색인 방식
arr3[np.ix_(0,[1,2],[2,3])]   # Cross index must be 1 dimensional (에러)
arr3[np.ix_([0],[1,2],[2,3])] # 하나의 정수값도 리스트로 전달
# => np.ix_인자로는 리스트만 들어올 수 있다.
# => 인자로 콜론(:) 전달 불가

## 시험 출제!
arr3[0,:,:][[1,2],:][:,[2,3]]
arr3[0:1,:,:][:,[1,2],][:,:,[2,3]]


a3[0,[1,2],2:4]

# 2) [[[5,6],
#      [9,10]],
#     [[17,18],
#      [21,22]]] 출력

arr3[:,[1,2],[0,1]]                # 불가, 포인트 색인 방식
arr3[np.ix_(:,[1,2],[0,1])]        # 불가, np.ix_ 인자로 콜론(:) 전달 불가

arr3[np.ix_([0,1],[1,2],[0,1])]
arr3[:,1:3,0:2]
arr3[:,[1,2],:][:,:,[0,1]]

arr3[:,[1,2],:2]
a3[0:,[1,2],:2]
