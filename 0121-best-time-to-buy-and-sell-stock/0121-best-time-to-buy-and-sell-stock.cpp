class Solution {
public:
    int maxProfit(vector<int>& prices) {
     int ans = 0;
     int diff = 0;
     int max = prices[0];
     int min = prices[0];
     for (int val=0; val < prices.size(); val++){
        if(prices[val] >= max){
            max = prices[val];
        }
        else if(prices[val] <= min ){
            min = prices[val];
            max = prices[val];
        }
        diff = max - min;
        if (diff > ans){
            ans = diff;
        }
     }
     return ans;
    }
};