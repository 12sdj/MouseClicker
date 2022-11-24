import time
import threading
import pynput.mouse  # pynput和tkinter都有Button这个包，注意区分
from pynput.keyboard import Key, Listener
from tkinter import *
import ctypes
from random import*
import requests
import math
from tkinter import ttk
from tqdm import tqdm
import zipfile
import tempfile
import tkinter.messagebox
import tkinter.simpledialog
import webbrowser
import os
from urllib import request
import sys
import subprocess 
import ffmpeg
from ttkthemes import *
import setproctitle

import getpass
import winshell#pip install pywin32 -i https://pypi.tuna.tsinghua.edu.cn/simple/
import win32con#pip install pypiwin32
import win32api
import winreg


LEFT = 0
RIGHT = 1
MIDDLE = 2

ON = 3
OFF = 4
global lan
#----------------------------------------------------------------------
deskTopDir = winshell.desktop()
drive = os.getenv("SystemDrive")
user_name = getpass.getuser()


#--------------------------------------------------------
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
                input.configure(state='normal')
                self.running = False
                state.delete('0.0', END)
                
                if lan == 2:
                    state.insert(INSERT, "Current State: Listening\n")
                    state.insert(INSERT, "Press ESC to stop listening.\n")
                    state.insert(INSERT, "Press F8 to start clicking.")
                elif lan == 3:
                    state.insert(INSERT, "Текущее состояние: прослушивание нажатий клавиш\n")
                    state.insert(INSERT, "Нажмите ESC для завершения прослушивания\n")
                    state.insert(INSERT, "Нажмите F8, чтобы запустить программу")
                elif lan == 4:
                    state.insert(INSERT, "Aktueller Status: Abhören von Tastatureingaben\n")
                    state.insert(INSERT, "ESC drücken, um das Anhören zu beenden.\n")
                    state.insert(INSERT, "Drücken Sie F8, um das Programm zu starten.")
                elif lan == 5:
                    state.insert(INSERT, "現在の状態：キー入力のリスニング中\n")
                    state.insert(INSERT, "ESCを押して試聴を終了する.\n")
                    state.insert(INSERT, "F8キーを押して、プログラムを開始します.")
                else:
                    state.insert(INSERT, "当前状态：正在监听按键\n")
                    state.insert(INSERT, "按下ESC键结束监听\n")
                    state.insert(INSERT, "按下F8键开始运行程序")
                # 停止连点也需要调用这个函数
                self.mouse_click()
            else:
                input.configure(state='readonly')
                self.running = True
                state.delete('0.0', END)
                if lan == 2:
                    state.insert(INSERT, "Current State: Clicking\n")
                    state.insert(INSERT, "Press F8 to stop clicking.\n")
                elif lan == 3:
                    state.insert(INSERT, "Текущее состояние: Работает\n")
                    state.insert(INSERT, "Нажмите F8, чтобы завершить выполнение.\n")
                elif lan == 4:
                    state.insert(INSERT, "Aktueller Status: Läuft\n")
                    state.insert(INSERT, "Drücken Sie F8, um den Lauf zu beenden.\n")
                elif lan == 5:
                    state.insert(INSERT, "現在の状況: ランニング中\n")
                    state.insert(INSERT, "F8キーを押してランを終了する.\n")
                else:
                    state.insert(INSERT, "当前状态：正在运行\n")
                    state.insert(INSERT, "按下F8键结束运行\n")
                self.mouse_click()
        elif key == Key.esc:
            input.configure(state='normal')
            if self.running:
                self.running = False
                self.mouse_click()
            input.delete(0, 'end')
            btn_start['state'] = NORMAL
            state.delete('0.0', END)

            
            
            if lan == 2:
                state.insert(INSERT, "Current State: IDLE\n")
                state.insert(INSERT, "Choose which mouse button you want to click and enter CPS in CPS setting, then click START button to start clicking.")
            elif lan == 3:
                state.insert(INSERT, "Текущий статус: Ожидание\n")
                state.insert(INSERT, "Выберите объект щелчка мыши и введите CPS в поле 'Параметры CPS', затем вы можете нажать кнопку 'Нажмите для запуска', чтобы запустить программу")

            elif lan == 4:
                state.insert(INSERT, "Aktueller Status: In Erwartung\n")
                state.insert(INSERT, "Wählen Sie ein Mausklick-Objekt aus und geben Sie CPS in das Feld 'CPS-Einstellungen' ein, dann können Sie auf die Schaltfläche 'Zum Starten klicken' klicken, um das Programm zu starten")

            elif lan == 5:
                state.insert(INSERT, "現在の状態：アイドル\n")
                state.insert(INSERT, "マウスクリックオブジェクトを選択し、「CPS設定」フィールドにCPSを入力すると、「クリックで起動」ボタンをクリックしてプログラムを実行することができます")

            else:
                state.insert(INSERT, "当前状态：空闲\n")
                state.insert(INSERT, "选择一个鼠标点击对象并在‘CPS 设置’一栏中输入CPS， 然后，你就可以点击'点击以开始'按钮以运行程序")
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
def bth_start():
    #print("1")
    try:
        # 将文本框读到的字符串转化为浮点数
        #print("test")
        ach = float(input.get())
        time = 1 / ach
        #print(time)
        if mouse.get() == LEFT:
            button = pynput.mouse.Button.left
        elif mouse.get() == RIGHT:
            button = pynput.mouse.Button.right
        else:
            button = pynput.mouse.Button.middle
        btn_start['state'] = DISABLED
        state.delete('0.0', END)
        try:
            
     
            if lan == 2:
                try:
                    state.insert(INSERT, "Current State: Listening\n")
                    state.insert(INSERT, "Press ESC to stop listening.\n")
                    state.insert(INSERT, "Press F8 to start clicking.")
                except:
                    tkinter.messagebox.showerror('Error','Unknown error')
            elif lan == 3:
                try:
                    state.insert(INSERT, "Текущее состояние: прослушивание нажатий клавиш\n")
                    state.insert(INSERT, "Нажмите ESC для завершения прослушивания\n")
                    state.insert(INSERT, "Нажмите F8, чтобы запустить программу")
                except:
                    tkinter.messagebox.showerror('Error','Unknown error')
            elif lan == 4:
                try:
                    state.insert(INSERT, "Aktueller Status: Abhören von Tastatureingaben\n")
                    state.insert(INSERT, "ESC drücken, um das Anhören zu beenden.\n")
                    state.insert(INSERT, "Drücken Sie F8, um das Programm zu starten.")
                except:
                    tkinter.messagebox.showerror('Error','Unknown error')
            
            elif lan == 5:
                try:
                    state.insert(INSERT, "現在の状態：キー入力のリスニング中\n")
                    state.insert(INSERT, "ESCを押して試聴を終了する.\n")
                    state.insert(INSERT, "F8キーを押して、プログラムを開始します.")
                except:
                    tkinter.messagebox.showerror('Error','Unknown error')
            else:
                try:
                    state.insert(INSERT, "当前状态：正在监听按键\n")
                    state.insert(INSERT, "按下ESC键结束监听\n")
                    state.insert(INSERT, "按下F8键开始运行程序")
                except:
                    tkinter.messagebox.showerror('Error','Unknown error')
        except:
            tkinter.messagebox.showerror('Error','Unknown error')
        # 开启新线程，避免GUI卡死
        t = threading.Thread(target=new_thread_start, args=(button, time))
        # 开启守护线程，这样在GUI意外关闭时线程能正常退出
        t.setDaemon(True)
        t.start()
        # 不能使用 t.join()，否则也会卡死
    except:
        state.delete('0.0', END)
        if lan == 2:
            try:
                state.insert(INSERT, "CPS input ERROR!\n")
                state.insert(INSERT, "You should enter an integer or a float number.")
                tkinter.messagebox.showerror('Error','You should enter an integer or a float number.')
            except:
                tkinter.messagebox.showerror('Error','Unknown error')
        elif lan == 3:
            try:
                state.insert(INSERT, "Ошибка ввода CPS\n")
                state.insert(INSERT, "Вы должны были ввести целое число или число с плавающей точкой.")
                tkinter.messagebox.showerror('Ошибка','Вы должны были ввести целое число или число с плавающей точкой.')
            except:
                tkinter.messagebox.showerror('Error','Unknown error')
        elif lan == 4:
            try:
                state.insert(INSERT, "CPS-Eingabefehler\n")
                state.insert(INSERT, "Sie sollten eine Ganzzahl oder eine Gleitkommazahl eingegeben haben")
                tkinter.messagebox.showerror('Fehler','Sie sollten eine Ganzzahl oder eine Gleitkommazahl eingegeben haben.')
            except:
                tkinter.messagebox.showerror('Error','Unknown error')
        elif lan == 5:
            try:
                state.insert(INSERT, "CPS入力異常!\n")
                state.insert(INSERT, "整数または浮動小数点数を入力する必要があります")
                tkinter.messagebox.showerror('異常','整数または浮動小数点数を入力する必要があります')
            except:
                tkinter.messagebox.showerror('Error','Unknown error')
        else:
            try:
                state.insert(INSERT, "CPS输入错误\n")
                state.insert(INSERT, "您应该在‘CPS 设置’栏中输入一个实数")
                tkinter.messagebox.showerror('错误','你应该输入一个适宜的整数或浮点数。')
            except:
                tkinter.messagebox.showerror('Error','Unknown error')

            

def about():
    state.delete('0.0', END)
    if lan == 2:
        state.insert(INSERT, "MouseClicker Professional Plus\n")
        state.insert(INSERT, "Version: 6.5.1_Beta (Build 6410)\n")
        state.insert(INSERT, "2022/8/11 20:50(UTC+8) Update 39 \n")
        state.insert(INSERT, "Copyright © 2022 12sdj. All Rights Reserved. \n")
    elif lan == 3:
        state.insert(INSERT, "MouseClicker Professional Plus\n")
        state.insert(INSERT, "Версии: 6.5.1_Beta (Build 6410)\n")
        state.insert(INSERT, "2022/8/11 20:50(UTC+8) Update 39 \n")
        state.insert(INSERT, "Copyright © 2022 12sdj. All Rights Reserved. \n")
    elif lan == 4:
        state.insert(INSERT, "MouseClicker Professional Plus\n")
        state.insert(INSERT, "Versionen: 6.5.1_Beta (Build 6410)\n")
        state.insert(INSERT, "2022/8/11 20:50(UTC+8) Update 39 \n")
        state.insert(INSERT, "Copyright © 2022 12sdj. All Rights Reserved. \n")
    elif lan == 5:
        state.insert(INSERT, "MouseClicker Professional Plus\n")
        state.insert(INSERT, "バージョン: 6.5.1_Beta (Build 6410)\n")
        state.insert(INSERT, "2022/8/11 20:50(UTC+8) Update 39 \n")
        state.insert(INSERT, "Copyright © 2022 12sdj. All Rights Reserved. \n")
    else:
        state.insert(INSERT, "MouseClicker Professional Plus\n")
        state.insert(INSERT, "版本: 6.5.1_Beta (Build 6410)\n")
        state.insert(INSERT, "2022/8/11 20:50(UTC+8) Update 39 \n")
        state.insert(INSERT, "Copyright © 2022 12sdj. 保留一切权利. \n")


