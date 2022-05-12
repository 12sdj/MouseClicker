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

	cout << "version:1.1(Update 01 2022.1.15) Made by 12sdj" << endl;

	cout << "输入 任意字符 以开始（默认CPS15)" << endl;

	cout << "请注意：目前没有任何设定的方法阻止本软件关闭" << endl;
	system("title Mouse Clicker");
	cout << "input: ";
	cin >> a;
	cout << "Beginning!" << endl;
	while (1) {
		
		for (int i = 1; i <= 50; i++) {
			mouse_event(MOUSEEVENTF_LEFTDOWN, 500, 500, 0, 0);
			mouse_event(MOUSEEVENTF_LEFTUP, 500, 500, 0, 0);
		
		}
			
		
		

	}

}
