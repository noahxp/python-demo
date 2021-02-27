# example copy from : https://ericjhang.github.io/archives/dad03d64.html

import pandas as pd
from bs4 import BeautifulSoup
import requests

'''
Lotto649Control_history_dlQuery_L649_DrawTerm_ : 期
Lotto649Control_history_dlQuery_L649_DDate_ : 開獎日
Lotto649Control_history_dlQuery_L649_SellAmount_ 銷售總額
'''
winning_numbers_sort_lotto = [
    'Lotto649Control_history_dlQuery_L649_DrawTerm_',
    'Lotto649Control_history_dlQuery_L649_DDate_',
    'Lotto649Control_history_dlQuery_No1_', 'Lotto649Control_history_dlQuery_No2_', 'Lotto649Control_history_dlQuery_No3_',
    'Lotto649Control_history_dlQuery_No4_', 'Lotto649Control_history_dlQuery_No5_', 'Lotto649Control_history_dlQuery_No6_', 'Lotto649Control_history_dlQuery_SNo_']


def search_winning_numbers(css_class):
    global winning_numbers_sort_lotto
    if(css_class != None):
        for i in range(len(winning_numbers_sort_lotto)):
            if winning_numbers_sort_lotto[i] in css_class:
                return css_class


def parse_tw_lotto_html(html_data):
    row_len = winning_numbers_sort_lotto.__len__()
    ''' html_data : html data\n number_count: 每期捉幾號'''
    lottery_list = []
    total_cycle = len(html_data)//row_len
    idx = 0
    for i in range(total_cycle):
        cycle_array = ['大樂透']
        for j in range(row_len):
            if j == 2:
                cycle_array.append('')
                cycle_array.append('')
                cycle_array.append('')
            idx = i*row_len + j
            tmp = html_data[idx].text
            cycle_array.append(tmp)
            # print(idx)
        cycle_array.append('')
        cycle_array.append('')
        cycle_array.append('')
        cycle_array.append('')
        cycle_array.append('')
        lottery_list.append(cycle_array)
    return lottery_list


# 捉最後一個月的開獎號碼
'''
head_Html_lotto = 'http://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx'
res = requests.get(head_Html_lotto, timeout=30)
soup = BeautifulSoup(res.text, 'lxml')
header_Info = soup.find_all(id=search_winning_numbers)
data_Info_List, data_Info_Dict = parse_tw_lotto_html(header_Info, 7)
print(data_Info_Dict)
file = open('./lottery/dist/latest-month.txt', 'w')
file.write(str(data_Info_Dict))
file.close()
'''

# 已捉下來的內容
files = ['./lottery/source/202102.html']
for file in files:
    f = open(file, 'r')
    print(file)
    html = f.read()
    f.close()
    soup = BeautifulSoup(html, 'lxml')
    lottery_html = soup.find_all(id=search_winning_numbers)
    lottery_list = parse_tw_lotto_html(lottery_html)
    # print('\n\n')
    # print(lottery_list)
    df = pd.DataFrame(lottery_list)
    df.to_csv('./lottery/dist/2.csv', index=False)
    print('done')
