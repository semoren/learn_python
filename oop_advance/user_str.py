class Student(object):
    def __init__(self, name):
        self.name = name

    # 相当于Java中的toString()
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

print(Student('sermo'))
