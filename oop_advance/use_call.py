class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('my name is %s' % self.name)

f = Student('s')
f()

print(callable(Student('')))  #判断对象是否是“可调用”对象
