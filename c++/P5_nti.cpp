#include <iostream>
#include <math.h>
#include <string>

using namespace std;

/*
    What is the smallest positive number that is 
    evenly divisible by all of the numbers from 1 to 20?
*/
bool divisible(int m, int x){
    for(int i = x; i > 1; i--){
        if(m%i) return false;
    }
    return true;
}

int sMult(int x){
    int start = x*(x-1);
    while(!divisible(start, x)){
        start+=2;
    }
    return start;
}

int main(){
    int x;
    cin >> x;
    cout << sMult(x) << endl;
    return 0;
}
