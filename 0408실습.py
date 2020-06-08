# =============================================================================
# #1. 구구단 출력
# =============================================================================
for i in range(1,10):
    for j in range(2,10):
        print('%d X %d = %2d' % (j, i,j*i), end = ' ')
    print()
mul = [' %d x %d = %2d' % (j,i,j*i) for i in range (1,10) for j in range(2,10)]     
mul1
print('asc\tdsd')
for i in range(2,10):
    for j in range(1,10):
        print(f'%d * %d = %2d'%(i,j,i*j))
    print()
    
print(f'hi {i}')
mul2= [f'{i} * {j} = {i*j}' % (i,j,i*j) for i in range(2,9) for j in range(1,9)]
print(mul2)

# =============================================================================
# 2. 별 출력
# =============================================================================
s1 = '\u2605'

v1 = '  ' 
v2 = '\u2605'

print(v1 * (5-i) + v2 * (2i-1))    i
print(v1 * 4 + v2)                 1
print(v1 * 3 + v2 * 3)             2
print(v1 * 2 + v2 * 5)             3
...
print(v1*0 + v2*9)                 5    v1(5-i) + v2(2*i-1)
print(v1+1 + v2*7)                 6    v1(i-5) + v1((10-i)*2-1)
print(v1*2 + v2*5)                 7
print(v1*3 + v2*3 )                8

 # while문
i=1
while i<=10:
    if i <=5:
        print(v1*(5-i) + v2*(2*i-1))
    else : 
        print(v1*(i-5) + v2*((10-i)*2-1))
    i += 1



for star in range(1, 5):
     print(' ' * (5 - star) + '*' * (2 * star - 1))   
     if 3 == star:
         for star in range(3, 0, -1):
             print(' ' * (3 - star) + '*' * (2 * star - 1))
 

  
 line = int(input('number : '))
for star in range(1, line+1):
     print(' ' * (line - star) + '*' * (2 * star - 1))   
     if line == star:
         for star in range(line-1, 0, -1):
             print(' ' * (line - star) + '*' * (2 * star - 1))
 

# =============================================================================
# 3. 사용자로부터 하나의 단어를 입력받고 회문여부 판별
# lloll
# =============================================================================
v3=['lloll']
v4=['llooll']

v3[0]==v3[-1]
v3[1]==v3[-2]

v4[0] == v4[-1]
v4[1] == v4[-2]
v4[2] == v4[-3]

import math
vword = input('회문 판별할 문자 : ')
vcnt = math.trunc(len(vword) / 2)

for i in range(0,vcnt) :
    if vword[i] == vword[-(1+i)]:
        continue
    else:
        print('회문이 아니다.')
        exit(0)     # 프로그램 종료
    
print('회문입니다')  # 모든 for문 수행한 경우



word = input('input word : ')
check = True

for i in range(len(word)//2):
    if word[i] != word[-1 - i]:
        check = False
        break
        
print(check)