def update():
    state.delete('0.0', END)
    if lan == 2:
        state.insert(INSERT, "<Jump in ...>\n")
    elif lan == 3:
        state.insert(INSERT, "<Перейти на сайт ...>\n")
    elif lan == 4:
        state.insert(INSERT, "<Sprung in ...>\n")
    elif lan == 5:
        state.insert(INSERT, "<飛び込め...>\n")
    else:
        state.insert(INSERT, "<跳转中...>\n")
    try:
        webbrowser.open('https://github.com/12sdj/MouseClicker-by-12sdj/releases')
    except:
        if lan == 2:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
        elif lan == 3:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
        elif lan == 4:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
        elif lan == 5:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
        else:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            


def github():
    webbrowser.open('https://github.com/12sdj/MouseClicker-by-12sdj/issues')



def light():
    themeset_path = drive + "\\Users/" + user_name + "\AppData\Local\MouseClicker\ThemeSet.txt"
    try:
        with open(themeset_path,'r+') as d:
            d.read()
            d.seek(0)
            d.truncate()
            d.write('light')
        theme = 1
        if lan == 2:
            state.delete('0.0', END)
            state.insert(INSERT, "Theme has been switched to 'Light Mode' \n")
            state.insert(INSERT, "The program needs to be restarted to complete the change")
        elif lan == 3:
            state.delete('0.0', END)
            state.insert(INSERT, "тема была переключена на \"легкий режим\"\n")
            state.insert(INSERT, "Для завершения изменений необходимо перезапустить программу")
        elif lan == 4:
            state.delete('0.0', END)
            state.insert(INSERT, "das Thema wurde in den \"Lichtmodus\" versetzt \n")
            state.insert(INSERT, "Das Programm muss neu gestartet werden, um die Änderung abzuschließen")
        elif lan == 5:
            state.delete('0.0', END)
            state.insert(INSERT, "テーマが「ライトモード」に切り替わりました \n")
            state.insert(INSERT, "変更を完了するには、プログラムの再起動が必要です")  
        else:
            state.delete('0.0', END)
            state.insert(INSERT, "主题已切换至'浅色模式' \n")
            state.insert(INSERT, "程序需要重启以完成该更改")
    except:
        if lan == 2:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
        else:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            
    

def dark():
    themeset_path = drive + "\\Users/" + user_name + "\AppData\Local\MouseClicker\ThemeSet.txt"
    try:
        with open(themeset_path,'r+') as d:
            d.read()
            d.seek(0)
            d.truncate()
            d.write('dark')
        theme = 2
        if lan == 2:
            state.delete('0.0', END)
            state.insert(INSERT, "Theme has been switched to 'Dark Mode' \n")
            state.insert(INSERT, "The program needs to be restarted to complete the change")
        elif lan == 3:
            state.delete('0.0', END)
            state.insert(INSERT, "Тема была переключена на \"темный режим\" \n")
            state.insert(INSERT, "Для завершения изменений необходимо перезапустить программу")
        elif lan == 4:
            state.delete('0.0', END)
            state.insert(INSERT, "Das Thema wurde auf den \"dunklen Modus\" umgestellt\n")
            state.insert(INSERT, "Das Programm muss neu gestartet werden, um die Änderung abzuschließen")
        elif lan == 5:
            state.delete('0.0', END)
            state.insert(INSERT, "テーマが「ダークモード」に切り替わりました \n")
            state.insert(INSERT, "変更を完了するには、プログラムの再起動が必要です")
                    
        else:
            state.delete('0.0', END)
            state.insert(INSERT, "主题已切换至'深色模式' \n")
            state.insert(INSERT, "程序需要重启以完成该更改")
    except:
        if lan == 2:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
        elif lan == 3:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
        elif lan == 4:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
        elif lan == 5:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
        else:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            


    





def helpa():
        helpa = Toplevel()
        helpa.geometry("695x485")
        helpa.title("HELP")
        
        state = Text(helpa, relief="flat", font=("Microsoft YaHei UI", 10))
        state.place(relx=0.03, y=10, relwidth=0.95, height=460)
        if lan == 2:
            state.insert(INSERT, "What is CPS?\n")
            state.insert(INSERT, "  []CPS, is short for Click Per Second, means the number of clicks per second\n")
            state.insert(INSERT, "\n")
            state.insert(INSERT, "How to convert time interval to CPS?\n")
            state.insert(INSERT, "  []TIME INTERVAL = 1/CPS \n")
            state.insert(INSERT, "\n")
            state.insert(INSERT, "How does the program simulate CPS? \n")
            state.insert(INSERT, "  []The program realizes the button click by calling the Windows API, and then calculates the interval through the CPS calculation method.\n")
        elif lan == 3:
            state.insert(INSERT, "Что такое CPS?\n")
            state.insert(INSERT, "  []CPS, сокращение от Click Per Second, означает количество кликов в секунду.\n")
            state.insert(INSERT, "\n")
            state.insert(INSERT, "Как преобразовать временные интервалы и CPS?\n")
            state.insert(INSERT, "  []Временной интервал = 1/CPS \n")
            state.insert(INSERT, "\n")
            state.insert(INSERT, "Какими средствами программа будет имитировать CPS \n")
            state.insert(INSERT, "  []Программа реализует нажатие клавиш, вызывая Windows API, а затем вычисляет интервал с помощью метода расчета CPS\n")

        elif lan == 4:
            state.insert(INSERT, "Was ist CPS?\n")
            state.insert(INSERT, "  []CPS, kurz für Click Per Second, bedeutet Klicks pro Sekunde\n")
            state.insert(INSERT, "\n")
            state.insert(INSERT, "Zeitintervallumrechnung CPS?\n")
            state.insert(INSERT, "  []Zeitintervall = 1/CPS \n")
            state.insert(INSERT, "\n")
            state.insert(INSERT, "Wie setzt das Programm simulierte Klicks mit CPS um? \n")
            state.insert(INSERT, "  []Das Programm implementiert die Tastenanschläge, indem es die Windows-API aufruft, und berechnet dann das Intervall mit Hilfe der CPS-Berechnungsmethode\n")
        elif lan == 5:
            state.insert(INSERT, "CPSとは？\n")
            state.insert(INSERT, "  []CPSとは、Click Per Secondの略で、1秒あたりのクリック数を意味します\n")
            state.insert(INSERT, "\n")
            state.insert(INSERT, "時間間隔とCPSの変換方法を教えてください?\n")
            state.insert(INSERT, "  []時間間隔 = 1/CPS \n")
            state.insert(INSERT, "\n")
            state.insert(INSERT, "CPSのシミュレーションはどのように行うのですか？\n")
            state.insert(INSERT, "  []プログラムは、Windows APIを呼び出してボタンのクリックを実現し、CPS計算方式で間隔を計算する\n")
        else:
            state.insert(INSERT, "什么是CPS？\n")
            state.insert(INSERT, "  []CPS，是Click Per Second的简写，意思是每秒点击次数\n")
            state.insert(INSERT, "\n")
            state.insert(INSERT, "时间间隔和CPS怎么换算?\n")
            state.insert(INSERT, "  []时间间隔 = 1/CPS \n")
            state.insert(INSERT, "\n")
            state.insert(INSERT, "程序如何模拟CPS？\n")
            state.insert(INSERT, "  [] 程序通过调用Windows API实现按键点击，然后通过CPS计算方法计算出间隔\n")
        
    
        helpa.mainloop()






    
