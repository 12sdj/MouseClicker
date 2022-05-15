import time
import threading
import pynput.mouse  # pynput和tkinter都有Button这个包，注意区分
from pynput.keyboard import Key, Listener
from tkinter import *
import ctypes
from random import*
import requests
import math

from tqdm import tqdm
import zipfile
import tempfile
import tkinter.messagebox
import tkinter.simpledialog
import webbrowser
import os


LEFT = 0
RIGHT = 1
MIDDLE = 2

# 鼠标连点控制类
class MouseClick:
    def __init__(self, button, time):
        self.mouse = pynput.mouse.Controller()
        self.running = False  # 确认是否在运行
        self.time = time
        self.button = button
        # 开启主监听线程
        self.listener = Listener(on_press=self.key_press)
        self.listener.start()

    def key_press(self, key):
        if key == Key.f8:
            if self.running:
                self.running = False
                state.delete('0.0', END)
                state.insert(INSERT, "Current State: Listening\n")
                state.insert(INSERT, "Press ESC to stop listening.\n")
                state.insert(INSERT, "Press F8 to start clicking.")
                # 停止连点也需要调用这个函数
                self.mouse_click()
            else:
                self.running = True
                state.delete('0.0', END)
                state.insert(INSERT, "Current State: Clicking\n")
                state.insert(INSERT, "Press F8 to stop clicking.\n")
                self.mouse_click()
        elif key == Key.esc:
            btn_start['state'] = NORMAL
            state.delete('0.0', END)
            state.insert(INSERT, "Current State: IDLE\n")
            state.insert(
                INSERT, "Choose which mouse button you want to click and set the time interval, then click START button to start clicking.")
            # 退出主监听线程
            self.listener.stop()

    def mouse_click(self):
        # 这里还需要额外线程进行监听，为了能够更新self.running，防止陷入死循环
        key_listener = Listener(on_press=self.key_press)
        key_listener.start()
        while self.running:
            self.mouse.click(self.button)
            time.sleep(self.time)
        key_listener.stop()


# 新线程处理函数
def new_thread_start(button, time):
    MouseClick(button, time)


# START按键处理函数
def start():
    try:
        # 将文本框读到的字符串转化为浮点数
        time = float(input.get())
        if mouse.get() == LEFT:
            button = pynput.mouse.Button.left
        elif mouse.get() == RIGHT:
            button = pynput.mouse.Button.right
        else:
            button = pynput.mouse.Button.middle
        btn_start['state'] = DISABLED
        state.delete('0.0', END)
        state.insert(INSERT, "Current State: Listening\n")
        state.insert(INSERT, "Press ESC to stop listening.\n")
        state.insert(INSERT, "Press F8 to start clicking.")
        # 开启新线程，避免GUI卡死
        t = threading.Thread(target=new_thread_start, args=(button, time))
        # 开启守护线程，这样在GUI意外关闭时线程能正常退出
        #t.setDaemon(True)
        t.start()
        # 不能使用 t.join()，否则也会卡死
    except:
        state.delete('0.0', END)
        state.insert(INSERT, "Time input ERROR!\n")
        state.insert(INSERT, "You should enter an integer or a float number.")
        tkinter.messagebox.showerror('Error','You should enter an integer or a float number.')

def about():
    state.delete('0.0', END)
    state.insert(INSERT, "MouseClicker PRO PLUS\n")
    state.insert(INSERT, "Major Version: 4.3.2 \n")
    state.insert(INSERT, "Stage Version: 3.3.8 \n")
    state.insert(INSERT, "2022/5/15 16:08 Update 16 (Made by 12sdj) \n")

def update():
    state.delete('0.0', END)
    state.insert(INSERT, "<Checking ...>\n")
    tkinter.messagebox.showerror('Error','CHECK FOR UPDATE is read-only, you can"t read it')

 



    
def logs():
    state.delete('0.0', END)
    state.insert(INSERT, "Update 16\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Add a button \n")
    state.insert(INSERT, " 2. Optimization Experience to Reduce the bug occurs \n")
    
    state.insert(INSERT, "Update 15(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Add some buttons \n")
    
    state.insert(INSERT, "Update 14\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Add Middle-click button \n")
    state.insert(INSERT, " 2. Optimize the user interface \n")
    
    state.insert(INSERT, "Update 13(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Fix bugs \n")
    state.insert(INSERT, " 2. Optimize the user interface \n")

    
