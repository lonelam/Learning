#include<iostream>
int main(){
	using namespace std;
	int a,b;short c;
	a=10;
	while (a){
		b+=a;
		a--; 
		cout<<a;
		c=SHRT_MAX;
		c=c+1;
	}
	cout<<b<<endl<<c;
	return (0);
}
