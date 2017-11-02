'''
1．编写一个输入分数，输出分数等级的程序，具体为：
Score	Grade
90~100	A
70~89	B
60~69	C
0~59	D
others	Invalid score
'''
def score_grade(score):
    score = int(score)
    if score >= 90 and score <= 100:
        print('A')
    elif score >= 70:
        print('b')
    elif score >= 60:
        print('c')
    elif score >= 0:
        print('d')
    else:
        print('error')

score = input('input: ')
print(score_grade(score))

####################################################################################################
'''
2. 验证命题：如果一个三位整数是37的倍数，则这个整数循环左移后得到的另两个3位数也是37的倍数。（注意验证命题的结果输出方式，只要输出命题为真还是假即可，而非每一个三位数都有一个真假的输出）
'''
def multiple():
    flag = False
    for i in range(100, 201):
        str_num = str(i)
        if i%37 != 0:
            continue
        elif int(str_num[2]+str_num[0]+str_num[1])%37 == 0 and int(str_num[1]+str_num[2]+str_num[0])%37 == 0:
            flag = True
    return flag

print(multiple())

####################################################################################################
'''
3.验证哥德巴赫猜想之一：2000以内的正偶数（大于等于4）都能够分解为两个质数之和。每个偶数表达成形如：4=2+2的形式，输出时每行显示6个式子。
'''
def is_prime(num):
    for i in range(2, int(num/2)+1):
        if num%i == 0:
            return False
        else:
            return True

def test():
    result=[]
    for i in range(4, 100):
        if i%2 != 0:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if is_prime(j) == True and is_prime(i-j) == True:
                    result.append(str(i)+'='+str(j)+'+'+str(i-j))
                else:
                    continue
    return result
               
def print_format(result_list):
    for i in range(len(result_list)):
        print(result_list[i], end='; ')
        if (i+1)%6 == 0:
            print(end='\n')
        
        
print(print_format(test()))

####################################################################################################
'''
4. 编写一个程序，让用户输入苹果个数和单价，然后计算出价格总额。
'''
while True:
    try:
        count = int(input("Enter count: "))
        price = int(input("Enter price for each: "))
        Pay = count * price
        print("The price is: ", Pay)
        break
    except ValueError:
        print('Error, please enter a numeric. ')
####################################################################################################
'''
寻找第6个默尼森数

经典程序设计问题：找第n个默尼森数。P是素数且M也是素数，并且满足等式M=2**P-1，则称M为默尼森数。例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数。
'''
import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num%i == 0:
            return False
    return True
    
    
def isMonisen(p):
    if isPrime(p) == True and isPrime(2**p-1) == True:
        return True
    return False


def getMonisen(n):
    i = 0
    start = 2
    while i < n:
        while True:
            if isMonisen(start) == True:
                print('i is: {0:d}'.format(i))
                print('start is: {0:d}'.format(start))
                start += 1
                i += 1
            else:
                start += 1
                break
    return 2**start-1


print(getMonisen(6))
