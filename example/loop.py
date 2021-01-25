
print('while-loop 範例:')
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue

    print('i=', i)

else:
    print('The end, while 條件已不成立')


print('for-loop 範例:')

print('for-in string:')
for x in ('banana'):
    print(x)


print('for-in arrays:')
fruits = ['apple', 'banana', 'guava']
for x in fruits:
    print(x)


print('for in range(6):')
for x in range(6):
    print(x)

print('for in range(2,6):')
for x in range(2, 6):
    print(x)

print('for in range(3,30,3):')
for x in range(3, 30, 3):
    print(x)


a = ['a', 'b', 'c']
b = ['1', '2', '3']
for x in a:
    for y in b:
        print(x, y)
