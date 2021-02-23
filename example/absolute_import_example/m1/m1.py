from m1.m2.m2 import bar


def foo():
    print('I am foo in m1 of absolute import example')
    bar('x')


bar('y')
print('z')
