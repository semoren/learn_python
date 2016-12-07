#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
r = r'^\d{3}\-\d{3,8}$'
if re.match(r, '010-12345'):
    print('ok')
else:
    print('faild')

print(re.split(r'[\s\,]+', 'a,b,c d'))

print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))


m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))


re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-123765').group())