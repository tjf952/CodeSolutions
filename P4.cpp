#include <iostream>
#include <math.h>
#include <string>

using namespace std;

/*
    Find the largest palindrome made 
    from the product of two 3-digit numbers.
*/

bool palindrome(int x){
    string s = to_string(x);
    int cen = s.length()/2;
    for(int i = 0; i < cen; i++) if(s[i] != s[s.length()-1-i]) return false;
    return true;
}

int max3_b(){
    int max = 0;
    for(int i = 0; i < 1000; i++){
        for(int j = i; j < 1000; j++){
            if(palindrome(i*j) && i*j > max) max = i*j;
        }
    }
    return max;
}

int main(){
    cout << max3_b() << endl;
    return 0;
}
