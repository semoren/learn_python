# 列表生成式

print(list(range(1,11)))

L = [x * x for x in range(1,11)]
print(L)

S = [m + n for m in 'ABC' for n in 'XYZ']
print(S)

import os
F = [d for d in os.listdir(".")]
print(F)

d = {'a':1, 'b':2, 'c':3}
for k, v in d.items():
    print(k,'=', v)

L = ['Hello', 'World', 'IBM', 'Apple']
L1 = [s.lower() for s in L]
print(L1)

x = "abc"
y = 123
print(isinstance(x, str))
print(isinstance(y, str))