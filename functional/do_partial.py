# 偏函数
print(int('123'))

print(int('123', base=8))
print(int('16',base=16))


def int2(x, base=2):
    return int(x, base)

print(int2('100000'))

import functools
int2 = functools.partial(int, base=2)
print(int2('1000'))
