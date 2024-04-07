# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

company = '阿里巴巴'
title = '测试标题'
href = '测试链接'
source = '测试来源'
date = '测试日期'

import pymysql
db = pymysql.connect(
    host = 'localhost',
    port = 3309,
    user = 'root',
    password = '',
    database = 'spyder',
    charset = 'utf8'
    )

cur = db.cursor() # 获取会话指针，用来调用 SQL 语句
sql = 'INSERT INTO test(company, title, href, source, date) VALUES(%s, %s, %s, %s, %s)'
db.commit() # 当改变表结构后，更新数据表的操作
cur.close() # 关闭会话指针
db.close() # 关闭数据库连接
