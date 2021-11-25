# -*- coding:utf-8 -*-
"""
作者：zhaoxz
本项目创建时间：2021年 11月 09日
本项目用于：导入excel表格并处理
"""

import tkinter as tk
from tkinter import filedialog
import numpy as np
import pandas as pd
from show import Application



"""创造对话框并请求输入文件地址"""
root = tk.Tk()
root.title("处方录入提词器")
root.geometry("500x300")

app = Application(master=root)
app.mainloop()
file_path = app.file_path

"""获取并处理数据"""

'''删除无用数据'''
df = pd.DataFrame(pd.read_excel(file_path))
df = df.drop(
    ['患者姓名', '出生日期', '日期', '药品规格', '单次量', '单次量单位', '开药数量', '频次', '疗程单位', '数量', '单次量单位1', '单价', '医生', '开药数量单位', '数量1'],
    axis=1)
df = df[:-1]

'''储存数据的数据结构'''
column_num = df.shape[0]

df_dict = df.to_dict(orient='index')

# di_1 = {'code', 'ks', 'gd', 'yr', 'zd', 'yp', 'way', 'cost', 'yp2', 'way2'}
# di_2 = {'code', 'ks', 'gd', 'yr', 'zd', 'yp', 'way', 'cost'}
di_1 = {}
di_2 = {}
di_1['if0'] = 1
di_2['if0'] = 1

if0 = 1

'''遍历整个列表，标记重复项'''
i = 1
for i in range(1, column_num):
    code0 = df_dict[i - 1]["处方编码"]
    code1 = df_dict[i]['处方编码']
    df_dict[i]['if1'] = 0
    if code1 == code0:
        df_dict[i - 1]['if0'] = 0
        df_dict[i]['if0'] = 1
    else:
        df_dict[i - 1]['if0'] = 1
        df_dict[i]['if0'] = 1

df_dict[0]['if1'] = 0
j = 0
for j in range(0, column_num - 1):
    if_j = df_dict[j]["if0"]
    if if_j == 0:
        cup = df_dict[j]['药品名称']
        df_dict[j + 1]['yp'] = cup
        cup = df_dict[j]['给药途径']
        df_dict[j + 1]['way'] = cup
        cup = df_dict[j]['费用']
        df_dict[j + 1]['费用'] += cup
        df_dict[j + 1]['if1'] = 1
    else:
        df_dict[j + 1]['if1'] = 0


index = 0
num_pts = 1

def show_rst():
    global index
    global num_pts
    if df_dict[index]['if0'] == 1:

        cup = df_dict[index]['处方编码']
        l_1 = tk.Label(window, text="处方编码:" + str(cup), bg='white', font=('宋体', 12))
        l_1.place(x=10, y=10)

        cup = df_dict[index]['科室']
        l_2 = tk.Label(window, text="科室：" + str(cup), bg='white', font=('宋体', 12))
        l_2.place(x=250, y=10)

        cup = df_dict[index]['性别']
        l_2 = tk.Label(window, text="性别：" + str(cup), bg='white', font=('宋体', 12))
        l_2.place(x=10, y=30)

        cup_n = df_dict[index]['年龄']
        cup_n = round(cup_n)
        l_2 = tk.Label(window, text="年龄：" + str(cup_n), bg='white', font=('宋体', 12))
        l_2.place(x=250, y=30)

        cup = df_dict[index]['诊断']
        l_2 = tk.Label(window, text="诊断：" + str(cup), bg='white', font=('宋体', 12))
        l_2.place(x=30, y=110)

        cup = df_dict[index]['药品名称']
        l_2 = tk.Label(window, text="药品名称：" + str(cup), bg='white', font=('宋体', 12))
        l_2.place(x=30, y=210)

        cup = df_dict[index]['给药途径']
        l_2 = tk.Label(window, text="给药途径：" + str(cup), bg='white', font=('宋体', 12))
        l_2.place(x=170, y=210)

        cup_n = df_dict[index]['费用']
        cup_n = round(cup_n,2)
        l_2 = tk.Label(window, text="费用：" + str(cup_n), bg='white', font=('宋体', 12))
        l_2.place(x=310, y=210)

        l_3 = tk.Label(window, text="这是第" + str(num_pts) + "位患者")
        l_3.place(x=250, y=250)

        num_pts = num_pts + 1

        if df_dict[index]['if1'] == 1:
            cup = df_dict[index]['药品名称']
            l_2 = tk.Label(window, text=str(cup), font=('宋体', 12))
            l_2.place(x=30, y=230)

            cup = df_dict[index]['给药途径']
            l_2 = tk.Label(window, text=str(cup), font=('宋体', 12))
            l_2.place(x=170, y=230)
    index = index + 1
    window.update()




window = tk.Tk()
window.title('处方录入提词器 Ver1.0')
window.geometry('500x300')


b_1 = tk.Button(window, width=15, heigh=2, text="下一项", command=lambda: show_rst())
b_1.place(x=20, y=250)

b_1 = tk.Button(window, width=15, heigh=2, text="结束", command=lambda: window.destroy())
b_1.place(x=70, y=250)


window.mainloop()
