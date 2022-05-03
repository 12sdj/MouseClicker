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

//全局变量 
int a;
long c;
long long b; 

void Test()
{
	HWND hWnd = GetConsoleWindow();
	HMENU hMenu = GetSystemMenu(hWnd, false);
	RemoveMenu(hMenu, SC_MAXIMIZE, MF_BYCOMMAND);
	DestroyMenu(hMenu);
	ReleaseDC(hWnd, NULL);
}
void func()
{
	//			if(MessageBox(NULL,"Still Continue?","MouseClicker",MB_YESNO+32)==6)
	int ch;
	while (1) {
		default_random_engine e;
   		uniform_real_distribution<double> u(-80.0, 40.0);
		u(e);
		int(u(e));
		default_random_engine p;
   		uniform_real_distribution<double> s(-50.0, 30.0);
		s(p);
		int(s(p));
		
		for (int d =1 ;d<= 40; d++){
			mouse_event(MOUSEEVENTF_LEFTDOWN, 500, 500, 0, 0);
			mouse_event(MOUSEEVENTF_LEFTUP, 500, 500, 0, 0);
			Sleep(c+u(e)); 
		}
		for (int k =1 ;k <= 40 ;k++){
			mouse_event(MOUSEEVENTF_LEFTDOWN, 500, 500, 0, 0);
			mouse_event(MOUSEEVENTF_LEFTUP, 500, 500, 0, 0);
			Sleep(c+s(p)); 		
		}
		for (int k =1 ;k <= 10 ;k++){
			mouse_event(MOUSEEVENTF_LEFTDOWN, 500, 500, 0, 0);
			mouse_event(MOUSEEVENTF_LEFTUP, 500, 500, 0, 0);
			Sleep(c-c/2); 		
		}
	
		
		

					
	}
}

void funk()
{
	while (1) {
		default_random_engine e;
   		uniform_real_distribution<double> u(-30.0, 50.0);
		u(e);
		int(u(e));
		mouse_event(MOUSEEVENTF_RIGHTDOWN, 500, 500, 0, 0);
		mouse_event(MOUSEEVENTF_RIGHTUP, 500, 500, 0, 0);
		
		Sleep(c+u(e)); 
				
					
	}
}

void funs()
{
	while (1) {
		default_random_engine e;
   		uniform_real_distribution<double> u(-30.0, 50.0);
		u(e);
		int(u(e));
		mouse_event(MOUSEEVENTF_MIDDLEDOWN, 500, 500, 0, 0);
		mouse_event(MOUSEEVENTF_MIDDLEUP, 500, 500, 0, 0);
		
		Sleep(c+u(e)); 
				
					
	}
}


int main()
{
	Test();
	int ch;
	

	while (true){
		a = 0;
		b = 0;
		c = 0;
		cout << "Version 3.3(Update 08) Made by 12sdj" << endl;
		cout << "Version 3.3.0 Release" << endl;
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
		Sleep(1);
		cout << "3.0(Update 06 2022.4.26)" << endl;
		Sleep(3);
		cout << "3.2(Update 07 2022.5.1)" << endl;
		Sleep(5);
		cout << "3.3(Update 08 2022.5.3)" << endl;
		cout << endl;
		system("color 03");
		cout << "About 3s later, This procedure will begin to start." <<endl;
		Sleep(3150);
		
		system("cls");
		system("title MouseClicker V3.3");
		cout << "Settings" << endl;
		cout << endl;
		Sleep(445);
		cout << "CPS, is the abbreviation of 'Click per second'. The Chinese translation is the number of clicks per second, which can also be understood as hand speed. The average person's CPS does not exceed 10. Using tools such as a connector can make the CPS exceed this number, and the limit can even reach 60." << endl;
		cout << "Please input CPS: ";
		cin >> b;
		cout << endl;
		
	
	
  		if(b <= 0) {
        	printf("<MouseClicker: Error>\n");
			MessageBox(NULL,"Program Error!                                ","MouseClicker",MB_OK+16);
			MessageBox(NULL,"Please enter an appropriate positive number!  ","MouseClicker",MB_OK+48);
			MessageBox(NULL,"Program Crashes!                              ","MouseClicker",MB_OK+16);
			return false;
	}
		
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
		cout <<"Settings" << endl;
		cout << endl;
		cout << "CPS: " << b <<endl;
		cout << "Click: " << put << endl;
		cout << "Turn on/off: " <<"ESC"<<endl;
		
		
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

		if(strcmp(put, "left") == 0){
		
			cout << "<Is created and detached thread>" << endl;
			
			thread t(func);
			t.detach();
			
			
			cout << "<WAITING>" << endl;
			Sleep(2000);
			system("cls");
			cout << "<Execution>" << endl;  
			while(1){
				for (int e =1 ;e<= 5; e++){
				mouse_event(MOUSEEVENTF_LEFTDOWN, 500, 500, 0, 0);
				mouse_event(MOUSEEVENTF_LEFTUP, 500, 500, 0, 0);
				Sleep(c+1000); 	
			}
				ch=getch();
				if (ch == 27) {
					return 0;
				}
				
				
				

			}
		
	}	
		
	
		if(strcmp(put, "right") == 0){
			cout << "<Execution>" << endl;
			cout << "<Is created and detached thread>" << endl;
			
			thread k(funk);
			k.detach();
			cout << "<WAITING>" << endl;
			Sleep(2000);
			system("cls");
			cout << "<Execution>" << endl; 
	
			while(1){
				ch=getch();
				if (ch == 27) {
					system("pause");
				}

			}		
						
				
				

}
		if(strcmp(put, "middle") == 0){
			cout << "<Execution>" << endl;
			cout << "<Is created and detached thread>" << endl;
			
			thread s(funs);
			s.detach();
		
			cout << "<WAITING>" << endl;
			Sleep(2000);
			system("cls");
			cout << "<Execution>" << endl; 
			while(1){
				ch=getch();
				if (ch == 27) {
					system("pause");
				}

			}

		
}
	
	
	
	
		else{
			system("color 04");
			cout <<"ERROR!PLEASE INPUT 'LEFT' or 'RIGHT' or 'MIDDLE'" <<endl;
			MessageBox(NULL,"ERROR!PLEASE INPUT 'LEFT' or 'RIGHT' or 'MIDDLE'. Please try again!'.","MouseClicker",MB_OK+16);
			cout << "<Restart>" << endl;
			for (int res = 1; res <= 5; res++){
				cout << "</Restarting,Please Wait .../> " << "</There are" << 6-res << "seconds left/>" << endl;
				Sleep(970);
			}
			Sleep(1550);
			system("cls");
			
		}
}

}
