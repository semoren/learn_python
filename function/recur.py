# 递归函数

def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)
print(fact(6))
print(fact(100))


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

def fact2(n):
    return fact_iter(n, 1)
