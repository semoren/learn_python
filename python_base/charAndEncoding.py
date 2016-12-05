#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字符串和编码
print('包含中文的str')

print(ord('A'))     # 65
print(ord('中'))    # 20013
print(chr(66))      # B
print(chr(25991))   # 文

print('\u4e2d\u6587')   # 中文  十六进制

print('ABC'.encode('ascii'))
# b'ABC'
print('中文'.encode('UTF-8'))
# b'\xe4\xb8\xad\xe6\x96\x87'

print(b'ABC'.decode('UTF-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len(b'ABC'))                  # 3
print(len('中文'.encode('utf-8')))  # 6
# 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节

print('%2d-%02d' %(3,1)) # ' 3-01'
print('%.2f' % 3.1415926)  # 3.14

s1 = 72
s2 = 85
r = (s2-s1) / s1 * 100
print('%.1f' % r)