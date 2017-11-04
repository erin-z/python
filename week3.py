'''
已知有一个列表中存放了一组音乐数据：
music_data = [("the rolling stones","Satisfaction"),("Beatles","Let It Be"),("Guns N' Roses","Don't Cry"),("Metallica","Nothing Else Matters")]
请根据这组数据创建一个如下的DataFrame：

               singer             song_name
1  the rolling stones          Satisfaction
2             Beatles             Let It Be
3       Guns N' Roses             Don't Cry
4           Metallica  Nothing Else Matters
'''

import pandas as pd
music_data = [("the rolling stones","Satisfaction"),("Beatles","Let It Be"),("Guns N' Roses","Don't Cry"),("Metallica","Nothing Else Matters")]
pd_music = pd.DataFrame(music_data)

music_table = pd.DataFrame(music_data, index=range(1, 5))
music_table.columns = ['singer', 'song_name'] 
print(music_table)

################################################################################################################
'''
对于一个已分词的中文句子：
"我 是 一个 测试 句子，大家 赶快 来 统计 我 吧，大家 赶快 来 统计 我 吧，家 赶快 来 统计 我 吧，重要 事情 说 三遍！"
可以用collections模块中的Counter()函数方便地统计词频，例如可用如下代码：
'''
import collections
s = "我 是 一个 测试 句子，大家 赶快 来 统计 我 吧，大家 赶快 来 统计 我 吧，家 赶快 来 统计 我 吧，重要 事情 说 三遍！"
s_list = s.split()
[s_list.remove(item) for item in s_list if item in '，。！”“']
print(collections.Counter(s_list))

#------------------------------------------------------------------------------------------------
s_dict = {}
for item in s_list:
    if item not in '，。！”“':
        if item in s_dict.keys():
            s_dict[item] += 1
        else:
            s_dict[item] = 1
print(s_dict)
