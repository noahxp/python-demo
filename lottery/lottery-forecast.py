import os
import numpy as py
import pandas as pd

forcast = []  # 下期投注獎號

all = []  # 每期的所有獎號
for filename in sorted(os.listdir('./lottery/data')):
    with open(os.path.join('./lottery/data/', filename), 'r') as file:
        print(filename)
        csv = pd.read_csv(file, header=None, skiprows=1,
                          usecols=[6, 7, 8, 9, 10, 11, 12])
        if len(all) == 0:
            all = csv
        else:
            all = pd.concat([all, csv], ignore_index=True)

all = all.values

##### 馬可夫矩陣-start #####
# 計算上、下期關係
stat = py.zeros((50, 50), dtype=float)
for i in range(all.__len__()):  # i 所有期數
    if i == all.__len__()-1:  # 最後一期沒有下一期
        break
    for j in range(all[i].__len__()):  # j 每期獎號
        for k in range(all[i+1].__len__()):  # k 下期獎號
            stat[all[i][j], all[i+1][k]] += 1.0

# 計算機率
summary = py.zeros(50, dtype=float)
percent = py.zeros((50, 50), dtype=float)
for i in range(50):
    summary[i] = py.sum(stat[i])  # 每一列的總合
    for j in range(50):
        if stat[i, j] != 0:
            percent[i, j] = stat[i, j] / summary[i]

markov_model_forcast = []  #
last = all[all.__len__()-1]
print('最近一期號碼:', last)  # 最近一期
for i in range(len(last)):
    idx = py.argsort(stat[last[i]])
    # print(last[i], idx[49:50], percent[last[i], idx[49:50]])
    markov_model_forcast.append([idx[49:50][0], percent[last[i], idx[49:50][0]]])

markov_model_forcast.sort(key=lambda x: x[1], reverse=True)
for i in range(5):  # 取5個號碼，
    forcast.append(markov_model_forcast[i][0])

print('markov_model排序後機率=', markov_model_forcast, '\n')
##### 馬可夫矩陣-end #####


##### 次數最多-start #####
most = py.zeros((50), dtype=int)
for i in range(all.__len__()):
    for j in all[i]:
        most[j] += 1
most_top = py.zeros(3, int)
for i in range(3):
    idx = most.argmax()
    most_top[i] = idx
    most[idx] = 0
print('前三開出的獎號:', most_top)
forcast.append(most_top[0])

##### 次數最多-end #####

forcast.sort()
print('下期建議投註:')
print(forcast)
