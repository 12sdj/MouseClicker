#include <windows.h>
#include <iostream>
#include <conio.h>
#include <stdlib.h>
#include <time.h>
#include <cstdio>
#include<thread>
#include<cstdlib>
#include<bits/stdc++.h>
#include<random>
#define KEY_DOWN(VK_NONAME) ((GetAsyncKeyState(VK_NONAME) & 0x8000) ? 1:0) 
using namespace std;


int a;
long c;
long long b; 
int kill = 0;

void Test()
{
	HWND hWnd = GetConsoleWindow();
	HMENU hMenu = GetSystemMenu(hWnd, false);
	RemoveMenu(hMenu, SC_MAXIMIZE, MF_BYCOMMAND);
	DestroyMenu(hMenu);
	ReleaseDC(hWnd, NULL);
}

void func2(){
	printf("%s","<func2: Everything works fine>/n");
	printf("%s","[Please Note: Press the SPACEBAR to start or end running the program]");
	while(1)
    {
        if(GetAsyncKeyState(VK_SPACE))//按下空格，开始执行
        {
            while(1)
            {
                mouse_event(MOUSEEVENTF_LEFTDOWN|MOUSEEVENTF_LEFTUP,500,500,0,0);
                Sleep(10);
                if(GetAsyncKeyState(VK_ESCAPE)){
                	kill = 1;
				}
            }
        }
    }

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
	int af;

	while (true){
		a = 0;
		b = 0;
		c = 0;
		af = 0;
		printf("%s","MouseClicker Basic\n");
		printf("%s","Version 3.5.2(build 3110_220701) Release\n");
		printf("%s","Version 3.5(Update 10) Made by 12sdj\n");
		printf("%s","Copyright (c) 2022 12sdj\n");
		printf("%s","More information: https://github.com/12sdj/MouseClicker-by-12sdj\n");
		printf("%s","Checking updates: https://github.com/12sdj/MouseClicker-by-12sdj/releases\n");
		printf("%s","Please note: This update is the last functional update in the series\n");

	
	
		cout << endl;
		cout << endl;
		printf("%s","What's new (compared to the previous version): \n");
		printf("%s","1.Fix one or more bug(s)\n");
		printf("%s","2.Remove some unnecessary effects and optimize the user interface\n");
		cout << endl;
		system("color 02");
		cout << "About 4s later, This procedure will begin to start." <<endl;
		Sleep(4150);
		
		system("cls");
		system("title MouseClicker Basic V3.5");
		cout << "Settings" << endl;
		cout << endl;
		cout << "CPS, is the abbreviation of 'Click per second'. The Chinese translation is the number of clicks per second, which can also be understood as hand speed. The average person's CPS does not exceed 10. Using tools such as a connector can make the CPS exceed this number, and the limit can even reach 60." << endl;
		cout << "Please input CPS: ";
		cin >> b;
		cout << endl;
		
	
	
  		if(b <= 0) {
        	printf("<MouseClicker Basic: Error>\n");
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

		thread t(func2);
		t.detach();
		
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
		cout << "MouseClicker Baisc" << endl;

	
		system("color");
		cout << "Loading:  ";
		Sleep(500);
		cout << "(About 10s, Please WAIT) ";
		Sleep(890);
		system("color 03");
	
		cout << "-";
		for (int j = 1; j <= 19 ; j++){
			cout << "-";
			Sleep(40);
		}
		
		for (int o =1; o <= 30 ; o++){
			cout << "-";
			Sleep(65);
		}
		cout << " 100%";
		cout << endl;
		cout << "Checking your pleasure ..." << endl;
		Sleep(500);

		if(strcmp(put, "left") == 0){
			af = 1;
		}
		if(strcmp(put, "right") == 0){
			af = 2;
		}
		if(strcmp(put, "middle") == 0){
			af = 3;
		}
		if(strcmp(put, "left") != 0 and strcmp(put, "right") != 0 and strcmp(put, "middle") != 0){
			af = 4;
		}
		cout << "<Is created and detached thread>" << endl;
			
		
		if(af == 1){
			thread t(func);
			t.detach();
			cout << "<WAITING>" << endl;
			Sleep(2000);
			system("cls");
			cout << "<Execution>" << endl;  
			
		
			while(1){
				
				if(kill == 1){
					system("pause");
				}
			
				

			}
	}
	
		
		if(af == 2){



			thread k(funk);
			k.detach();
			cout << "<WAITING>" << endl;
			Sleep(2000);
			system("cls");
			cout << "<Execution>" << endl; 
			while(1){
				
				if(kill == 1){
					system("pause");
				}
			}
				

			}
	
			
	
				
				

		if(af == 3){
			
			thread s(funs);
			s.detach();
		
			cout << "<WAITING>" << endl;
			Sleep(2000);
			system("cls");
			cout << "<Execution>" << endl;
			while(1){
				
				if(kill == 1){
					system("pause");
				}
			}
				

			} 
	
		

	
		if(af == 4){
			system("color 04");
			cout <<"ERROR!PLEASE INPUT 'LEFT' or 'RIGHT' or 'MIDDLE'" <<endl;
			MessageBox(NULL,"ERROR!PLEASE INPUT 'LEFT' or 'RIGHT' or 'MIDDLE'. Please try again!'.","MouseClicker",MB_OK+16);
			cout << "<Restart>" << endl;
			for (int res = 1; res <= 5; res++){
				cout << "</Restarting,Please Wait .../> " << "</There are" << 6-res << "seconds left/>" << endl;
				Sleep(970);
				system("cls");
			}
			Sleep(1550);
			system("cls");
	}
			
		
}

}