def logs():
    state.delete('0.0', END)
    state.insert(INSERT, "Update 39\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1.Fix bugs: Pressing ESC and then F8 during program execution causes threads to start and exit abnormally\n")
    state.insert(INSERT, " 2.The program configuration file will now be generated in the AppData folder and the program will be available as an installer or as a single file\n")
    state.insert(INSERT, " 3.Improve the interface in the 'Light Mode' theme\n")
    state.insert(INSERT, " 4.Fully adapted to Simplified Chinese(except for copyright information and changelog)\n")
    state.insert(INSERT, " 5.Japanese, Russian and German added and fully adapted (except for copyright information and changelog)\n")
    
    
    state.insert(INSERT, "Update 38\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1.Optimize the interface of the program, while clarifying the design direction and framework of the program\n")
    state.insert(INSERT, " 2.Expanded the compatible objects in compiler compatibility. Added support for Windows 7 (32-bit) SP1\n")
    state.insert(INSERT, " 3.The framework used for the upgrade process\n")
    state.insert(INSERT, " 4.New dark mode and support memory user configuration\n")
    state.insert(INSERT, " 5.Improved support for Simplified Chinese and support for remembering user configurations")

    
    state.insert(INSERT, "Update 30-37(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " [Optimization]\n")
    
    state.insert(INSERT, "Update 29\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1.Manual detection updates is added\n")

    state.insert(INSERT, "Update 28(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Add some buttons \n")
    
    state.insert(INSERT, "Update 27\n")
    state.insert(INSERT, "CHANGE: \n")
    
    state.insert(INSERT, "[Security]  \n")
    state.insert(INSERT, "Added the latest May 2022 dependency component patch to enhance software security  \n")
    state.insert(INSERT, "[Stability]  \n")
    state.insert(INSERT, "Using multi-threading technology, the program can be greatly improved to run stably. However, it will increase CPU power consumption  \n")
    state.insert(INSERT, "[Popularity]  \n")
    state.insert(INSERT, "Remove some unnecessary components. At the same time, add “? “to introduce component uses and to be more oriented towards game users  \n")
    state.insert(INSERT, "[Language universality]  \n")
    state.insert(INSERT, "Increase the Chinese Simplified  \n")
    state.insert(INSERT, "[Practicality]  \n")
    state.insert(INSERT, "Improved user interface. At the same time, the “Anti-Machine Cheat Detection” function was added (version 4.25)  \n")
    state.insert(INSERT, "[Quality Update]  \n")
    state.insert(INSERT, "Fixed bugs and introduced a bug-proofing mechanism to reduce the incidence of bugs  \n")

    state.insert(INSERT, "Update 17-26(Unpublished)\n")
    state.insert(INSERT, "CHANGE: \n")
    state.insert(INSERT, " 1. Improve user page \n")
    
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
    
def chinese():
    languageset_path = drive + "\\Users/" + user_name + "\AppData\Local\MouseClicker\LanguageSet.txt"
    try:
        with open(languageset_path,"r+") as d:
            d.read()
            d.seek(0)
            d.truncate()
            d.write('Chinese Simplified')
        lan = 1
        state.delete('0.0', END)
        state.insert(INSERT, "语言已切换至'简体中文（中国大陆）' \n")
        state.insert(INSERT, "程序需要重启以完成该更改")
    except:
        if lan == 2:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
        elif lan == 3:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
        elif lan == 4:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
        elif lan == 5:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
        else:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            

def english():
    languageset_path = drive + "\\Users/" + user_name + "\AppData\Local\MouseClicker\LanguageSet.txt"
    try:
        with open(languageset_path,"r+") as d:
            d.read()
            d.seek(0)
            d.truncate()
            d.write('American English')

        lan = 2
        state.delete('0.0', END)
        state.insert(INSERT, "Language switched to 'English(United States)' \n")
        state.insert(INSERT, "The program needs to be restarted to complete the change")

    except:
        if lan == 2:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
        elif lan == 3:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
        elif lan == 4:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
        elif lan == 5:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
        else:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            

def russian():
    languageset_path = drive + "\\Users/" + user_name + "\AppData\Local\MouseClicker\LanguageSet.txt"
    try:
        with open(languageset_path,"r+") as d:
            d.read()
            d.seek(0)
            d.truncate()
            d.write('Russian')
        lan = 3
        state.delete('0.0', END)
        state.insert(INSERT, "Язык переключен на 'Русский'' \n")

        state.insert(INSERT, "Для завершения изменений необходимо перезапустить программу")
    except:
        if lan == 2:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
        elif lan == 3:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
        elif lan == 4:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
        elif lan == 5:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
        else:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            

def german():
    languageset_path = drive + "\\Users/" + user_name + "\AppData\Local\MouseClicker\LanguageSet.txt"
    try:
        with open(languageset_path,"r+") as d:
            d.read()
            d.seek(0)
            d.truncate()
            d.write('German')
        lan = 4
        state.delete('0.0', END)
        state.insert(INSERT, "Die Sprache wurde auf 'Deutsch' umgestellt' \n")

        state.insert(INSERT, "Das Programm muss neu gestartet werden, um die Änderung abzuschließen.")
    except:
        if lan == 2:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
        elif lan == 3:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
        elif lan == 4:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
        elif lan == 5:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
        else:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            

def japanese():
    languageset_path = drive + "\\Users/" + user_name + "\AppData\Local\MouseClicker\LanguageSet.txt"
    try:
        with open(languageset_path,"r+") as d:
            d.read()
            d.seek(0)
            d.truncate()
            d.write('Japanese')
        lan = 5
        state.delete('0.0', END)
        state.insert(INSERT, "言語が「日本語」に切り替わりました \n")
        state.insert(INSERT, "変更を完了するには、プログラムの再起動が必要です")
    except:
        if lan == 2:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
        elif lan == 3:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
        elif lan == 4:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
        elif lan == 5:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
        else:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            

              
def more():
    themeset_path = drive + "\\Users/" + user_name + "\AppData\Local\MouseClicker\ThemeSet.txt"
    languageset_path = drive + "\\Users/" + user_name + "\AppData\Local\MouseClicker\LanguageSet.txt"
    def handler():
        window = Toplevel()
        window.geometry("895x685")
        if lan == 2:
            window.title("LICENSE")
        elif lan == 3:
            window.title("Соглашение")
        elif lan == 4:
            window.title("Vereinbarung")
        elif lan == 5:
            window.title("契約内容")
        else:
            window.title("协议")
        state = Text(window, relief="flat", font=("Microsoft YaHei UI", 10))
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
        
    
    def view():
        if tkinter.messagebox.askyesno('Ask', 'The following will open https://github.com/12sdj/MouseClicker-by-12sdj.git. Are you sure to execute?') == 1:
            try:
                webbrowser.open('https://github.com/12sdj/MouseClicker-by-12sdj.git')
            except:
                if lan == 2:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
                elif lan == 3:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
                elif lan == 4:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
                elif lan == 5:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
                else:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            

    def funk(*args):
    
        if (mode.get() == "Light Mode") or (mode.get() == "浅色模式"):
            try:
                with open(themeset_path,'r+') as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('light')
                theme = 1
                if lan == 2:
                    state.delete('0.0', END)
                    state.insert(INSERT, "Theme has been switched to 'Light Mode' \n")
                    state.insert(INSERT, "The program needs to be restarted to complete the change")
                elif lan == 3:
                    state.delete('0.0', END)
                    state.insert(INSERT, "тема была переключена на \"легкий режим\"\n")
                    state.insert(INSERT, "Для завершения изменений необходимо перезапустить программу")
                elif lan == 4:
                    state.delete('0.0', END)
                    state.insert(INSERT, "das Thema wurde in den \"Lichtmodus\" versetzt \n")
                    state.insert(INSERT, "Das Programm muss neu gestartet werden, um die Änderung abzuschließen")
                elif lan == 5:
                    state.delete('0.0', END)
                    state.insert(INSERT, "テーマが「淡色パターン」に切り替わりました \n")
                    state.insert(INSERT, "変更を完了するには、プログラムの再起動が必要です")  
                else:
                    state.delete('0.0', END)
                    state.insert(INSERT, "主题已切换至'浅色模式' \n")
                    state.insert(INSERT, "程序需要重启以完成该更改")
            except:
                if lan == 2:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
                else:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            
    

        else:
            try:
                with open(themeset_path,'r+') as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('dark')
                theme = 2
                if lan == 2:
                    state.delete('0.0', END)
                    state.insert(INSERT, "Theme has been switched to 'Dark Mode' \n")
                    state.insert(INSERT, "The program needs to be restarted to complete the change")
                elif lan == 3:
                    state.delete('0.0', END)
                    state.insert(INSERT, "Тема была переключена на \"темный режим\" \n")
                    state.insert(INSERT, "Для завершения изменений необходимо перезапустить программу")
                elif lan == 4:
                    state.delete('0.0', END)
                    state.insert(INSERT, "Das Thema wurde auf den \"dunklen Modus\" umgestellt\n")
                    state.insert(INSERT, "Das Programm muss neu gestartet werden, um die Änderung abzuschließen")
                elif lan == 5:
                    state.delete('0.0', END)
                    state.insert(INSERT, "テーマが「ダークモード」に切り替わりました \n")
                    state.insert(INSERT, "変更を完了するには、プログラムの再起動が必要です")
                            
                else:
                    state.delete('0.0', END)
                    state.insert(INSERT, "主题已切换至'深色模式' \n")
                    state.insert(INSERT, "程序需要重启以完成该更改")
            except:
                if lan == 2:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
                elif lan == 3:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
                elif lan == 4:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
                elif lan == 5:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
                else:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
                    

            
                
    def func(*args):
        global lan
        global cgtime
        cgtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if (mode2.get() == "简体中文（中国大陆）"):
            
            try:
                with open(languageset_path,"r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('Chinese Simplified')
                lan = 1
                state.delete('0.0', END)
                state.insert(INSERT, "语言已切换至'简体中文（中国大陆）' \n")
                state.insert(INSERT, "当前时间是：")
                state.insert(INSERT, cgtime)
                state.insert(INSERT, "\n程序需要重启以完成该更改")
            except:
                if lan == 2:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
                elif lan == 3:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
                elif lan == 4:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
                elif lan == 5:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
                else:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            

        elif (mode2.get() == "Русский"):
            
            try:
                with open(languageset_path,"r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('Russian')
                lan = 3
                state.delete('0.0', END)
                state.insert(INSERT, "Язык переключен на 'Русский'' \n")

                state.insert(INSERT, "Для завершения изменений необходимо перезапустить программу")
            except:
                if lan == 2:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
                elif lan == 3:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
                elif lan == 4:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
                elif lan == 5:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
                else:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            

        elif (mode2.get() == "Deutsch"):
            
            try:
                with open(languageset_path,"r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('German')
                lan = 4
                state.delete('0.0', END)
                state.insert(INSERT, "Die Sprache wurde auf 'Deutsch' umgestellt' \n")

                state.insert(INSERT, "Das Programm muss neu gestartet werden, um die Änderung abzuschließen.")
            except:
                if lan == 2:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
                elif lan == 3:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
                elif lan == 4:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
                elif lan == 5:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
                else:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            

        elif (mode2.get() == "日本語"):
            
            try:
                with open(languageset_path,"r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('Japanese')
                lan = 5
                state.delete('0.0', END)
                state.insert(INSERT, "言語が「日本語」に切り替わりました \n")
                state.insert(INSERT, "変更を完了するには、プログラムの再起動が必要です")
            except:
                if lan == 2:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
                elif lan == 3:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
                elif lan == 4:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
                elif lan == 5:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
                else:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            

        else:
            try:
                with open(languageset_path,"r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('American English')

                lan = 2
                state.delete('0.0', END)
                state.insert(INSERT, "Language switched to 'English(United States)' \n")
                state.insert(INSERT, "The time now is ")
                state.insert(INSERT, cgtime)
                state.insert(INSERT, "\nThe program needs to be restarted to complete the change")

            except:
                if lan == 2:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
                elif lan == 3:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
                elif lan == 4:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
                elif lan == 5:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
                else:
                    tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            

    def close():
        otherFrame.destroy()
    #-------------------------------- 
    otherFrame = Toplevel()
    otherFrame.geometry("540x300")
    if lan == 2:
        otherFrame.title("MouseClicker Professional Plus - More")
    elif lan == 3:
        otherFrame.title("MouseClicker Professional Plus - Подробнее")
    elif lan == 4:
        otherFrame.title("MouseClicker Professional Plus - Mehr")
    elif lan == 5:
        otherFrame.title("MouseClicker Professional Plus - もっと見る")
    else:
        otherFrame.title("MouseClicker Professional Plus - 更多")
    
    mode = StringVar()
    cmb = ttk.Combobox(otherFrame,textvariable=mode, state='readonly',width = 20)
    cmb.pack()
    # 设置下拉菜单中的值
    if lan == 2:
        cmb['value'] = ('Light Mode','Dark Mode')
    elif lan == 3:
        cmb['value'] = ('Световой режим','Темный режим')
    elif lan == 4:
        cmb['value'] = ('Helles Farbmuster','Dunkler Modus')
    elif lan == 5:
        cmb['value'] = ('淡色パターン','ダークモード')
    else:
        cmb['value'] = ('浅色模式','深色模式')
    # 设置默认值，即默认下拉框中的内容
    if theme == 1:
        cmb.current(0)
        
    if theme == 2:
        cmb.current(1)
        otherFrame.configure(bg='black')



        
    cmb.bind("<<ComboboxSelected>>",funk)
#-------------------------------------------------------------------------------------
    mode2 = StringVar()
    cmd = ttk.Combobox(otherFrame,textvariable=mode2, state='readonly',width = 20)
    cmd.pack()
    # 设置下拉菜单中的值
    cmd['value'] = ('简体中文（中国大陆）','English(United States)','Русский','Deutsch','日本語')
    # 设置默认值，即默认下拉框中的内容
    if lan == 1:
        cmd.current(0)
    if lan == 2:
        cmd.current(1)
    if lan == 3:
        cmd.current(2)
    if lan == 4:
        cmd.current(3)
    if lan == 5:
        cmd.current(4)
    cmd.bind("<<ComboboxSelected>>",func)

    if lan == 2:
        btn = Button(otherFrame, text="LICENSE",font=('Arial', 14), command=handler)
        btn.pack()
        btn2 = Button(otherFrame, text="View the source code", font=('Arial', 14), command=view)
        btn2.pack()
    elif lan == 3:
        btn = Button(otherFrame, text="Протоколы",font=('Arial', 14), command=handler)
        btn.pack()
        btn2 = Button(otherFrame, text="Просмотр исходного кода", font=('Arial', 14), command=view)
        btn2.pack()
    elif lan == 4:
        btn = Button(otherFrame, text="Protokolle",font=('Arial', 14), command=handler)
        btn.pack()
        btn2 = Button(otherFrame, text="Quellcode anzeigen", font=('Arial', 14), command=view)
        btn2.pack()
    elif lan == 5:
        btn = Button(otherFrame, text="契約内容",font=('Arial', 14), command=handler)
        btn.pack()
        btn2 = Button(otherFrame, text="ソースコードを見る", font=('Arial', 14), command=view)
        btn2.pack()
    else:
        btn = Button(otherFrame, text="协议",font=('Arial', 14), command=handler)
        btn.pack()
        btn2 = Button(otherFrame, text="查看源代码", font=('Arial', 14), command=view)
        btn2.pack()

    
    Label = Button(otherFrame,text='CLOSE',bg='orange',fg='white',command=close)
    Label.pack(side=BOTTOM)




    otherFrame.overrideredirect(True)
    otherFrame.mainloop()

    
# -------------------------------- GUI界面 --------------------------------
root=ThemedTk(theme="adapta", toplevel=False, themebg=False)
# 高dpi
winWidth = 850
winHeight = 330

ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/75)
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)


root.title('MouseClicker Professional Plus')
#root.geometry('850x330')
root.resizable(0,0)
root.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
mouse = IntVar()
cheat = IntVar()
#------------------------------------------------------------------------------------------------------------------------------------------------------

def create_shortcut(bin_path: str, name: str, desc: str):

	#:param bin_path: exe路径
	#:param name: 需要创建快捷方式的路径
	#:param desc: 描述，鼠标放在图标上面会有提示
	#:return:


	shortcut =  name + ".lnk"
	winshell.CreateShortcut(
		Path=shortcut,
		Target=bin_path,
		Icon=(bin_path, 0),
		Description=desc)

 
def get_desktop():
	key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
	                     r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
	return winreg.QueryValueEx(key, "Desktop")[0]
 

	
start_path = drive + "\\Users/" + user_name + "\AppData\Local\MouseClicker\Start.txt"
try:
    with open(start_path,"r+") as f:
        lines = f.read() ##Assume the sample file has 3 lines
        first = lines.split('\n', 1)[0]
        str(first)
    #win32api.SetFileAttributes('Start.txt', win32con.FILE_ATTRIBUTE_HIDDEN)
    try:
        
        if first == "yes":
            start = 1
        elif first == "no":
            start = 2
        else:

            tkinter.messagebox.showerror('MouseClicker Update Assitant','Please do not change the configuration file: Start.txt')
   
            

            try:
                with open(start_path,"r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('no')
                start = 2
            except:
                start = 0
    except:

        tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
    
            

except:
    try:
        folder_path = drive + "\\Users/" + user_name + "\AppData\Local"
        os.mkdir(folder_path + './MouseClicker')
    except:
        tkinter.messagebox.showerror('MouseClicker Update Assitant','Do not delete the file: "Start.txt"')
    try:

        with open(start_path,"w+") as f:
            f.write('no')
        #win32api.SetFileAttributes('Start.txt', win32con.FILE_ATTRIBUTE_HIDDEN)
        with open(start_path,"r+") as f:
            lines = f.read() ##Assume the sample file has 3 lines
            first = lines.split('\n', 1)[0]
        try:
            start = 2
        except:
   
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
      
            

    except:
  
        tkinter.messagebox.showerror('MouseClicker Update Assitant','You should allow this program can create a shorcut in your desktop. If necessary, turn off the anti-virus software on your computer!')
      



if start == 2:
    
    
    bin_path = r"MouseClicker.exe"
    link_path = deskTopDir + "\\MouseClicker"
    desc = "MouseClicker by 12sdj"
    create_shortcut(bin_path, link_path, desc)
    
    with open(start_path,"r+") as d:
        d.read()
        d.seek(0)
        d.truncate()
        d.write('yes')
    start = 1
#-----------------------------------------------------------------------------------------------------------------------------------------------------

            

        #-----------------------------------------------------------------------------------------------------------------------------------------------------
global lan
languageset_path = drive + "\\Users/" + user_name + "\AppData\Local\MouseClicker\LanguageSet.txt"
try:
    with open(languageset_path,"r+") as f:
        lines = f.read() ##Assume the sample file has 3 lines
        first = lines.split('\n', 1)[0]
        str(first)
        #print(first)#test code
    #win32api.SetFileAttributes('LanguageSet.txt', win32con.FILE_ATTRIBUTE_HIDDEN)
    try:
        
        if first == "Chinese Simplified":
            lan = 1
        elif first == "American English":
            lan = 2
        elif first == "Russian":
            lan = 3
        elif first == "German":
            lan = 4
        elif first == "Japanese":
            lan = 5
            
        else:

            tkinter.messagebox.showerror('MouseClicker Update Assitant','Please do not change the configuration file: LanguageSet.txt')

            

            try:
                with open(languageset_path,"r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('American English')
                lan = 2
            except:
                lan = 0
    except:
  
        tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')

            

except:
    try:

        with open(languageset_path,"w+") as f:
            f.write('American English')
        #win32api.SetFileAttributes('LanguageSet.txt', win32con.FILE_ATTRIBUTE_HIDDEN)
        with open(languageset_path,"r+") as f:
            lines = f.read() ##Assume the sample file has 3 lines
            first = lines.split('\n', 1)[0]
        try:
            lan = 2
        except:
  
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
            
            

    except:

        tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
 
            
global theme
themeset_path = drive + "\\Users/" + user_name + "\AppData\Local\MouseClicker\ThemeSet.txt"
try:
    with open(themeset_path,'r+') as f:
        lines = f.read() ##Assume the sample file has 3 lines
        first = lines.split('\n', 1)[0]
        str(first)
    #win32api.SetFileAttributes('ThemeSet.txt', win32con.FILE_ATTRIBUTE_HIDDEN)#隐藏
    try:
        
        if first == "light":
            theme = 1
        elif first == "dark":
            theme = 2
        else:
            if lan == 2:
                tkinter.messagebox.showerror('MouseClicker Update Assitant','Please do not change the configuration file: ThemeSet.txt')
            elif lan == 3:
                tkinter.messagebox.showerror('MouseClicker Update Assitant','Пожалуйста, не изменяйте файл конфигурации:ThemeSet.txt')
            elif lan == 4:
                tkinter.messagebox.showerror('MouseClicker Update Assitant','Bitte verändern Sie nicht die Konfigurationsdatei:ThemeSet.txt')
            elif lan == 5:
                tkinter.messagebox.showerror('MouseClicker Update Assitant','設定ファイル :ThemeSet.txt を変更しないでください。')
            else:
                tkinter.messagebox.showerror('MouseClicker Update Assitant','请不要随意更改配置文件: ThemeSet.txt')
            

            try:
                with open(themeset_path, "r+") as d:
                    d.read()
                    d.seek(0)
                    d.truncate()
                    d.write('light')
                theme = 1
            except:
                theme = 0
    except:
        if lan == 2:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
        elif lan == 3:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
        elif lan == 4:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
        elif lan == 5:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
        else:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            

except:
    try:

        with open(themeset_path,'w+') as f:
            f.write('light')
        #win32api.SetFileAttributes('ThemeSet.txt', win32con.FILE_ATTRIBUTE_HIDDEN)
        with open(themeset_path,'r+') as f:
            lines = f.read() ##Assume the sample file has 3 lines
            first = lines.split('\n', 1)[0]
        try:
            theme = 1
        except:
            if lan == 2:
                tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
            elif lan == 3:
                tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
            elif lan == 4:
                tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
            elif lan == 5:
                tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
            else:
                tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')
            

    except:
        if lan == 2:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Known Error! Please go to our "Github - Issue" to feedback the issue')
        elif lan == 3:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Неизвестная ошибка! Пожалуйста, перейдите в наш раздел "Github - Issue" для обратной связи по этому вопросу')
        elif lan == 4:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','Unbekannter Fehler! Bitte gehen Sie zu unserem "Github - Issue" Bereich, um Feedback zu diesem Problem zu geben')
        elif lan == 5:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','不明なエラー! この問題に関するフィードバックは、Github - Issueセクションで行ってください。')
        else:
            tkinter.messagebox.showerror('MouseClicker Update Assitant','未知错误！请前往我们的"Github - Issue"一栏中反馈该问题')

#------------------------------------------------------------------------
if theme == 1:
    if lan == 2:
        lab1 = Label(root, text='Mouse Button', font=("Microsoft YaHei UI", 11),bg='#FFFAFA')
        lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)
        r1 = Radiobutton(root,
                         text='LEFT',
                         font=("Microsoft YaHei UI", 10),
                         bg='#FFFAFA',
                         value=0,
                         variable=mouse)
        r1.place(relx=0.05, y=40, relwidth=0.1, height=30)
        r2 = Radiobutton(root,
                         text='RIGHT',
                         font=("Microsoft YaHei UI", 10),
                     bg='#FFFAFA',
                         value=1,
                         variable=mouse)
        r2.place(relx=0.18, y=40, relwidth=0.1, height=30)
        r3 = Radiobutton(root,
                         text='MIDDLE',
                         font=("Microsoft YaHei UI", 10),
                        bg='#FFFAFA',
                         value=2,
                         variable=mouse)
        r3.place(relx=0.31, y=40, relwidth=0.12, height=30)
        lab2 = Label(root, text='CPS Setting', font=("Microsoft YaHei UI", 11),bg='#FFFAFA')
        lab2.place(relx=0.5, y=10, relwidth=0.45, height=30)
        label3 = Label(root,
                   text='---------- Current State and Instruction ----------',
                   font=("Microsoft YaHei UI", 8),bg='#FFFAFA')
        label3.place(relx=0.5, y=90, relwidth=0.45, height=20)
        
        b2 = Button(root, text='ABOUT', font=('Arial', 10),bg='white',command=about)
        b2.place(relx=0.07, y=220, relwidth=0.16, height=30)

        b3 = Button(root, text='CHANGELOG', font=('Arial', 10),bg='white',command=logs)
        b3.place(relx=0.23, y=220, relwidth=0.20, height=30)
        b4 = Button(root, text='MORE', font=('Arial', 10),bg='white',command=more)
        b4.place(relx=0.07, y=280, relwidth=0.36, height=30)
        b5 = Button(root, text='CHECK FOR UPDATES', font=('Arial', 10),bg='white',command=update)
        b5.place(relx=0.07, y=250, relwidth=0.36, height=30)

        lag = Label(root, text='Anti-Machine Cheat Detection', font=("Microsoft YaHei UI", 11),bg='#FFFAFA')
        lag.place(relx=0.05, y=100, relwidth=0.4, height=30)

        xon = Radiobutton(root,
                         text='ON',
                         font=("Microsoft YaHei UI", 10),
                        bg='#FFFAFA',
                         value=3,
                         variable=cheat)
        xon.place(relx=0.07, y=140, relwidth=0.15, height=30)
        xr = Radiobutton(root,
                         text='OFF',
                         font=("Microsoft YaHei UI", 10),
                           bg='#FFFAFA',
                         value=4,
                         variable=cheat)
        xr.place(relx=0.25, y=140, relwidth=0.15, height=30)
        xr.select()
        h1 = Button(root, text='?', font=('Arial', 10),command=helpa)
        h1.place(relx=0.8, y=10, relwidth=0.04, height=30)

        input = Entry(root, relief="flat", font=("Microsoft YaHei UI", 10),fg="#20B2AA")
        input.place(relx=0.575, y=40, relwidth=0.3, height=30)


        state = Text(root, relief="flat", font=("Microsoft YaHei UI", 10))
        state.place(relx=0.5, y=110, relwidth=0.45, height=150)
    elif lan == 3:
        lab1 = Label(root, text='Кнопки мыши', font=("Microsoft YaHei UI", 11),bg='#FFFAFA')
        lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)
        r1 = Radiobutton(root,
                         text='Слева',
                         font=("Microsoft YaHei UI", 10),
                         bg='#FFFAFA',
                         value=0,
                         variable=mouse)
        r1.place(relx=0.05, y=40, relwidth=0.1, height=30)
        r2 = Radiobutton(root,
                         text='Справа',
                         font=("Microsoft YaHei UI", 10),
                     bg='#FFFAFA',
                         value=1,
                         variable=mouse)
        r2.place(relx=0.18, y=40, relwidth=0.1, height=30)
        r3 = Radiobutton(root,
                         text='Средний',
                         font=("Microsoft YaHei UI", 10),
                        bg='#FFFAFA',
                         value=2,
                         variable=mouse)
        r3.place(relx=0.31, y=40, relwidth=0.12, height=30)
        lab2 = Label(root, text='Настройки CPS', font=("Microsoft YaHei UI", 11),bg='#FFFAFA')
        lab2.place(relx=0.5, y=10, relwidth=0.45, height=30)
        label3 = Label(root,
                   text='---------- Советы и состояние программы ----------',
                   font=("Microsoft YaHei UI", 8),bg='#FFFAFA')
        label3.place(relx=0.5, y=90, relwidth=0.45, height=20)
        
        b2 = Button(root, text='О сайте', font=('Arial', 10),bg='white',command=about)
        b2.place(relx=0.07, y=220, relwidth=0.16, height=30)

        b3 = Button(root, text='Журнал обновления', font=('Arial', 10),bg='white',command=logs)
        b3.place(relx=0.23, y=220, relwidth=0.20, height=30)
        b4 = Button(root, text='Подробнее', font=('Arial', 10),bg='white',command=more)
        b4.place(relx=0.07, y=280, relwidth=0.36, height=30)
        b5 = Button(root, text='Проверьте наличие обновлений', font=('Arial', 10),bg='white',command=update)
        b5.place(relx=0.07, y=250, relwidth=0.36, height=30)

        lag = Label(root, text='Обнаружение античитов', font=("Microsoft YaHei UI", 11),bg='#FFFAFA')
        lag.place(relx=0.05, y=100, relwidth=0.4, height=30)

        xon = Radiobutton(root,
                         text='Открыть',
                         font=("Microsoft YaHei UI", 10),
                        bg='#FFFAFA',
                         value=3,
                         variable=cheat)
        xon.place(relx=0.07, y=140, relwidth=0.15, height=30)
        xr = Radiobutton(root,
                         text='Закрыть',
                         font=("Microsoft YaHei UI", 10),
                           bg='#FFFAFA',
                         value=4,
                         variable=cheat)
        xr.place(relx=0.25, y=140, relwidth=0.15, height=30)
        xr.select()
        h1 = Button(root, text='?', font=('Arial', 10),command=helpa)
        h1.place(relx=0.82, y=10, relwidth=0.04, height=30)

        input = Entry(root, relief="flat", font=("Microsoft YaHei UI", 10),fg="#20B2AA")
        input.place(relx=0.575, y=40, relwidth=0.3, height=30)


        state = Text(root, relief="flat", font=("Microsoft YaHei UI", 10))
        state.place(relx=0.5, y=110, relwidth=0.45, height=150)
    elif lan == 4:
        lab1 = Label(root, text='Maustaste', font=("Microsoft YaHei UI", 11),bg='#FFFAFA')
        lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)
        r1 = Radiobutton(root,
                         text='Links',
                         font=("Microsoft YaHei UI", 10),
                         bg='#FFFAFA',
                         value=0,
                         variable=mouse)
        r1.place(relx=0.05, y=40, relwidth=0.1, height=30)
        r2 = Radiobutton(root,
                         text='Rechts',
                         font=("Microsoft YaHei UI", 10),
                     bg='#FFFAFA',
                         value=1,
                         variable=mouse)
        r2.place(relx=0.18, y=40, relwidth=0.1, height=30)
        r3 = Radiobutton(root,
                         text='Mitte',
                         font=("Microsoft YaHei UI", 10),
                        bg='#FFFAFA',
                         value=2,
                         variable=mouse)
        r3.place(relx=0.31, y=40, relwidth=0.12, height=30)
        lab2 = Label(root, text='CPS-Einstellungen', font=("Microsoft YaHei UI", 11),bg='#FFFAFA')
        lab2.place(relx=0.5, y=10, relwidth=0.45, height=30)
        label3 = Label(root,
                   text='---------- Tipps und Programmstatus ----------',
                   font=("Microsoft YaHei UI", 8),bg='#FFFAFA')
        label3.place(relx=0.5, y=90, relwidth=0.45, height=20)
        
        b2 = Button(root, text='Über', font=('Arial', 10),bg='white',command=about)
        b2.place(relx=0.07, y=220, relwidth=0.16, height=30)

        b3 = Button(root, text='Änderungsprotokoll', font=('Arial', 10),bg='white',command=logs)
        b3.place(relx=0.23, y=220, relwidth=0.20, height=30)
        b4 = Button(root, text='Protokoll aktualisieren', font=('Arial', 10),bg='white',command=more)
        b4.place(relx=0.07, y=280, relwidth=0.36, height=30)
        b5 = Button(root, text='Nach Aktualisierungen suchen', font=('Arial', 10),bg='white',command=update)
        b5.place(relx=0.07, y=250, relwidth=0.36, height=30)

        lag = Label(root, text='Anti-Maschinen-Betrugserkennung', font=("Microsoft YaHei UI", 11),bg='#FFFAFA')
        lag.place(relx=0.05, y=100, relwidth=0.4, height=30)

        xon = Radiobutton(root,
                         text='Öffnen Sie',
                         font=("Microsoft YaHei UI", 10),
                        bg='#FFFAFA',
                         value=3,
                         variable=cheat)
        xon.place(relx=0.07, y=140, relwidth=0.15, height=30)
        xr = Radiobutton(root,
                         text='Schließen Sie',
                         font=("Microsoft YaHei UI", 10),
                           bg='#FFFAFA',
                         value=4,
                         variable=cheat)
        xr.place(relx=0.25, y=140, relwidth=0.16, height=30)
        xr.select()
        h1 = Button(root, text='?', font=('Arial', 10),command=helpa)
        h1.place(relx=0.82, y=10, relwidth=0.04, height=30)

        input = Entry(root, relief="flat", font=("Microsoft YaHei UI", 10),fg="#20B2AA")
        input.place(relx=0.575, y=40, relwidth=0.3, height=30)


        state = Text(root, relief="flat", font=("Microsoft YaHei UI", 10))
        state.place(relx=0.5, y=110, relwidth=0.45, height=150)
    elif lan == 5:
        lab1 = Label(root, text='オブジェクトをクリックする', font=("Microsoft YaHei UI", 11),bg='#FFFAFA')
        lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)
        r1 = Radiobutton(root,
                         text='左クリック',
                         font=("Microsoft YaHei UI", 10),
                         bg='#FFFAFA',
                         value=0,
                         variable=mouse)
        r1.place(relx=0.05, y=40, relwidth=0.12, height=30)
        r2 = Radiobutton(root,
                         text='右クリック',
                         font=("Microsoft YaHei UI", 10),
                     bg='#FFFAFA',
                         value=1,
                         variable=mouse)
        r2.place(relx=0.18, y=40, relwidth=0.12, height=30)
        r3 = Radiobutton(root,
                         text='ミドルキーズ',
                         font=("Microsoft YaHei UI", 10),
                        bg='#FFFAFA',
                         value=2,
                         variable=mouse)
        r3.place(relx=0.32, y=40, relwidth=0.14, height=30)
        lab2 = Label(root, text='CPSの設定', font=("Microsoft YaHei UI", 11),bg='#FFFAFA')
        lab2.place(relx=0.5, y=10, relwidth=0.45, height=30)
        label3 = Label(root,
                   text='---------- プログラムメッセージ ----------',
                   font=("Microsoft YaHei UI", 8),bg='#FFFAFA')
        label3.place(relx=0.5, y=90, relwidth=0.45, height=20)
        
        b2 = Button(root, text='について', font=('Arial', 10),bg='white',command=about)
        b2.place(relx=0.07, y=220, relwidth=0.16, height=30)

        b3 = Button(root, text='更新履歴', font=('Arial', 10),bg='white',command=logs)
        b3.place(relx=0.23, y=220, relwidth=0.20, height=30)
        b4 = Button(root, text='アップデートを確認する', font=('Arial', 10),bg='white',command=more)
        b4.place(relx=0.07, y=280, relwidth=0.36, height=30)
        b5 = Button(root, text='その他のオプション', font=('Arial', 10),bg='white',command=update)
        b5.place(relx=0.07, y=250, relwidth=0.36, height=30)

        lag = Label(root, text='機械的な不正に対する検知の防御。', font=("Microsoft YaHei UI", 11),bg='#FFFAFA')
        lag.place(relx=0.05, y=100, relwidth=0.4, height=30)

        xon = Radiobutton(root,
                         text='オープン',
                         font=("Microsoft YaHei UI", 10),
                        bg='#FFFAFA',
                         value=3,
                         variable=cheat)
        xon.place(relx=0.07, y=140, relwidth=0.15, height=30)
        xr = Radiobutton(root,
                         text='閉じる',
                         font=("Microsoft YaHei UI", 10),
                           bg='#FFFAFA',
                         value=4,
                         variable=cheat)
        xr.place(relx=0.25, y=140, relwidth=0.16, height=30)
        xr.select()
        h1 = Button(root, text='?', font=('Arial', 10),command=helpa)
        h1.place(relx=0.82, y=10, relwidth=0.04, height=30)

        input = Entry(root, relief="flat", font=("Microsoft YaHei UI", 10),fg="#20B2AA")
        input.place(relx=0.575, y=40, relwidth=0.3, height=30)


        state = Text(root, relief="flat", font=("Microsoft YaHei UI", 10))
        state.place(relx=0.5, y=110, relwidth=0.45, height=150)
    else:
        lab1 = Label(root, text='鼠标点击按钮设置', font=("Microsoft YaHei UI", 11),bg='#FFFAFA')
        lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)
        r1 = Radiobutton(root,
                         text='左键',
                         font=("Microsoft YaHei UI", 10),
                         bg='#FFFAFA',
                         value=0,
                         variable=mouse)
        r1.place(relx=0.05, y=40, relwidth=0.1, height=30)
        r2 = Radiobutton(root,
                         text='右键',
                         font=("Microsoft YaHei UI", 10),
                     bg='#FFFAFA',
                         value=1,
                         variable=mouse)
        r2.place(relx=0.18, y=40, relwidth=0.1, height=30)
        r3 = Radiobutton(root,
                         text='中键',
                         font=("Microsoft YaHei UI", 10),
                        bg='#FFFAFA',
                         value=2,
                         variable=mouse)
        r3.place(relx=0.31, y=40, relwidth=0.12, height=30)
        lab2 = Label(root, text='CPS 设置', font=("Microsoft YaHei UI", 11),bg='#FFFAFA')
        lab2.place(relx=0.5, y=10, relwidth=0.45, height=30)
        label3 = Label(root,
                   text='---------- 通知中心 ----------',
                   font=("Microsoft YaHei UI", 8),bg='#FFFAFA')
        label3.place(relx=0.5, y=90, relwidth=0.45, height=20)
        
        b2 = Button(root, text='关于', font=('Arial', 10),bg='white',command=about)
        b2.place(relx=0.07, y=220, relwidth=0.16, height=30)

        b3 = Button(root, text='更新日志', font=('Arial', 10),bg='white',command=logs)
        b3.place(relx=0.23, y=220, relwidth=0.20, height=30)
        b4 = Button(root, text='更多', font=('Arial', 10),bg='white',command=more)
        b4.place(relx=0.07, y=280, relwidth=0.36, height=30)
        b5 = Button(root, text='检查更新（手动）', font=('Arial', 10),bg='white',command=update)
        b5.place(relx=0.07, y=250, relwidth=0.36, height=30)

        lag = Label(root, text='反机器诈术侦测', font=("Microsoft YaHei UI", 11),bg='#FFFAFA')
        lag.place(relx=0.05, y=100, relwidth=0.4, height=30)

        xon = Radiobutton(root,
                         text='开启',
                         font=("Microsoft YaHei UI", 10),
                        bg='#FFFAFA',
                         value=3,
                         variable=cheat)
        xon.place(relx=0.07, y=140, relwidth=0.15, height=30)
        xr = Radiobutton(root,
                         text='关闭',
                         font=("Microsoft YaHei UI", 10),
                           bg='#FFFAFA',
                         value=4,
                         variable=cheat)
        xr.place(relx=0.25, y=140, relwidth=0.15, height=30)
        xr.select()
        h1 = Button(root, text='?', font=('Arial', 10),command=helpa)
        h1.place(relx=0.8, y=10, relwidth=0.04, height=30)

        input = Entry(root, relief="flat", font=("Microsoft YaHei UI", 10),fg="#20B2AA")
        input.place(relx=0.575, y=40, relwidth=0.3, height=30)


        state = Text(root, relief="flat", font=("Microsoft YaHei UI", 10))
        state.place(relx=0.5, y=110, relwidth=0.45, height=150)        
if theme == 2:
    if lan == 2:
        lab1 = Label(root, text='Mouse Button', font=("Microsoft YaHei UI", 11), fg="gray",bg='black')
        lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)
        r1 = Radiobutton(root,
                         text='LEFT',
                         font=("Microsoft YaHei UI", 10),
                         fg='white',
                         bg='black',
                         value=0,
                         variable=mouse)
        r1.place(relx=0.05, y=40, relwidth=0.1, height=30)
        r2 = Radiobutton(root,
                         text='RIGHT',
                         font=("Microsoft YaHei UI", 10),
                         fg='white',
                         bg='black',
                         value=1,
                         variable=mouse)
        r2.place(relx=0.18, y=40, relwidth=0.1, height=30)
        r3 = Radiobutton(root,
                         text='MIDDLE',
                         font=("Microsoft YaHei UI", 10),
                         fg='white',
                         bg='black',
                         value=2,
                         variable=mouse)
        r3.place(relx=0.31, y=40, relwidth=0.12, height=30)

        lab2 = Label(root, text='CPS Setting', font=("Microsoft YaHei UI", 11), fg="gray",bg='black')
        lab2.place(relx=0.5, y=10, relwidth=0.45, height=30)
        label3 = Label(root,
                   text='---------- Current State and Instruction ----------',
                   font=("Microsoft YaHei UI", 8),
                   fg="gray",bg="black")
        label3.place(relx=0.5, y=90, relwidth=0.45, height=20)
       
        
        b2 = Button(root, text='ABOUT', font=('Arial', 10), fg="grey",bg='black',command=about)
        b2.place(relx=0.07, y=220, relwidth=0.16, height=30)

        b3 = Button(root, text='CHANGELOG', font=('Arial', 10), fg="grey",bg='black',command=logs)
        b3.place(relx=0.23, y=220, relwidth=0.20, height=30)
        b4 = Button(root, text='MORE', font=('Arial', 10), fg="grey",bg='black',command=more)
        b4.place(relx=0.07, y=280, relwidth=0.36, height=30)
        b5 = Button(root, text='CHECK FOR UPDATES', font=('Arial', 10), fg="grey",bg='black',command=update)
        b5.place(relx=0.07, y=250, relwidth=0.36, height=30)

        lag = Label(root, text='Anti-Machine Cheat Detection', font=("Microsoft YaHei UI", 11),  fg="gray",bg="black")
        lag.place(relx=0.05, y=100, relwidth=0.4, height=30)

        xon = Radiobutton(root,
                         text='ON',
                         font=("Microsoft YaHei UI", 10),
                         fg="white",
                         bg='black',
                         value=3,
                         variable=cheat)
        xon.place(relx=0.07, y=140, relwidth=0.15, height=30)
        xr = Radiobutton(root,
                         text='OFF',
                         font=("Microsoft YaHei UI", 10),
                         fg="white",
                         bg='black',
                         value=4,
                         variable=cheat)
        xr.place(relx=0.25, y=140, relwidth=0.15, height=30)
        xr.select()
        h1 = Button(root, text='?', font=('Arial', 10),fg='green',bg='black',command=helpa)
        h1.place(relx=0.8, y=10, relwidth=0.04, height=30)

        input = Entry(root, relief="flat", font=("Microsoft YaHei UI", 10),bg='gray')
        input.place(relx=0.575, y=40, relwidth=0.3, height=30)


        state = Text(root, relief="flat", font=("Microsoft YaHei UI", 10),bg='gray')
        state.place(relx=0.5, y=110, relwidth=0.45, height=150)
    elif lan == 3:
        lab1 = Label(root, text='Кнопки мыши', font=("Microsoft YaHei UI", 11), fg="gray",bg='black')
        lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)
        r1 = Radiobutton(root,
                         text='Слева',
                         font=("Microsoft YaHei UI", 10),
                         fg='white',
                         bg='black',
                         value=0,
                         variable=mouse)
        r1.place(relx=0.05, y=40, relwidth=0.1, height=30)
        r2 = Radiobutton(root,
                         text='Справа',
                         font=("Microsoft YaHei UI", 10),
                         fg='white',
                         bg='black',
                         value=1,
                         variable=mouse)
        r2.place(relx=0.18, y=40, relwidth=0.1, height=30)
        r3 = Radiobutton(root,
                         text='Средний',
                         font=("Microsoft YaHei UI", 10),
                         fg='white',
                         bg='black',
                         value=2,
                         variable=mouse)
        r3.place(relx=0.31, y=40, relwidth=0.12, height=30)

        lab2 = Label(root, text='Настройки CPS', font=("Microsoft YaHei UI", 11), fg="gray",bg='black')
        lab2.place(relx=0.5, y=10, relwidth=0.45, height=30)
        label3 = Label(root,
                   text='---------- Советы и состояние программы ----------',
                   font=("Microsoft YaHei UI", 8),
                   fg="gray",bg="black")
        label3.place(relx=0.5, y=90, relwidth=0.45, height=20)
       
        
        b2 = Button(root, text='О сайте', font=('Arial', 10), fg="grey",bg='black',command=about)
        b2.place(relx=0.07, y=220, relwidth=0.16, height=30)

        b3 = Button(root, text='Журнал обновления', font=('Arial', 10), fg="grey",bg='black',command=logs)
        b3.place(relx=0.23, y=220, relwidth=0.20, height=30)
        b4 = Button(root, text='Подробнее', font=('Arial', 10), fg="grey",bg='black',command=more)
        b4.place(relx=0.07, y=280, relwidth=0.36, height=30)
        b5 = Button(root, text='Проверьте наличие обновлений', font=('Arial', 10), fg="grey",bg='black',command=update)
        b5.place(relx=0.07, y=250, relwidth=0.36, height=30)

        lag = Label(root, text='Обнаружение античитов', font=("Microsoft YaHei UI", 11),  fg="gray",bg="black")
        lag.place(relx=0.05, y=100, relwidth=0.4, height=30)

        xon = Radiobutton(root,
                         text='Открыть',
                         font=("Microsoft YaHei UI", 10),
                         fg="white",
                         bg='black',
                         value=3,
                         variable=cheat)
        xon.place(relx=0.07, y=140, relwidth=0.15, height=30)
        xr = Radiobutton(root,
                         text='Закрыть',
                         font=("Microsoft YaHei UI", 10),
                         fg="white",
                         bg='black',
                         value=4,
                         variable=cheat)
        xr.place(relx=0.25, y=140, relwidth=0.15, height=30)
        xr.select()
        h1 = Button(root, text='?', font=('Arial', 10),fg='green',bg='black',command=helpa)
        h1.place(relx=0.82, y=10, relwidth=0.04, height=30)

        input = Entry(root, relief="flat", font=("Microsoft YaHei UI", 10),bg='gray')
        input.place(relx=0.575, y=40, relwidth=0.3, height=30)


        state = Text(root, relief="flat", font=("Microsoft YaHei UI", 10),bg='gray')
        state.place(relx=0.5, y=110, relwidth=0.45, height=150)
    elif lan == 4:
        lab1 = Label(root, text='Maustaste', font=("Microsoft YaHei UI", 11), fg="gray",bg='black')
        lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)
        r1 = Radiobutton(root,
                         text='Links',
                         font=("Microsoft YaHei UI", 10),
                         fg='white',
                         bg='black',
                         value=0,
                         variable=mouse)
        r1.place(relx=0.05, y=40, relwidth=0.1, height=30)
        r2 = Radiobutton(root,
                         text='Rechts',
                         font=("Microsoft YaHei UI", 10),
                         fg='white',
                         bg='black',
                         value=1,
                         variable=mouse)
        r2.place(relx=0.18, y=40, relwidth=0.1, height=30)
        r3 = Radiobutton(root,
                         text='Mitte',
                         font=("Microsoft YaHei UI", 10),
                         fg='white',
                         bg='black',
                         value=2,
                         variable=mouse)
        r3.place(relx=0.31, y=40, relwidth=0.12, height=30)

        lab2 = Label(root, text='CPS-Einstellungen', font=("Microsoft YaHei UI", 11), fg="gray",bg='black')
        lab2.place(relx=0.5, y=10, relwidth=0.45, height=30)
        label3 = Label(root,
                   text='---------- Tipps und Programmstatus ----------',
                   font=("Microsoft YaHei UI", 8),
                   fg="gray",bg="black")
        label3.place(relx=0.5, y=90, relwidth=0.45, height=20)
       
        
        b2 = Button(root, text='Über', font=('Arial', 10), fg="grey",bg='black',command=about)
        b2.place(relx=0.07, y=220, relwidth=0.16, height=30)

        b3 = Button(root, text='Änderungsprotokoll', font=('Arial', 10), fg="grey",bg='black',command=logs)
        b3.place(relx=0.23, y=220, relwidth=0.20, height=30)
        b4 = Button(root, text='Protokoll aktualisieren', font=('Arial', 10), fg="grey",bg='black',command=more)
        b4.place(relx=0.07, y=280, relwidth=0.36, height=30)
        b5 = Button(root, text='Nach Aktualisierungen suchen', font=('Arial', 10), fg="grey",bg='black',command=update)
        b5.place(relx=0.07, y=250, relwidth=0.36, height=30)

        lag = Label(root, text='Anti-Maschinen-Betrugserkennung', font=("Microsoft YaHei UI", 11),  fg="gray",bg="black")
        lag.place(relx=0.05, y=100, relwidth=0.4, height=30)

        xon = Radiobutton(root,
                         text='Öffnen Sie',
                         font=("Microsoft YaHei UI", 10),
                         fg="white",
                         bg='black',
                         value=3,
                         variable=cheat)
        xon.place(relx=0.07, y=140, relwidth=0.15, height=30)
        xr = Radiobutton(root,
                         text='Schließen Sie',
                         font=("Microsoft YaHei UI", 10),
                         fg="white",
                         bg='black',
                         value=4,
                         variable=cheat)
        xr.place(relx=0.25, y=140, relwidth=0.16, height=30)
        xr.select()
        h1 = Button(root, text='?', font=('Arial', 10),fg='green',bg='black',command=helpa)
        h1.place(relx=0.82, y=10, relwidth=0.04, height=30)

        input = Entry(root, relief="flat", font=("Microsoft YaHei UI", 10),bg='gray')
        input.place(relx=0.575, y=40, relwidth=0.3, height=30)


        state = Text(root, relief="flat", font=("Microsoft YaHei UI", 10),bg='gray')
        state.place(relx=0.5, y=110, relwidth=0.45, height=150)
    elif lan == 5:
        lab1 = Label(root, text='オブジェクトをクリックする', font=("Microsoft YaHei UI", 11), fg="gray",bg='black')
        lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)
        r1 = Radiobutton(root,
                         text='左クリック',
                         font=("Microsoft YaHei UI", 10),
                         fg='white',
                         bg='black',
                         value=0,
                         variable=mouse)
        r1.place(relx=0.05, y=40, relwidth=0.12, height=30)
        r2 = Radiobutton(root,
                         text='右クリック',
                         font=("Microsoft YaHei UI", 10),
                         fg='white',
                         bg='black',
                         value=1,
                         variable=mouse)
        r2.place(relx=0.18, y=40, relwidth=0.12, height=30)
        r3 = Radiobutton(root,
                         text='ミドルキーズ',
                         font=("Microsoft YaHei UI", 10),
                         fg='white',
                         bg='black',
                         value=2,
                         variable=mouse)
        r3.place(relx=0.32, y=40, relwidth=0.14, height=30)

        lab2 = Label(root, text='CPSの設定', font=("Microsoft YaHei UI", 11), fg="gray",bg='black')
        lab2.place(relx=0.5, y=10, relwidth=0.45, height=30)
        label3 = Label(root,
                   text='---------- プログラムメッセージ ----------',
                   font=("Microsoft YaHei UI", 8),
                   fg="gray",bg="black")
        label3.place(relx=0.5, y=90, relwidth=0.45, height=20)
       
        
        b2 = Button(root, text='について', font=('Arial', 10), fg="grey",bg='black',command=about)
        b2.place(relx=0.07, y=220, relwidth=0.16, height=30)

        b3 = Button(root, text='更新履歴', font=('Arial', 10), fg="grey",bg='black',command=logs)
        b3.place(relx=0.23, y=220, relwidth=0.20, height=30)
        b4 = Button(root, text='アップデートを確認する', font=('Arial', 10), fg="grey",bg='black',command=more)
        b4.place(relx=0.07, y=280, relwidth=0.36, height=30)
        b5 = Button(root, text='その他のオプション', font=('Arial', 10), fg="grey",bg='black',command=update)
        b5.place(relx=0.07, y=250, relwidth=0.36, height=30)

        lag = Label(root, text='機械的な不正に対する検知の防御', font=("Microsoft YaHei UI", 11),  fg="gray",bg="black")
        lag.place(relx=0.05, y=100, relwidth=0.4, height=30)

        xon = Radiobutton(root,
                         text='オープン',
                         font=("Microsoft YaHei UI", 10),
                         fg="white",
                         bg='black',
                         value=3,
                         variable=cheat)
        xon.place(relx=0.07, y=140, relwidth=0.15, height=30)
        xr = Radiobutton(root,
                         text='閉じる',
                         font=("Microsoft YaHei UI", 10),
                         fg="white",
                         bg='black',
                         value=4,
                         variable=cheat)
        xr.place(relx=0.25, y=140, relwidth=0.16, height=30)
        xr.select()
        h1 = Button(root, text='?', font=('Arial', 10),fg='green',bg='black',command=helpa)
        h1.place(relx=0.82, y=10, relwidth=0.04, height=30)

        input = Entry(root, relief="flat", font=("Microsoft YaHei UI", 10),bg='gray')
        input.place(relx=0.575, y=40, relwidth=0.3, height=30)


        state = Text(root, relief="flat", font=("Microsoft YaHei UI", 10),bg='gray')
        state.place(relx=0.5, y=110, relwidth=0.45, height=150)
    
    else:
        lab1 = Label(root, text='鼠标点击按钮设置', font=("Microsoft YaHei UI", 11), fg="gray",bg='black')
        lab1.place(relx=0.05, y=10, relwidth=0.4, height=30)
        r1 = Radiobutton(root,
                         text='左键',
                         font=("Microsoft YaHei UI", 10),
                         fg='white',
                         bg='black',
                         value=0,
                         variable=mouse)
        r1.place(relx=0.05, y=40, relwidth=0.1, height=30)
        r2 = Radiobutton(root,
                         text='右键',
                         font=("Microsoft YaHei UI", 10),
                         fg='white',
                         bg='black',
                         value=1,
                         variable=mouse)
        r2.place(relx=0.18, y=40, relwidth=0.1, height=30)
        r3 = Radiobutton(root,
                         text='中键',
                         font=("Microsoft YaHei UI", 10),
                         fg='white',
                         bg='black',
                         value=2,
                         variable=mouse)
        r3.place(relx=0.31, y=40, relwidth=0.12, height=30)

        lab2 = Label(root, text='CPS 设置', font=("Microsoft YaHei UI", 11), fg="gray",bg='black')
        lab2.place(relx=0.5, y=10, relwidth=0.45, height=30)
        label3 = Label(root,
                   text='---------- 通知中心 ----------',
                   font=("Microsoft YaHei UI", 8),
                   fg="gray",bg="black")
        label3.place(relx=0.5, y=90, relwidth=0.45, height=20)
       
        
        b2 = Button(root, text='关于', font=('Arial', 10), fg="grey",bg='black',command=about)
        b2.place(relx=0.07, y=220, relwidth=0.16, height=30)

        b3 = Button(root, text='更新日志', font=('Arial', 10), fg="grey",bg='black',command=logs)
        b3.place(relx=0.23, y=220, relwidth=0.20, height=30)
        b4 = Button(root, text='更多', font=('Arial', 10), fg="grey",bg='black',command=more)
        b4.place(relx=0.07, y=280, relwidth=0.36, height=30)
        b5 = Button(root, text='检查更新（手动）', font=('Arial', 10), fg="grey",bg='black',command=update)
        b5.place(relx=0.07, y=250, relwidth=0.36, height=30)

        lag = Label(root, text='反机器诈术侦测', font=("Microsoft YaHei UI", 11),  fg="gray",bg="black")
        lag.place(relx=0.05, y=100, relwidth=0.4, height=30)

        xon = Radiobutton(root,
                         text='开启',
                         font=("Microsoft YaHei UI", 10),
                         fg="white",
                         bg='black',
                         value=3,
                         variable=cheat)
        xon.place(relx=0.07, y=140, relwidth=0.15, height=30)
        xr = Radiobutton(root,
                         text='关闭',
                         font=("Microsoft YaHei UI", 10),
                         fg="white",
                         bg='black',
                         value=4,
                         variable=cheat)
        xr.place(relx=0.25, y=140, relwidth=0.15, height=30)
        xr.select()
        h1 = Button(root, text='?', font=('Arial', 10),fg='green',bg='black',command=helpa)
        h1.place(relx=0.8, y=10, relwidth=0.04, height=30)

        input = Entry(root, relief="flat", font=("Microsoft YaHei UI", 10),bg='gray')
        input.place(relx=0.575, y=40, relwidth=0.3, height=30)


        state = Text(root, relief="flat", font=("Microsoft YaHei UI", 10),bg='gray')
        state.place(relx=0.5, y=110, relwidth=0.45, height=150)

