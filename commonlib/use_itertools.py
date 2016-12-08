#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools

# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# ca = itertools.count('abc')
#
# for c in ca:
#     print(c)

ns = itertools.repeat('abs', 3)
for n in ns:
    print(n)

nstuals = itertools.count(1)
# takewhile()等函数根据条件判断来截取出一个有限的序列：
ns = itertools.takewhile(lambda x: x<=10, nstuals)
print(list(ns))


for c in itertools.chain('ABC','123'):
    print(c)
#     A B C 1 2 3

for key, group in itertools.groupby('AAABBBCCAAAa'):
    print(key, list(group))
# A ['A', 'A', 'A']
# B ['B', 'B', 'B']
# C ['C', 'C']
# A ['A', 'A', 'A']
# a ['a']

for key, group in itertools.groupby('AAABBBCCAAAa', lambda c: c.upper()):
    print(key, list(group))
# A ['A', 'A', 'A']
# B ['B', 'B', 'B']
# C ['C', 'C']
# A ['A', 'A', 'A', 'a']