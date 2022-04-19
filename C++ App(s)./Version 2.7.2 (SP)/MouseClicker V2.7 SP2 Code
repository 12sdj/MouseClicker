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
	
	cout << "Version 2.7(Update 05 SP2) Made by 12sdj" << endl;

	cout << "All History Update:" << endl;
	cout << "1.0(2021.12.25)" << endl;
	cout << "1.1(Update 01 2022.1.15)" << endl;
	cout << "1.2(Update 02 2022.1.25)" << endl;
	cout << "2.0(Update 03 2022.4.15)" << endl;
	cout << "2.1(Update 04 2022.4.15)" << endl;
	cout << "2.7(Update 05 2022.4.15)" << endl;
	cout << "2.7(Update 05 SP1 2022.4.18)" << endl;
	cout << "2.7(Update 05 SP2 2022.4.19)" << endl;
	system("color 03");
	system("title MouseClicker V2.7 SP2");
	cout << "Please input CPS: ";
	cin >> b;
	cout << endl;
	c = 1000/b;
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
		Sleep(80);
	}
	cout << " 100%";
	cout << endl;
	cout << "Beginning!" << endl;

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
