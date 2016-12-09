#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mysql.connector

conn = mysql.connector.connect(user='root', password='123456', database='test')

cursor = conn.cursor()

cursor.execute('insert into user(id, age, name) VALUES (%s, %s, %s)', ['1', 20, 'sermo'])
print(cursor.rowcount)

conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id=%s',('1',))
values = cursor.fetchall()
print(values)
cursor.close()
