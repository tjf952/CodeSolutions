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
	
	return sum(n-1);
}

int main(){
   int x = sum(89);
   cout << x << endl;
}
