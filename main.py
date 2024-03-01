# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:20:33 2024

@author: Administrator
"""

def ranker(score):
    if score < 60:
        return "不及格"
    elif score >= 60 and score < 80:
        return "及格"
    elif score >= 80:
        return "优秀"


import random
name = [chr(ord("a")+i) for i in range(4)]
score = [random.randint(0, 100) for y in range(4)]
p = dict(zip(name, score))
print(p)
for i in range(4):
    print(chr(ord("a")+i),"同学得分",p[chr(ord("a")+i)],ranker(p[chr(ord("a")+i)]))
