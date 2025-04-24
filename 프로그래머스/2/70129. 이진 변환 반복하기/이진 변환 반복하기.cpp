#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    
    int count_transform = 0;
    int count_zero = 0;
    
    while(s != "1"){
        
        count_transform += 1;
        
        // x의 모든 0을 제거
        count_zero += count(s.begin(), s.end(), '0');
        s.erase(remove(s.begin(), s.end(), '0'), s.end());
        
        // x의 길이를 c라고 한다면, x를 "c를 2진법으로 표현한 문자열"로 바꿈
        int c = s.length();
        s = "";
        while(c > 0){
            s = to_string(c%2) + s;
            c /= 2;
        }
        
    }
    
    answer.push_back(count_transform);
    answer.push_back(count_zero);
    
    return answer;
}