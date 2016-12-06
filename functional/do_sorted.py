print(sorted([12,1,34,12,-2]))

print(sorted([12,1,34,12,-2], key=abs))

L = [12,1,34,12,-2]
print(L)
print(sorted(L))
print(L)

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

from operator import itemgetter
students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))