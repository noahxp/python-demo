
print('關鍵字參數 demo:')


def f(a, b=2, c=3):
    print(a, b, c)


print('\n有預設值的可以不用帶:')
f(1)
f(1, b=20)
f(1, c=30)


print('\n不定個數參數，類似 java 的 function f(int... a):')


def f(*a):
    for i in a:
        print(i)


f(1)
f(1, 2)


print('\ndemo / * 的參數')
print('- 在「/」前面的參數為: Position-Only Parameters')
print('- 在「*」後面的參數為: Keyword-Only Arguments')


def f(a, /, b=2, *, c=3):
    print(a, b, c)


f(1)
f(1, b=10)
f(1, c=20)
# f(b=10)  # 會執行週期錯誤「TypeError: f() missing 1 required positional argument: 'a'」


print('\ndist type 用 ** 帶入各別的變數:')


def f(a, b=2, c=3):
    print(a, b, c)


d = {'a': 10, 'b': 20}
f(**d)
f(**{'a': 30, 'b': 40, 'c': 50})
