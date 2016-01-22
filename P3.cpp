#include <iostream>
#include <math.h>
using namespace std;

/*
   Largest prime factor of x
*/

bool prime(long n){
   for(long i = 2; i <= sqrt(n); i++){
      if((n%i) == 0) return false;
   }
   return true;
}

int pfactor(long n){
   long largest = -1;
	for(long i = 3; i < sqrt(n); i+=2){
      if((n%i == 0) && prime(i)){
         cout << "Prime Factor: " << i << endl;
         largest = i;
      }
   }
   return largest;
}

int main(){
   long x;
   cin >> x;
   cout << pfactor(x) << endl;
}
