#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import struct

# pack的第一个参数是处理指令，'>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
s = struct.pack('>I', 10240099)
print(s)

u = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(u)


with open('D:\\PycharmProjects\\learn_python\\test1.bmp','rb') as f:
    s = f.read(30)
    print(s)
    print(struct.unpack('<ccIIIIIIHH',s))