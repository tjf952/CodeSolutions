#include <iostream>
#include <math.h>
#include <string>

using namespace std;

/*
    Find the difference between the sum of the squares of the 
    first one hundred natural numbers and the square of the sum.
*/

int diff(int x){
    int sum = x*(x+1)/2;
    int squ = x*(2*x+1)*(x+1)/6;
    return pow(sum, 2) - squ;
}

int main(){
    int x;
    cin >> x;
    cout << diff(x);
    return 0;
}
