from functools import reduce
def add(x, y):
    return x + y
r = reduce(add, [1, 2, 3, 4, 5])
print(r)

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def fn(x,y):
    return x * 10 + y

r = reduce(fn, [1,3,5,7])
print(r)