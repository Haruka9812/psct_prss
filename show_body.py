# -*- coding:utf-8 -*-
"""
作者：zhaoxz
本项目创建时间：2021年 11月 19日
本项目用于：显示主体部分
"""

import tkinter as tk

def show_body(**dic):
    window = tk.Tk()
    window.title('处方录入提词器 Ver1.0')
    window.geometry('500x300')

    cup = dic['处方编码']
    l_1 = tk.Label(window,text = "处方编码:"+str(cup))

    l_1.place(x = 10, y = 10)
    # l_1_ans = tk.Label(window,text = dic['处方编码'])
    # l_1_ans.place(x=100, y=10)
    window.mainloop()