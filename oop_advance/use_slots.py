class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name='sermo' #动态给实例绑定一个属性
print(s.name)

def set_age(self, age):  #定义一个函数作为实例方法
    self.age = age

from  types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25)
print(s.age)


def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)
