# 定义函数

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(10))
print(my_abs(-20))
print(my_abs(12.44))


import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

r = move(100, 100, 60, math.pi / 6)
print(r)

print(pow(3,2))

def quadratic(a, b, c):
    t = math.sqrt(pow(b, 2) - 4 * a * c)
    if(pow(b ,2) - 4 * a *c) > 0:
        return (-b + t) / (2 * a), (-b - t) / (2 * a)
    elif(pow(b, 2) - 4 * a * c) == 0:
        return (-b + t) / (2 * a)
    else:
        return None
print(quadratic(1,2,-3))