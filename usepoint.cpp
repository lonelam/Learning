#include<iostream>
using namespace std;
void swap(int *a, int *b){
	int c;
	c=*a;*a=*b;*b=c;
}
void usepoint(){
	int a=1;
	int *pa;
	int*ppa;
	pa=&a;
	*ppa=9;
	cout<<pa<<endl<<*pa;
}
void useswap(){
	int a,b;
	a=1;b=2;
	cout<<a<<endl<<b<<endl;
	swap(&a,&b);
	cout<<a<<endl<<b;
}
int main(){
	useswap();	
}
