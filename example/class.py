class a:
    """
    this is a class
    """
    i = 3   # public variables
    _j = 3  # private variables

    def __init__(self):   # 建構子
        print('run constructor')

    def add(self, x, y):
        """ this is a method """
        return x+y

    def sub(self, x, y):
        return x-y


x = a()
print(x.add(1, 2))
print(x.sub(1, 2))

a.i = a.i + 1
print(a.i, x.i)  # result: 4 4 (a改變x跟著改變)

x.i = x.i + 1
print(a.i, x.i)  # result: 4 5 (x改變a不變)

y = a()
print(a.i, y.i)  # result: 4 4

if isinstance(x, a):
    print('x object is instance of a')

if not isinstance(x, str):
    print('x object is not instance of str ')
