# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""

A,B=map(int,input("Please input 2 integers:").split())
if 0<=A<=100 and 0<=B<=100:
    C=A+B
    print ("{}+{}={}".format(A,B,C))
else:
    print ("input error...")
 