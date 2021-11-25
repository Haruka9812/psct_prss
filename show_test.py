# -*- coding:utf-8 -*-
"""
作者：zhaoxz
本项目创建时间：2021年 11月 18日
本项目用于：
"""
import tkinter as tk
from tkinter import filedialog
import os


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.filePath = tk.StringVar()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 获取文件
        self.getFile_bt = tk.Button(self)
        self.getFile_bt['width'] = 15
        self.getFile_bt['height'] = 1
        self.getFile_bt["text"] = "打开"
        self.getFile_bt["command"] = self._getFile
        self.getFile_bt.grid(row = 10, column = 10)


    # 打开文件并显示路径
    def _getFile(self):
        default_dir = r"文件路径"
        self.filePath = tk.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))


root = tk.Tk()
root.title("处方录入提词器")
root.geometry("500x300")

app = Application(master=root)
app.mainloop()