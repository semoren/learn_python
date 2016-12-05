def power(x, n=2):
    r = 1
    while n > 0:
        n = n - 1
        r = r * x
    return r
print(power(2,3))
print(power(3,3))
print(power(3))


def calc(numbers):
    sum = 0
    for i in numbers:
        sum = sum +  i * i
    return sum
print(calc([1,2,3,4,5]))
print(calc((1,2,3)))


def calcc(*numbers):
    s = 0
    for i in  numbers:
        s = s + i * i
    return s

print(calcc(1,2,3))
print(calcc(1,2,3,4))
nums = [1,2,3]
print(calcc(*nums))


def person(name, age, **kw):
    print('name:',name, 'age:',age, 'other:', kw)

person('one', 12)
person('two', 20, city='beijing')