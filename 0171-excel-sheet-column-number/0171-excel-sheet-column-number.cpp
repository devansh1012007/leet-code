#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
class Solution {
public:
    /*
    int titleToNumber(string columnTitle) {
        std::reverse(columnTitle.begin(), columnTitle.end());
        std::unordered_map<std::char, int> hashMap;
        std::vector<std::string> alphas = {"A", "B", "C", "D", "E", "F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"};
        for(int j = 0; j < alphas.size(); j++){
            hashMap.insert({alphas[j], j+1});
        }
        int sum = 0;
        for(int i =0 ; i< columnTitle.size(); i++){
            sum = sum + hashMap[columnTitle[i]]*26^i;
        }
        return sum;
    }*/
    int titleToNumber(std::string columnTitle) {
        int result = 0;
        for (char c : columnTitle) {
            result = result * 26 + (c - 'A' + 1);
        }
        return result;
    }
};