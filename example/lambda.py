print('anonymous function(lambda):')


def f(n):
    return lambda a: a*n


f2 = f(2)  # f 回傳一個 anonymous function
print(f2(2))


print('\n用 lambda 指定排序欄位:')
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])  # 用 lamba 指定欄位排序
print(pairs)

pairs.sort(key=lambda pair: pair[0], reverse=True)
print(pairs)
