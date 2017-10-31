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
