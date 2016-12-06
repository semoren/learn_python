def lazy_sum(*args):
    def calc_sum():
        sum = 0
        for n in args:
            sum = sum + n
        return sum
    return calc_sum

f = lazy_sum(1,2,3,4,5)
print(f)
print(f())

f1 = lazy_sum(1,2,3,4,5)
f2 = lazy_sum(1,2,3,4,5)
print(f1 == f2)  #False
