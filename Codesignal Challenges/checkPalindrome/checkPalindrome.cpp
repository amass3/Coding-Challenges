#include <cstring>
#include <iostream>
using namespace std; 

bool solution(string inputString) {
    
    string reversed_input = "";
    int start = 0;
    int end = inputString.length() -1;
    
    while(start <= end){
        if (inputString[start]!= inputString[end]) {
            return false;
        }
        start++;
        end--;
    }       
    
    return true;

}