#-----------------------------------------------------------------------------

if lan == 2:
    state.insert(INSERT, "Current State: IDLE\n")
    state.insert(INSERT, "Choose which mouse button you want to click and enter CPS in CPS setting, then click START button to start clicking.")
    btn_start = Button(root,
                   text='START',
                   font=("Microsoft YaHei UI", 12),
                   fg="white",
                   bg="#207fdf",
                   relief="flat",
                   command=bth_start)
    #print("1")
elif lan == 3:
    state.insert(INSERT, "Текущий статус: Ожидание\n")
    state.insert(INSERT, "Выберите объект щелчка мыши и введите CPS в поле 'Параметры CPS', затем вы можете нажать кнопку 'Нажмите для запуска', чтобы запустить программу")
    btn_start = Button(root,
                   text='Начало реализации',
                   font=("Microsoft YaHei UI", 12),
                   fg="white",
                   bg="#207fdf",
                   relief="flat",
                   command=bth_start)
elif lan == 4:
    state.insert(INSERT, "Aktueller Status: In Erwartung\n")
    state.insert(INSERT, "Wählen Sie ein Mausklick-Objekt aus und geben Sie CPS in das Feld 'CPS-Einstellungen' ein, dann können Sie auf die Schaltfläche 'Zum Starten klicken' klicken, um das Programm zu starten")
    btn_start = Button(root,
                   text='Beginn der Durchführung',
                   font=("Microsoft YaHei UI", 12),
                   fg="white",
                   bg="#207fdf",
                   relief="flat",
                   command=bth_start)
