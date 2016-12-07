#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    f = open('D:\\PycharmProjects\\learn_python\\README.md','r', encoding='utf-8')
    print(f.read())
finally:
    if f:
        f.close()

with open('D:\\PycharmProjects\\learn_python\\README.md','r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉

# 如果文件很小，read()一次性读取最方便；
# 如果不能确定文件大小，反复调用read(size)比较保险；
# 如果是配置文件，调用readlines()最方便

with open('D:\\PycharmProjects\\20160825144524.png','rb') as f:
    print(f.read())

with open('D:\\PycharmProjects\\123.txt', 'w') as f:
    f.write('hello, world')