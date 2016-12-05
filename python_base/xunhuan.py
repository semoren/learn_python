# 循环
names = ['one', 'two', 'three']
for name in names:
    print('your name=', name)

sum = 0
for i in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + i
print(sum)

sum = 0
for i in range(101):
    sum = sum + i
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

