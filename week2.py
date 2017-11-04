'''
1.定义函数countchar()按字母表顺序统计字符串中26个字母出现的次数（不区分大小写）。例如字符串“Hope is a good thing.”的统计结果为：
[1, 0, 0, 1, 1, 0, 2, 2, 2, 0, 0, 0, 0, 1, 3, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
'''
#answer:
def countchar(s):
    lst = [0] * 26
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <='z':  
            lst[ord(s[i])- ord('a')] += 1
    print(lst)

if __name__ == "__main__":
    s = "Hope is a good thing."
    s = s.lower()
    countchar(s)
  
#------------------------------------------------------------------------------------------------   
import string
def createDict():
    newDict = {}
    s = string.ascii_letters
    for i in range(len(s)):
        newDict[s[i]] = 0
    return newDict

def countChar(sentence):
    result = createDict()
    for i in range(len(sentence)):
        if sentence[i] in result.keys() and sentence[i].isalpha():
            result[sentence[i]] += 1
    print(result.values())

if __name__ == "__main__":
    s = "Hope is a good thing."
    s = s.lower()
    countChar(s)

######################################################################################################    
'''
2. 有一个咖啡列表['32Latte', '_Americano30', '/34Cappuccino', 'Mocha35']，列表中每一个元素都是由咖啡名称、价格和一些其他非字母字符组成，编写一个函数clean_list()处理此咖啡列表，处理后列表中只含咖啡名称，并将此列表返回。__main__模块中初始化咖啡列表，调用clean_list()函数获得处理后的咖啡列表，并利用zip()函数给咖啡名称进行编号后输出，输出形式如下：

1 Latte

2 Americano

3 Cappuccino

4 Mocha
'''
#answer:
def clean_list(lst):
    cleaned_list = []
    for item in lst:
        for c in item:
            if c.isalpha() != True:
                 item = item.replace(c, '')
        cleaned_list.append(item)
    return cleaned_list                                            

if __name__ == "__main__":
    coffee_list = ['32Latte', '_Americano30', '/34Cappuccino', 'Mocha35']
    cleaned_list = clean_list(coffee_list)
    for k,v in zip(range(1, len(cleaned_list)+1), cleaned_list):
        print(k, v)
#------------------------------------------------------------------------------------------------ 

import re

def clean_list(l):
    for i in range(len(l)):
        l[i] = ''.join(re.findall('[a-zA-Z]+', l[i]))
    return l      

if __name__ == '__main__':
    coffee = clean_list(['32Latte', '_Americano30', '/34Cappuccino', 'Mocha35'])
    ind = range(len(coffee))
    coffee = list(zip(ind, coffee))
    for item in coffee:
        print(str(item[0]) + ' ' + item[1])
        

        
'''
3. 请完成以下文件综合编程迷你项目（提示：可以利用list的insert函数）。

(1) 创建一个文件Blowing in the wind.txt，其内容是：

How many roads must a man walk down

Before they call him a man

How many seas must a white dove sail

Before she sleeps in the sand

How many times must the cannon balls fly

Before they're forever banned

The answer my friend is blowing in the wind

The answer is blowing in the wind

(2) 在文件头部插入歌名“Blowin’ in the wind”

(3) 在歌名后插入歌手名“Bob Dylan”

(4) 在文件末尾加上字符串“1962 by Warner Bros. Inc.”

(5) 在屏幕上打印文件内容
'''
#answser:
def insert_line(lines):
    lines.insert(0, "Blowin' in the wind\n")
    lines.insert(1, "Bob Dylan\n")
    lines.append("1962 by Warner Bros. Inc.")
    return ''.join(lines)

with open('Blowing in the wind.txt', 'r+') as f:
    lines = f.readlines()
    string = insert_line(lines)
    print(string)
    f.seek(0)
    f.write(string)
    
#------------------------------------------------------------------------------------------------ 
import os

def write_file(file, sentences):
    with open (file, 'w+') as f:
        f.write(sentences)

def insert_file(i, text_list, text):
    text_list.insert(i, text)
    return text_list    

if __name__ == '__main__':
    os.chdir('/Users/Erin/Desktop')
    location = os.getcwd()
    sentences = '''
How many roads must a man walk down

Before they call him a man

How many seas must a white dove sail

Before she sleeps in the sand

How many times must the cannon balls fly

Before they're forever banned

The answer my friend is blowing in the wind

The answer is blowing in the wind
            '''
    write_file(location+'/Blowing in the wind.txt', sentences)
    with open(location+'/Blowing in the wind.txt', 'r+') as f:
        text_list = f.readlines()
        text_list = insert_file(0, text_list, 'Blowin’ in the wind\n')
        text_list = insert_file(1, text_list, 'Bob Dylan\n')
        text_list.append('1962 by Warner Bros. Inc.')
    write_file(location+'/Blowing in the wind.txt', ''.join(text_list))   
    print(''.join(text_list))
