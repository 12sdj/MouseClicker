#include <windows.h>
#include <iostream>
#include <conio.h>
#include <stdlib.h>
#include <time.h>
#include <cstdio>


using namespace std;

int main()
{
	int a;
	long c;
	long long b; 
	system("title MouseClicker LITE V2");
	cout << "Version 2.0(Lite) Made by 12sdj" << endl;
	cout << endl;
	
	cout << "所有更新内容:" << endl;
	cout << "1.0(2022.5.2)" << endl;
	cout << "2.0(2022.5.8)" << endl;
	
	cout << "-------------------------" << endl;
	cout << "说明：" << endl;
	cout << "该版本为中国大陆地区的特供版本，具有中文和易操作性" << endl;
	cout << endl;
	cout << "该版本不具有：" << endl;
	cout << "1.原版更新周期" << endl;
	cout << "2.会除去部分功能" << endl;
	cout << "3.不会受到作者的重视" << endl;
	cout << "-------------------------" << endl;
	cout << "该版本具有开源项目和协议" << endl;
	cout << "项目地址:https://github.com/12sdj/MouseClicker-by-12sdj" << endl;
	cout << "MIT License: Copyright (c) 2022 12sdj" << endl;
	cout << "您可以使用软件进行商业用途、修改、分配、私人使用" << endl;
	cout << endl;
	
	cout << "<4秒后进入主程序>" << endl;
	Sleep(3950);
	system("cls");

	system("color 03");

	cout << "输入自定义CPS: ";
	cin >> b;
	cout << endl;
	c = 1000/b;
	system("cls");
	cout << "<已接受输入内容，请等待>" << endl;
	Sleep(2000);
	system("cls");
	cout << "<正在运行>" << endl;
	cout << "CPS:" << b << endl;
	

	while (1) {
		mouse_event(MOUSEEVENTF_LEFTDOWN, 500, 500, 0, 0);
		mouse_event(MOUSEEVENTF_LEFTUP, 500, 500, 0, 0);
		Sleep(c); 
		}
	}