elif lan == 5:
    state.insert(INSERT, "現在の状態：アイドル\n")
    state.insert(INSERT, "マウスクリックオブジェクトを選択し、「CPS設定」フィールドにCPSを入力すると、「クリックで起動」ボタンをクリックしてプログラムを実行することができます")
    btn_start = Button(root,
                   text='クリックで起動',
                   font=("Microsoft YaHei UI", 12),
                   fg="white",
                   bg="#207fdf",
                   relief="flat",
                   command=bth_start)
    
else:
    state.insert(INSERT, "当前状态：空闲\n")
    state.insert(INSERT, "选择一个鼠标点击对象并在‘CPS 设置’一栏中输入CPS， 然后，你就可以点击'点击以开始'按钮以运行程序")
    btn_start = Button(root,
                   text='点击以开始',
                   font=("Microsoft YaHei UI", 12),
                   fg="white",
                   bg="#207fdf",
                   relief="flat",
                   command=bth_start)


btn_start.place(relx=0.5, y=280, relwidth=0.45, height=30)




#------------------------------------------------------------------------------------------------------
if theme == 1:
    root.configure(bg='#FFFAFA')
if theme == 2:
    root.configure(bg='black')
if theme == 0:
    sys.exit(0)
#-------------------------------------------------------------------------------------------

