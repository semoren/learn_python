#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image

im = Image.open('20160825144524.png')
w, h = im.size
print('size: %sx%s' % (w, h))

im.thumbnail((w//2, h//2))
print('Resize iamge to %sx%s' % (w//2,h//2))
im.save('th.png', 'png')


