#include<iostream>
#include<array>
#include<vector>
using namespace std;
void review1(){
	int arr[5]={1,3,5,7,9};
	int even=arr[0]+arr[4];
	cout<<even;
	char actor[30];
	vector<short> betsie(100);
	array<float,13>chuck;
	array<long double,64>dipsea;
}
void review13(){
	int in;
	cout<<"write an integer:"<<INT_MAX;
	cin>>in;
	int *p;
	p=new int[in^2];
	vector<int> pa(in);
	cout<<sizeof(*p)<<endl<<sizeof(pa);
}
void review14(){
	cout<<(int *)"Home of the olly byetes";
}
void eof(){
	char ch;
	int count =0;
	cin.get(ch);
	while(cin.fail()==false){
		cout<<ch;
		++count;
		cin.get(ch);
	}
	cout<<endl<<count<<"charactors read\n";
}
int main(){
	eof();
}
