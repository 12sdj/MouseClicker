import threading
import pynput.mouse
from pynput.keyboard import Key, Listener
from tkinter import *
import ctypes
import tkinter.messagebox
import tkinter.simpledialog
from random import*
from time import*
import os

LEFT = 0
RIGHT = 1

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
                tkinter.messagebox.showinfo(title = 'MouseClicker Assitant: info',message='Current State: Listening\n'
                                        ' Press ESC to stop listening.\n'
                                           ' Press F8 to start clicking.')

                # 停止连点也需要调用这个函数
                self.mouse_click()
            else:
                self.running = True
                tkinter.messagebox.showinfo(title = 'MouseClicker Assitant: info',message='Current State: Listening\n'
                                        ' Press ESC to stop listening.\n'
                                           ' Press F8 to start clicking.')
                self.mouse_click()
        elif key == Key.esc:
            tkinter.messagebox.showinfo(title = 'MouseClicker Assitant: info',message='Choose which mouse button you want to click and set the time interval, then click START button to start clicking.') 
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

        
def new_thread_start(button, time):
    MouseClick(button, time)

def start():
    try:
            
        # 将文本框读到的字符串转化为浮点数
        time = float(input.get())
        if mouse.get() == LEFT:

            button = pynput.mouse.Button.left
         
        elif mouse.get() == RIGHT:
    
            button = pynput.mouse.Button.right
    
        t = threading.Thread(target=new_thread_start, args=(button, time))

        #t.setDaemon(True)
        t.start()
    except:
        tkinter.messagebox.showinfo(title = 'MouseClicker Assitant: info',message='You should enter an integer or a float number.')
        tkinter.messagebox.showerror(title = 'MouseClicker Assitant: Error',message='ERROR:Time_out_Not energy')
        tkinter.messagebox.showwarning(title = 'MouseClicker Assitant: Warning',message='WARNING: You should unput a float number in Settings')
  

def settings():
    global result
    result = tkinter.simpledialog.askinteger(title = 'CPS Settings',prompt='                    Set the number of CPS                    ',initialvalue = '5')


root = Tk()
# 高dpi
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/75)

root.title('Mouse Clicker')
root.geometry('450x200')

#
b1 = Button(root, text='Settings', font=('Arial', 12), command=settings)
b1.place(relx=0.55, y=80, relwidth=0.4, height=30)
input = Entry(root, relief="flat", font=("微软雅黑", 10))
input.place(relx=0.55, y=40, relwidth=0.4, height=30)

mouse = IntVar()
lab1 = Label(root, text='Mouse Button', font=("微软雅黑", 11), fg="gray")
lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)
r1 = Radiobutton(root,
                 text='LEFT',
                 font=("微软雅黑", 10),
                 value=0,
                 variable=mouse)
r1.place(relx=0.05, y=40, relwidth=0.15, height=30)
r2 = Radiobutton(root,
                 text='RIGHT',
                 font=("微软雅黑", 10),
                 value=1,
                 variable=mouse)
r2.place(relx=0.2, y=40, relwidth=0.3, height=30)

lab2 = Label(root, text='CPS Settings', font=("微软雅黑", 11), fg="gray")
lab2.place(relx=0.55, y=10, relwidth=0.4, height=30)



btn_start = Button(root,
                   text='START',
                   font=("微软雅黑", 12),
                   fg="white",
                   bg="#207fdf",
                   relief="flat",
                   command=start)
btn_start.place(relx=0.25, y=135, relwidth=0.5, height=30)

root.mainloop()

