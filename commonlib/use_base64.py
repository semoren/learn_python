#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64

e = base64.b64encode(b'binary\x00string')
print(e)

d = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(d)

e = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(e)

e = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(e)


def safe_base64_decode(s):
    x = len(s) % 4 != 0
    if x != 0:
        s = s + b'=' * (4-x)
    d = base64.b64decode(s)
    print(d)
safe_base64_decode(b'YmluYXJ5AHN0cmluZw')

print(b'=' * 2)