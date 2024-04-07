# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymysql
db = pymysql.connect(
    host = 'localhost',
    port = 3309,
    user = 'root',
    password = '',
    database = 'spy',
    charset = 'utf8'
    )


company = '小米'
title = '测试标题'

cur = db.cursor() # 获取会话指针，用来调用 SQL 语句
sql = 'SELECT * FROM spyder WHERE company = %s AND title = %s'
cur.execute(sql, (company, title))
data = cur.fetchall() # 提取所有数据，并且赋值给 data 变量
print(data)
db.commit() # 没有改变表的结构可以不用写这一条
cur.close() # 关闭会话指针
db.close() # 关闭数据库连接