menubar = Menu(root)
#　定义一个空的菜单单元
filemenu = Menu(menubar, tearoff=0)  # tearoff意为下拉
#　将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
if lan == 2:
    menubar.add_cascade(label='Shortcut Settings', menu=filemenu)



    submenu = Menu(filemenu)
    submenu1 = Menu(filemenu) 
    filemenu.add_cascade(label='Themes', menu=submenu, underline=0)
    submenu.add_command(label='Light Mode', command=light)
    submenu.add_command(label='Dark Mode', command=dark)
    filemenu.add_cascade(label='Language', menu=submenu1, underline=0)
    submenu1.add_command(label='简体中文（中国大陆）', command=chinese)
    submenu1.add_command(label='English(United States)', command=english)
    submenu1.add_command(label='Русский', command=russian)
    submenu1.add_command(label='Deutsch', command=german)
    submenu1.add_command(label='日本語', command=japanese)
    # 分隔线
    filemenu.add_separator()
    filemenu.add_command(label='EXIT', command=root.quit)
     

    editmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='HELP', menu=editmenu)
    editmenu.add_command(label='Go to Github Feedback', command=github)
elif lan == 3:
    menubar.add_cascade(label='Настройки ярлыков', menu=filemenu)



    submenu = Menu(filemenu)
    submenu1 = Menu(filemenu) 
    filemenu.add_cascade(label='Темы', menu=submenu, underline=0)
    submenu.add_command(label='Светлый цветной рисунок', command=light)
    submenu.add_command(label='Темный режим', command=dark)
    filemenu.add_cascade(label='Язык', menu=submenu1, underline=0)
    submenu1.add_command(label='简体中文（中国大陆）', command=chinese)
    submenu1.add_command(label='English(United States)', command=english)
    submenu1.add_command(label='Русский', command=russian)
    submenu1.add_command(label='Deutsch', command=german)
    submenu1.add_command(label='日本語', command=japanese)
    # 分隔线
    filemenu.add_separator()
    filemenu.add_command(label='Вывод средств', command=root.quit)
     

    editmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Помощь', menu=editmenu)
    editmenu.add_command(label='Перейти к отзывам на Github', command=github)
