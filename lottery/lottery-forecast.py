import numpy as np
import pandas as pd
import ast

files = ['./lottery/dist/202101.txt',
         './lottery/dist/202012.txt', './lottery/dist/202011.txt', './lottery/dist/202010.txt', './lottery/dist/202009.txt', './lottery/dist/202008.txt',  './lottery/dist/202007.txt', './lottery/dist/202006.txt']

lottery_no = []
for f in files:
    f_content = open(f, 'r')
    month = f_content.read()
    month_dict = ast.literal_eval(month)
    for period in month_dict:
        period_no = month_dict.get(period)
        lottery_no.append(period_no)

print(lottery_no)
stat = np.zeros((50, 50), dtype=float)
