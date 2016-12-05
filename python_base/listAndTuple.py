# 使用list和tuple

class_master = ['one', 'two', 'three']
print(class_master)
print(len(class_master))

print(class_master[0])  # one
print(class_master[-1]) # three

class_master.append('admin')
print(class_master)
# ['one', 'two', 'three', 'admin']

class_master.insert(1, 'java')
print(class_master)
#['one', 'java', 'two', 'three', 'admin']

class_master.pop()  # 删除末尾的元素
print(class_master)

temp = class_master.pop(1)
print(temp)
print(class_master)

class_master[0]='java'
print(class_master)

L = ['one', 1, True]
print(L)

s = ['python', 'java', ['asp','php'], 'html']
print(s)
print(len(s)) # 4
L = []
print(len(L))


#-------------------tuple---------------------------------
classMaster = ('one','two','three')
print(classMaster)