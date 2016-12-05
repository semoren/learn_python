# 切片

L = ['one', 'two', 'three', 'java']
print(L[0:3])
print(L[:3])

print(L[-2:])

L = list(range(100))
print(L)
print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2])  # 前10个数，每两个取一个
print(L[::5])   # 每五个取一个

print((0,1,2,3,4,5)[:3])
print('abcdef'[:2])
