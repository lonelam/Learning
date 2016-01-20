#include<iostream>
#include<string>
using namespace std;
void bondini(){
	cout<<"Operation \" Hyperhype\" is now activated!\b\b\b\b\b\b";
}
void assign(){
	cout.setf(ios_base::fixed, ios_base::floatfield);
	char grade='A';
	cout<<(int)grade;
}
void charandstr(){
	char dog[9]={'a','2','2','2','2','2','2','2','3'};
	cout<<dog;
}
void strclass(){
	string cat="Who's your daddy";
	char mount[1];
	cin>>cat;
	cout<<cat;
	cin>>mount;
	cout<<mount;
}
void swap(int a,int b){
	int c;
	c=a;a=b;b=c;
}
void simpletest(){
	int first=1,second=2;
	swap(first,second);
	cout<<first<<second;
}
void fstruct(){
	struct fclass{
		char name[20];
		short number;
		char cls;
	};
	fclass my={
	"uncle",10,1
	};
	cout<<my.name<<my.cls;
}

int main(){
	simpletest();
} 

