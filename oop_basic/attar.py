class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x')) # 有属性'x'吗

print(obj.x)

print(hasattr(obj, 'y'))

setattr(obj, 'y', 19)

print(hasattr(obj, 'y'))

print(getattr(obj, 'y'))

print(obj.y)
setattr(obj, 'x', 2)
print(obj.x)

print(getattr(obj, 'z', 404))

print(hasattr(obj, 'power')) # 是否有属性'power'