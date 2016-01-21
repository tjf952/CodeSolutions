#include <iostream>
using namespace std;

/*
   Sum of the even-valued terms of the Fibonacci
   sequence below four million
*/

int fib(int n){
   if(n == 0) return 0;
   if(n == 1) return 1;
   return fib(n-1) + fib(n-2);
}

int sum(int n){
	int total = 0, i = 0;
	while(fib(i) < n){
		if(fib(i)%2 == 0) total += fib(i);
		i++;
	}	
	return total;
}

int main(){
   int x;
   cin >> x;
   cout << sum(x) << endl;
}