elif lan == 4:
    menubar.add_cascade(label='Shortcut-Einstellungen', menu=filemenu)



    submenu = Menu(filemenu)
    submenu1 = Menu(filemenu) 
    filemenu.add_cascade(label='Themen', menu=submenu, underline=0)
    submenu.add_command(label='Helles Farbmuster', command=light)
    submenu.add_command(label='Dunkler Modus', command=dark)
    filemenu.add_cascade(label='Sprache', menu=submenu1, underline=0)
    submenu1.add_command(label='简体中文（中国大陆）', command=chinese)
    submenu1.add_command(label='English(United States)', command=english)
    submenu1.add_command(label='Русский', command=russian)
    submenu1.add_command(label='Deutsch', command=german)
    submenu1.add_command(label='日本語', command=japanese)
    # 分隔线
    filemenu.add_separator()
    filemenu.add_command(label='Rücknahme', command=root.quit)
     

    editmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Hilfe', menu=editmenu)
    editmenu.add_command(label='Zu Github Feedback gehen', command=github)
elif lan == 5:
    menubar.add_cascade(label='ショートカットの設定', menu=filemenu)



    submenu = Menu(filemenu)
    submenu1 = Menu(filemenu) 
    filemenu.add_cascade(label='トピックス', menu=submenu, underline=0)
    submenu.add_command(label='淡色パターン', command=light)
    submenu.add_command(label='ダークモード', command=dark)
    filemenu.add_cascade(label='言語', menu=submenu1, underline=0)
    submenu1.add_command(label='简体中文（中国大陆）', command=chinese)
    submenu1.add_command(label='English(United States)', command=english)
    submenu1.add_command(label='Русский', command=russian)
    submenu1.add_command(label='Deutsch', command=german)
    submenu1.add_command(label='日本語', command=japanese)
    # 分隔线
    filemenu.add_separator()
    filemenu.add_command(label='退出時の手続き', command=root.quit)
     

    editmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='ヘルプ', menu=editmenu)
    editmenu.add_command(label='Github フィードバックへ', command=github)
else:
    menubar.add_cascade(label='快捷设置', menu=filemenu)



    submenu = Menu(filemenu)
    submenu1 = Menu(filemenu) 
    filemenu.add_cascade(label='主题', menu=submenu, underline=0)
    submenu.add_command(label='浅色模式', command=light)
    submenu.add_command(label='深色模式', command=dark)
    filemenu.add_cascade(label='语言', menu=submenu1, underline=0)
    submenu1.add_command(label='简体中文（中国大陆）', command=chinese)
    submenu1.add_command(label='English(United States)', command=english)
    submenu1.add_command(label='Русский', command=russian)
    submenu1.add_command(label='Deutsch', command=german)
    submenu1.add_command(label='日本語', command=japanese)
    # 分隔线
    filemenu.add_separator()
    filemenu.add_command(label='退出', command=root.quit)
     

    editmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='帮助', menu=editmenu)
    editmenu.add_command(label='前往Github反馈', command=github)
 

 
 
root.config(menu=menubar)  # 加上这代码，才能将菜单栏显示



root.mainloop()







 
    
