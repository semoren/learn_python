#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('UTF-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
str = f.read().decode('utf-8')
print(str)