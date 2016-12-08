#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2016, 12, 6, 18, 30, 12)
print(dt)
print(dt.timestamp())

t = 1481020212.0
print(datetime.fromtimestamp(t))

cday = datetime.strptime('2016-12-6 18:00:00', '%Y-%m-%d %H:%M:%S')
print(cday)

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))


tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)