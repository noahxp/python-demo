
def make_icecream(*toppings):
    '''列出製作冰淇淋的材料'''
    print('冰淇淋材料如下')
    for topping in toppings:
        print(topping)


def make_drink(size, drink):
    '''飲料種類及大小'''
    print(f'{drink}:{size}')
