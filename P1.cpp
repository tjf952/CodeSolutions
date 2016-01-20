#include <iostream>
using namespace std;

// Sum of all the multiples of 3 or 5 below 1000

int sum(int n){
   if(n == 0) return 0;
   if((n%3 == 0) || (n%5 == 0)) return sum(n-1) + n;
   return sum(n-1);
}

int main(){
   int x = sum(999);
   cout << x << endl;
}
