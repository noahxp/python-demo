
print('continue & break 範例:')
for i in range(6):
    if (i == 3):
        continue  # 執行下一個疊代(next i)
    if (i == 5):
        break  # 離開迴圈

    print(i)


print('pass 範例:')


def f():
    pass  # 沒特別要執行的內容，可以用「pass」關鍵字替代


f()


# 以下二行，變成 deadlock
# while True:
#     pass