def more():
    def handler():
        window = Toplevel()
        window.geometry("850x680")
        window.title("LICENSE")
        
        state = Text(window, relief="flat", font=("微软雅黑", 10))
        state.place(relx=0.03, y=10, relwidth=0.95, height=660)
        state.insert(INSERT, "MIT License\n")
        state.insert(INSERT, "\n")
        state.insert(INSERT, "Copyright (c) 2022 12sdj\n")
        state.insert(INSERT, "\n")
        state.insert(INSERT, "Permission is hereby granted, free of charge, to any person obtaining a copy\n")
        state.insert(INSERT, "of this software and associated documentation files (the 'Software'), to deal\n")
        state.insert(INSERT, "in the Software without restriction, including without limitation the rights\n")
        state.insert(INSERT, "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n")
        state.insert(INSERT, "copies of the Software, and to permit persons to whom the Software is\n")
        state.insert(INSERT, "furnished to do so, subject to the following conditions:\n")
        state.insert(INSERT, "\n")
        state.insert(INSERT, "The above copyright notice and this permission notice shall be included in all\n")
        state.insert(INSERT, "copies or substantial portions of the Software.\n")
        state.insert(INSERT, "\n")
        state.insert(INSERT, "THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n")
        state.insert(INSERT, "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n")
        state.insert(INSERT, "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n")
        state.insert(INSERT, "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n")
        state.insert(INSERT, "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n")
        state.insert(INSERT, "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n")
        state.insert(INSERT, "SOFTWARE.\n")
        window.mainloop()
        
    def update():
        global down
        update = Toplevel()
        update.geometry("680x200")
        update.title("Download the Update manually")
        
        tkinter.messagebox.showerror('Error','Download the Update manually is read-only, you can"t read it')
   
        update.mainloop()
    def view():
        if tkinter.messagebox.askyesno('Ask', 'The following will open https://github.com/12sdj/MouseClicker-by-12sdj.git. Are you sure to execute?') == 1:
            try:
                webbrowser.open('https://github.com/12sdj/MouseClicker-by-12sdj.git')
            except:
                tkinter.messagebox.showerror('Error','Unknown error')
        
        
    otherFrame = Toplevel()
    otherFrame.geometry("540x300")
    otherFrame.title("MouseClicker PRO PLUS - More")
    

    btn = Button(otherFrame, text="LICENSE",font=('Arial', 14), command=handler)
    btn.pack()
    btn1 = Button(otherFrame, text="Download the Update manually", font=('Arial', 14), command=update)
    btn1.pack()
    btn2 = Button(otherFrame, text="View the source code", font=('Arial', 14), command=view)
    btn2.pack()

    otherFrame.mainloop()

    
# -------------------------------- GUI界面 --------------------------------
root = Tk()
# 高dpi
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/75)

root.title('MouseClicker PRO PLUS')
root.geometry('800x330')

mouse = IntVar()
lab1 = Label(root, text='Mouse Button', font=("微软雅黑", 11), fg="gray")
lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)
r1 = Radiobutton(root,
                 text='LEFT',
                 font=("微软雅黑", 10),
                 value=0,
                 variable=mouse)
r1.place(relx=0.05, y=40, relwidth=0.1, height=30)
r2 = Radiobutton(root,
                 text='RIGHT',
                 font=("微软雅黑", 10),
                 value=1,
                 variable=mouse)
r2.place(relx=0.18, y=40, relwidth=0.1, height=30)
r3 = Radiobutton(root,
                 text='MIDDLE',
                 font=("微软雅黑", 10),
                 value=2,
                 variable=mouse)
r3.place(relx=0.31, y=40, relwidth=0.12, height=30)

lab2 = Label(root, text='Time Interval', font=("微软雅黑", 11), fg="gray")
lab2.place(relx=0.55, y=10, relwidth=0.4, height=30)
input = Entry(root, relief="flat", font=("微软雅黑", 10))
input.place(relx=0.55, y=40, relwidth=0.4, height=30)

label3 = Label(root,
               text='---------- Current State and Instruction ----------',
               font=("微软雅黑", 8),
               fg="gray")
label3.place(relx=0.05, y=90, relwidth=0.9, height=20)
state = Text(root, relief="flat", font=("微软雅黑", 10))
state.place(relx=0.05, y=110, relwidth=0.9, height=120)
state.insert(INSERT, "Current State: IDLE\n")
state.insert(INSERT, "Choose which mouse button you want to click and set the time interval, then click START button to start listening.")

btn_start = Button(root,
                   text='START',
                   font=("微软雅黑", 12),
                   fg="white",
                   bg="#207fdf",
                   relief="flat",
                   command=start)
btn_start.place(relx=0.6, y=240, relwidth=0.35, height=30)
b2 = Button(root, text='ABOUT', font=('Arial', 10),command=about)
b2.place(relx=0.05, y=240, relwidth=0.15, height=30)
b1 = Button(root, text='CHECK FOR UPDATES', font=('Arial', 10),command=update)
b1.place(relx=0.05, y=272, relwidth=0.285, height=30)
b3 = Button(root, text='CHANGELOG', font=('Arial', 10),command=logs)
b3.place(relx=0.21, y=240, relwidth=0.20, height=30)
b4 = Button(root, text='MORE', font=('Arial', 10),command=more)
b4.place(relx=0.345, y=272, relwidth=0.115, height=30)


root.mainloop()
