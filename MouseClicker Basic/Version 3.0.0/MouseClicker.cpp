#include <windows.h>
#include <iostream>
#include <conio.h>
#include <stdlib.h>
#include <time.h>
#include <cstdio>
#include<thread>
#include<bits/stdc++.h>
#include<random>
#define KEY_DOWN(VK_NONAME) ((GetAsyncKeyState(VK_NONAME) & 0x8000) ? 1:0) 
using namespace std;

void Test()
{
	HWND hWnd = GetConsoleWindow();
	HMENU hMenu = GetSystemMenu(hWnd, false);
	RemoveMenu(hMenu, SC_MAXIMIZE, MF_BYCOMMAND);
	DestroyMenu(hMenu);
	ReleaseDC(hWnd, NULL);
}
int main()
{
	Test();
	int a;
	long c;
	long long b; 
	

	while (true){
	
		cout << "Version 3.0(Update 06) Made by 12sdj" << endl;
		cout << "Version 3.0.0.220426 Release" << endl;
		cout << "MIT License: Copyright (c) 2022 12sdj" << endl;
	
	
		cout << endl;
		cout << endl;
		cout << "All History Update:" << endl;
		Sleep(30);
		cout << "1.0(2021.12.25)" << endl;
		Sleep(20);
		cout << "1.1(Update 01 2022.1.15)" << endl;
		Sleep(20);
		cout << "1.2(Update 02 2022.1.25)" << endl;
		Sleep(20);
		cout << "2.0(Update 03 2022.4.15)" << endl;
		Sleep(15);
		cout << "2.1(Update 04 2022.4.15)" << endl;
		Sleep(13);
		cout << "2.7(Update 05 2022.4.15)" << endl;
		Sleep(10);
		cout << "2.7(Update 05 SP1 2022.4.18)" << endl;
		Sleep(10);
		cout << "2.7(Update 05 SP2 2022.4.19)" << endl;
		Sleep(2);
		cout << "2.7(Update 05 SP3 2022.4.22)" << endl;
		cout << "3.0(Update 06 2022.4.26)" << endl;
		cout << endl;
		system("color 03");
		cout << "About 3s later, This procedure will begin to start." <<endl;
		Sleep(3150);
		
		system("cls");
		system("title MouseClicker V3.0");
		cout << "Settings" << endl;
		cout << endl;
		cout << "CPS, is the abbreviation of 'Click per second'. The Chinese translation is the number of clicks per second, which can also be understood as hand speed. The average person's CPS does not exceed 10. Using tools such as a connector can make the CPS exceed this number, and the limit can even reach 60." << endl;
		cout << "Please input CPS: ";
		cin >> b;
		cout << endl;
		c = 1000/b;
		system("cls");
		
		cout << "Settings" << endl;
		cout << endl;
		cout << "CPS: " << b <<endl;
		cout << endl;
		Sleep(500);
		cout << "Please input 'left' or 'right' or 'middle' ,If you want to click the left mouse button, enter 'left', if you want to click the right mouse button, enter 'right',if you want to click the middle mouse button, enter'middle' "<<endl;
		cout << "Please input your choose:  ";
		char put[5];
		int left,right,middle;
		cin >> put;
		
		system("cls");
		cout << "Settings"<< endl;
		cout << endl;
		cout << "CPS: " << b <<endl;
		cout << "Click: " << put << endl;
		cout << endl;	
		
		
		system("cls");
		cout <<"Settings" << endl;
		cout << endl;
		cout << "CPS: " << b <<endl;
		cout << "Click: " << put << endl;
		cout << "Turn on/off: " <<"U"<<endl;
		
		
		cout << "Please input any key to start: ";
		cin >> a;
		system("cls"); 
		
		cout << "<Processing request>" << endl;
		cout << "Processing request";
		system("color 02");
		for (int y =1; y <= 3; y++){
			cout << ".";
			Sleep(950);
		}
		cout << endl;
		system("cls");
		cout << "MouseClicker" << endl;

	
		system("color");
		cout << "Loading:  ";
		Sleep(500);
		cout << "(About 10s, Please WAIT) ";
		Sleep(890);
		system("color 03");
	
		cout << "-";
		for (int j = 1; j <= 19 ; j++){
			cout << "-";
			Sleep(110);
		}
		for (int u = 1; u <= 10 ; u++){
			cout << "-";
			Sleep(800);
		} 
		for (int o =1; o <= 30 ; o++){
			cout << "-";
			Sleep(65);
		}
		cout << " 100%";
		cout << endl;
		cout << "Checking your pleasure ..." << endl;
		int ch; 
		if(strcmp(put, "left") == 0){
		
			cout << "<Execution>" << endl;
			
		

			while (1) {
				if (_kbhit()){//如果有按键按下，则_kbhit()函数返回真
					ch = _getch();//使用_getch()函数获取按下的键值
				
					if (ch == 76){
						if(MessageBox(NULL,"Still Continue?","MouseClicker",MB_YESNO+32)==6){
							cout << "CONTINUE" << endl;
					}
						else{
							break;	
					}
					}//当按下ESC时循环，ESC键的键值时27.
				}
				
				else{
					
				
					mouse_event(MOUSEEVENTF_LEFTDOWN, 500, 500, 0, 0);
					mouse_event(MOUSEEVENTF_LEFTUP, 500, 500, 0, 0);
					Sleep(c); 
				}
					
		}
				
	}	
		
	
		if(strcmp(put, "right") == 0){
			cout << "<Execution>" << endl;
			while (1) {
	
				if (_kbhit()){//如果有按键按下，则_kbhit()函数返回真
					ch = _getch();//使用_getch()函数获取按下的键值
				
					if (ch == 76){
						if(MessageBox(NULL,"Still Continue?","MouseClicker",MB_YESNO+32)==6){
							cout << "CONTINUE" << endl;
					}
						else{
							break;	
					}
					}//当按下ESC时循环，ESC键的键值时27.
				}
				else{
				
						
					mouse_event(MOUSEEVENTF_RIGHTDOWN, 500, 500, 0, 0);
					mouse_event(MOUSEEVENTF_RIGHTUP, 500, 500, 0, 0);
					Sleep(c); 
				}
				
			
			}	

}
		if(strcmp(put, "middle") == 0){
		
			cout << "<Execution>" << endl;
			
		

			while (1) {
		
				if (_kbhit()){//如果有按键按下，则_kbhit()函数返回真
					ch = _getch();//使用_getch()函数获取按下的键值
				
					if (ch == 76){
						if(MessageBox(NULL,"Still Continue?","MouseClicker",MB_YESNO+32)==6){
							cout << "CONTINUE" << endl;
					}
						else{
							break;	
					}
					}//当按下ESC时循环，ESC键的键值时27.
				}
				else{ 
					mouse_event(MOUSEEVENTF_MIDDLEDOWN, 500, 500, 0, 0);
					mouse_event(MOUSEEVENTF_MIDDLEUP, 500, 500, 0, 0);
					Sleep(c); 
				}
					
		}
				}
		
		
	
	
	
	
		else{
			system("color 04");
			cout <<"ERROR!PLEASE INPUT 'LEFT' or 'RIGHT' or 'MIDDLE'" <<endl;
			MessageBox(NULL,"ERROR!PLEASE INPUT 'LEFT' or 'RIGHT' or 'MIDDLE'. Please try again!'.","MouseClicker",MB_OK+16);
			cout << "<Restart>" << endl;
			Sleep(2550);
			system("cls");
			
		}
}

}
