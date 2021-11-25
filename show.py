# -*- coding:utf-8 -*-
"""
作者：zhaoxz
本项目创建时间：2021年 11月 18日
本项目用于：开始时的图形界面
"""
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import os


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.filePath = tk.StringVar()
        self.pack()
        self.bg_interface()
        self.file_name = tk.StringVar()
        self.file_name = "文件名"



    def bg_interface(self):
        self.e = tk.Label(self, text='请在点击开始后，选择您的输入文件\n选择完成后，关闭该窗口',height=10, font=('宋体', 12))
        self.e.pack(side='top')
        self.b = tk.Button(self, text="开始", width=15, height=2, command=lambda: self.scl_file())
        self.b.pack(side='top')
        # self.b_1 = tk.Button(self, text="完成", width=10, height=1, command=lambda: root.destroy())
        # self.b_1.pack(side='top')


    def scl_file(self):
        a = tk.filedialog.askopenfilename(title=u'选择文件')
        self.file_path = a
        self.e1 = tk.Label(self, text = '您选择的文件是：', height = 2 ,font = ('宋体',12))
        self.e1.pack(side='top')
        file_name = os.path.basename(a)
        self.e2 = tk.Label(self, text=file_name, height=2, font=('宋体', 12))
        self.e2.pack(side='top')
        return self.file_path



