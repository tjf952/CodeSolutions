#include <iostream>
#include <math.h>
#include <string>

using namespace std;

/*
    Finding nth prime number (10 001)
*/

bool prime(long n){
   for(long i = 2; i <= sqrt(n); i++){
      if((n%i) == 0) return false;
   }
   return true;
}

int counter(int x){
    int count = 1, num = 1;
    while(count != x){
        num+=2;
        if(prime(num)) count++;
    }
    return num;
}

int main(){
    int x;
    cin >> x;
    cout << counter(x);
    return 0;
}
