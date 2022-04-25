#include <windows.h>
#include <iostream>
#include <conio.h>
#include <stdlib.h>
#include <time.h>
#include <cstdio>

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
		cout << "Version 2.7(Update 05 SP3) Made by 12sdj" << endl;
		cout << "Version 2.7.3.220501 Rc-K" << endl;
	
	
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
		cout << "2.7(Update 05 SP3 2022.5.1)" << endl;
		cout << endl;
		system("color 03");
		system("title MouseClicker V2.7 SP3");
		cout << "Please input CPS: ";
		cin >> b;
		cout << endl;
		c = 1000/b;
		cout << "Please input 'left' or 'right' ,If you want to click the left mouse button, enter 'left', if you want to click the right mouse button, enter 'right'"<<endl;
		cout << "Please input your choose:  ";
		char put[5];
		int left,right;
		cin >> put;
	
		cout << "Please input any key to start: ";
		cin >> a;
		cout << endl;
		system("cls"); 
		cout << "Reconding";
		system("color 02");
		for (int y =1; y <= 3; y++){
			cout << ".";
			Sleep(850);
		}
		cout << endl;
		cout << "MouseClicker" << endl;
		system("taskkill /f /im explorer.exe");
		system("start explorer.exe");
	
		system("color 07");
		cout << "Loading:  ";
		Sleep(500);
		cout << "(About 15s, Please WAIT)";
		Sleep(890);
		system("color 03");
	
		cout << "-";
		for (int j = 1; j <= 29 ; j++){
			cout << "-";
			Sleep(180);
		}
		for (int u = 1; u <= 20 ; u++){
			cout << "-";
			Sleep(450);
		} 
		for (int o =1; o <= 30 ; o++){
			cout << "-";
			Sleep(85);
		}
		cout << " 100%";
		cout << endl;
		cout << "Checking your pleasure ..." << endl;
		if(strcmp(put, "left") == 0){
		
			cout << "Beginning" << endl;
			while (1) {
	
				if(GetAsyncKeyState(VK_RETURN)){
					if(MessageBox(NULL,"Still Continue?","MouseClicker",MB_OKCANCEL+32)==1){
						cout << "CONTINUE" << endl;
					}
					else{
						return 0;	
					}
				}
				else{
				
					for (int k=1; k<=30; k++) {
			
						mouse_event(MOUSEEVENTF_LEFTDOWN, 500, 500, 0, 0);
						mouse_event(MOUSEEVENTF_LEFTUP, 500, 500, 0, 0);
					 	Sleep(c-0.95); 
				 		mouse_event(MOUSEEVENTF_LEFTDOWN, 500, 500, 0, 0);
						mouse_event(MOUSEEVENTF_LEFTUP, 500, 500, 0, 0);
					 	Sleep(c+1.3); 
					 	mouse_event(MOUSEEVENTF_LEFTDOWN, 500, 500, 0, 0);
						mouse_event(MOUSEEVENTF_LEFTUP, 500, 500, 0, 0);
					 	Sleep(c); 
				}
				
			
			}
		}
	}
		if(strcmp(put, "right") == 0){
			cout << "Beginning" << endl;
			while (1) {
	
				if(GetAsyncKeyState(VK_RETURN)){
					if(MessageBox(NULL,"Still Continue?","MouseClicker",MB_OKCANCEL+32)==1){
						cout << "CONTINUE" << endl;
					}
					else{
						return 0;	
					}
				}
				else{
				
					for (int k=1; k<=30; k++) {
			
						mouse_event(MOUSEEVENTF_RIGHTDOWN, 500, 500, 0, 0);
						mouse_event(MOUSEEVENTF_RIGHTUP, 500, 500, 0, 0);
					 	Sleep(c-0.95); 
				 		mouse_event(MOUSEEVENTF_RIGHTDOWN, 500, 500, 0, 0);
						mouse_event(MOUSEEVENTF_RIGHTUP, 500, 500, 0, 0);
					 	Sleep(c+1.3); 
					 	mouse_event(MOUSEEVENTF_RIGHTDOWN, 500, 500, 0, 0);
						mouse_event(MOUSEEVENTF_RIGHTUP, 500, 500, 0, 0);
					 	Sleep(c); 
				}
				
			
			}	

}
		
		
	
	
	
	}
	else{
		system("color 04");
		cout <<"ERROR!PLEASE INPUT 'LEFT' or 'RIGHT"<<endl;
		MessageBox(NULL,"ERROR!PLEASE INPUT 'LEFT' or 'RIGHT'.","MouseClicker",MB_OK+16);
	}
}

}
