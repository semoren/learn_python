# 迭代
d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)

for ch in 'asb':
    print(ch)

from collections import Iterable
from collections import Iterator
print(isinstance('abc', Iterable))  # str是否可迭代

for i, value in enumerate(['a','b','c']):
    print(i, value)

for x, y in [(1,1),(2,4),(3,9)]:
    print(x,y)


# 可以使用isinstance()判断一个对象是否是Iterator对象
print(isinstance((x for x in range(10)), Iterator))
# True
print(isinstance([], Iterator))     # False
print(isinstance({}, Iterator))     # False
print(isinstance("abc", Iterator))  # False

print(isinstance(iter("abc"), Iterator))    # True

# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
