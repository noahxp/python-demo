import numpy as np


# 多維陣列排序,範例:
a = np.array([[2, 7, 4, 2], [35, 9, 1, 5], [22, 12, 3, 2]])
print(a)

# 按最後一列順序排序
b = a[np.lexsort(a.T)]
print('按最後一列順序排序:\n', b)

# 按最後一列逆序排序
b = a[np.lexsort(-a.T)]
print('按最後一列逆序排序:\n', b)

# 按第一列順序排序
b = a[np.lexsort(a[:, ::-1].T)]
print('按第一列順序排序:\n', b)

# 按最後一行順序排序
b = a.T[np.lexsort(a)].T
print('按最後一行順序排序:\n', b)

# 按第一行順序排序
b = a.T[np.lexsort(a[::-1, :])].T
print('按第一行順序排序:\n', b)
