#include <iostream>
using namespace std;

// Sum of all the multiples of 3 or 5 below x

int sum(int n){
   if(n == 0) return 0;
   if((n%3 == 0) || (n%5 == 0)) return sum(n-1) + n;
   return sum(n-1);
}

int main(){
   int x;
   cin >> x;
   cout << sum(x) << endl;
}
