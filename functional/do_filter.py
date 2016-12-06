def is_old(n):
    return n % 2 == 1
r= list(filter(is_old, [1,2,3,4,5,6,7,8]))
print(r)

def not_empty(s):
    return s and s.strip()
r = list(filter(not_empty, ['A','','B',None,'C','  ']))
print(r)

# 生成器 无限序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) #构造新序列

for n in primes():
    if n < 100:
        print(n)
    else:
        break