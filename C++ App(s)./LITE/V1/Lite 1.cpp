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
	cout << "Welcome to use MOUSECLICKER LITE. But the version is not the original, some features will not be added on this release."<< endl;
	cout << "Version 1.0(Lite) Made by 12sdj" << endl;
	cout << "MIT License: Copyright (c) 2022 12sdj" << endl;
	cout << endl;

	cout << "All History Update:" << endl;
	cout << "1.0(2022.5.2)" << endl;

	system("color 03");
	system("title MouseClicker LITE V1");
	cout << "Please input CPS: ";
	cin >> b;
	cout << endl;
	c = 1000/b;
	system("cls");
	cout << "Please wait..." << endl;
	Sleep(2000);
	system("cls");
	cout << "Working!" << endl;
	
	int ch;
	while (1) {

		if (_kbhit()){
			ch = _getch();
				
			if (ch == 76){
				if(MessageBox(NULL,"Still Continue?","MouseClicker",MB_YESNO+32)==6){
					cout << "CONTINUE" << endl;
				}
				else{
					break;	
				}
			}
		}
		else{
			
		
			mouse_event(MOUSEEVENTF_LEFTDOWN, 500, 500, 0, 0);
			mouse_event(MOUSEEVENTF_LEFTUP, 500, 500, 0, 0);
			Sleep(c); 
		}
			
		
		}


		
		
	
	
	
	}

