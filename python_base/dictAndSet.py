d = {'one':1, 'two':2, 'three':3}
print(d['one'])

d['one']=88
print(d['one'])

print('one' in d) #判断是否存在
print('s' in d)

print(d.get('ss'))      #None
print(d.get('ss', 3))   # 3  不存在返回指定的value

print(d.get('ss') is None)  # True

two = d.pop('two')
print(two)
print(d)

#  list不能作为 key

#-------------set-------------------------
s = set([1,23,3])
print(s)
s = set([1,2,3,4,5,4])
print(s)    #{1, 2, 3, 4, 5}

s.add(6)
s.remove(1)
print(s)

s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)   # {2, 3}
print(s1 | s2)  # {1, 2, 3, 4}

a = ['c','a','b']
a.sort()
print(a)   #['a', 'b', 'c']

a = 'abc'
b = a.replace('a', 'A')
print(a)    #abc
print(b)    #Abc

s = (1,2,3)
b = set([s])
print(b)  # {(1, 2, 3)}

b = {s:2}
print(b.get(s))       #2