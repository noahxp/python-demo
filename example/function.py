
print('function 一般應用:')


def abc():
    pass


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


print(abc())
print(add(1, 2))
print(subtract(1, 2))


print('參數帶預設值，類似OOP的Overload多載:')


def fun(a, b=3, c=[]):  # b 變數是一般型別，不會被覆寫掉，c 變數是物件型別(reference type)，如 list, dictionary, 或一般物件，則值會被改版
    if (a == 3):
        b = 9
    c.append(a)
    print('a=', a, ',b=', b, ',c=', c)


fun(1)
fun(1, 2)
fun(3)
fun(1)


def fun_L(a, L=[]):  # L 是 array 屬於 reference type ，值將會被一直改變
    L.append(a)
    return L


print(fun_L(1))
print(fun_L(2))
print(fun_L(3))
