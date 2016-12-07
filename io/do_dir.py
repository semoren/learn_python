#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
print(os.name)
# print(os.uname())  windows下不提供


print(os.environ)
print(os.environ.get('PATH'))

print(os.environ.get('x','default'))

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
path = os.path.join('D:\PycharmProjects\learn_python','testDir')
print(path)
# 然后创建一个目录:
os.mkdir(path)
# 删掉一个目录:
os.rmdir(path)

L = os.path.split('D:\PycharmProjects\learn_python\README.md')
print(L)

L = os.path.splitext('D:\PycharmProjects\learn_python\README.md')
print(L)

# os.rename('ceshi.py', 'with_file.py')
# os.remove('asd.py')

#  所有目录
l = [x for x in os.listdir('.') if os.path.isdir(x)]
print(l)

L = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(L)
