import makefood  # 導入 makefood 所有函式
import random
import twstock

from makefood import make_drink  # 導入單一函式，該函式能直接使用

makefood.make_icecream('a', 'b', 'c')
makefood.make_drink('large', 'cola')


make_drink('small', 'soda')

no = [1, 2, 3, 4, 5, 6]
print('random choice:', random.choice(no))

print('打亂前:', no)
random.shuffle(no)
print('打亂後', no)

for i in range(10):
    print(random.choice(no), end=',')

print(random.sample(range(1, 50), 6))

for i in range(1, 3):
    print(i)


stock2330 = twstock.stock.Stock('2330')
print(stock2330.fetch_from(2020, 1))
print(stock2330.price)
