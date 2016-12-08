#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter
Point = namedtuple('Point',['x', 'y'])
p = Point(1, 2)
print(p)

print(isinstance(p, Point))
print(isinstance(p, tuple))

# namedtuple('名称', [属性list]):
Cricle = namedtuple('Cricle', ['x', 'y', 'r'])

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print(d)
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)
od = OrderedDict()
od['x']=1
od['z']=2
od['y']=3
print(list(od.keys()))

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('add:',(key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

# Counter是一个简单的计数器，例如，统计字符出现的个数：
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)