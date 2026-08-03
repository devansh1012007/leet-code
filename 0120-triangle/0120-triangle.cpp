#include <vector>
#include <algorithm>
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        std::vector<int> DP = {};
        int length = triangle.size();
        for (int row = 0; row <length; row++){
            std::vector<int> new_DP = {};
            int length_row = triangle[row].size();
            if (length_row > 1){
                new_DP.push_back(triangle[row][0]+DP[0]);
                for (int i=1;i < (length_row-1); i++){
                    new_DP.push_back(triangle[row][i] + std::min(DP[i], DP[i-1]));
                }
                new_DP.push_back(triangle[row].back() + DP.back());
            }
            else{
                new_DP.push_back(triangle[row].back());
            }
            DP = std::move(new_DP);
        }
        return *std::min_element(DP.begin(), DP.end());
    }
};