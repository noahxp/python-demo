# example copy from : https://ericjhang.github.io/archives/dad03d64.html

from bs4 import BeautifulSoup
import requests

winning_Numbers_Sort_lotto = ['Lotto649Control_history_dlQuery_No1_', 'Lotto649Control_history_dlQuery_No2_', 'Lotto649Control_history_dlQuery_No3_',
                              'Lotto649Control_history_dlQuery_No4_', 'Lotto649Control_history_dlQuery_No5_', 'Lotto649Control_history_dlQuery_No6_', 'Lotto649Control_history_dlQuery_SNo_']


def search_winning_numbers(css_class):
    global winning_Numbers_Sort_lotto
    if(css_class != None):
        for i in range(len(winning_Numbers_Sort_lotto)):
            if winning_Numbers_Sort_lotto[i] in css_class:
                return css_class


def parse_tw_lotto_html(data_Info, number_count):
    data_Info_List = []
    data_Info_Dict = {}
    tmp_index = 0
    for index in range(len(data_Info)):
        if (index == 0):
            data_Info_List.append(data_Info[index].text)
        else:
            if(index % number_count != 0):
                data_Info_List.append(data_Info[index].text)
            else:
                data_Info_Dict[str(tmp_index)] = list(data_Info_List)
                data_Info_List = []
                data_Info_List.append(data_Info[index].text)
                tmp_index = tmp_index+1
        data_Info_Dict[str(tmp_index)] = list(data_Info_List)
    return data_Info_List, data_Info_Dict


# 捉最後一個月的開獎號碼
head_Html_lotto = 'http://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx'
res = requests.get(head_Html_lotto, timeout=30)
soup = BeautifulSoup(res.text, 'lxml')
header_Info = soup.find_all(id=search_winning_numbers)
data_Info_List, data_Info_Dict = parse_tw_lotto_html(header_Info, 7)
print(data_Info_Dict)
file = open('./lottery/dist/latest-month.txt', 'w')
file.write(str(data_Info_Dict))
file.close()

# 已捉下來的內容
'''
files = ['./lottery/source/202010.html', './lottery/source/202009.html',
         './lottery/source/202008.html', './lottery/source/202007.html', './lottery/source/202006.html']
for f in files:
    f_content = open(f, 'r')
    print(f)
    html = f_content.read()
    f_content.close()
    soup = BeautifulSoup(html, 'lxml')
    header_Info = soup.find_all(id=search_winning_numbers)
    data_Info_List, data_Info_Dict = parse_tw_lotto_html(header_Info, 7)
    print(data_Info_Dict)
'''
