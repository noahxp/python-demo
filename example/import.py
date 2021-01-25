import os  # 第一種import 方式: 基本 import 方式

# 第四種 import 方式，取別名
import platform as pf
# 第二種import 方式: import 所有函式，可以不透過 module 直接取用
from platform import *


import datetime
# 第三種import 方式: import 特定函式
from datetime import date

print('import os  # 基本 import 方式:')
dir = '/tmp/a'

if os.path.exists(dir):
    print(os.path.isdir(dir))
    print(os.path.isfile(dir))
else:
    print(dir, 'is not exist.')

print('\nfrom platform import *  # 可直接使用 platform 裡的函式，不需輸入套件名稱:')
print('system()=', system())
print('release()=', release())
print('platform()=', pf.platform())


print('\n import 特定函式:')
print(date.today())  # 從特定 import 來的函式的使用
print(datetime.date.today())  # 從 datetime 模組使用
