#include <windows.h>
#include <iostream>
#include <conio.h>
#include <stdlib.h>
#include <time.h>
#include <cstdio>

#define KEY_DOWN(VK_NONAME) ((GetAsyncKeyState(VK_NONAME) & 0x8000) ? 1:0) 
using namespace std;

int main()
{
	int a;
	long c;
	long long b; 

	cout << "Version 2.7(Update 05 2022.4.15) Made by 12sdj" << endl;

	cout << "All History Update:" << endl;
	cout << "1.0(2021.12.25)" << endl;
	cout << "1.1(Update 01 2022.1.15)" << endl;
	cout << "1.2(Update 02 2022.1.25)" << endl;
	cout << "2.0(Update 03 2022.4.15)" << endl;
	cout << "2.1(Update 04 2022.4.15)" << endl;
	cout << "2.7(Update 05 2022.4.15)" << endl;
	system("color 03");
	system("title MouseClicker V2.7");
	cout << "Please input CPS: ";
	cin >> b;
	cout << endl;
	c = 1000/b;
	cout << "Please input any key to start: ";
	cin >> a;
	cout << endl;
	cout << "Reconding!" << endl;
	cout << "-";
	for (int j = 1; j <= 10 ; j++){
		cout << "-";
		Sleep(500);
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
