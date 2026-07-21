class Solution {
public:
    int climbStairsRecur(int n, vector<int>& arr){
        if (n == 1 || n == 0)
            return 1;
        if (arr[n] != -1)
            return arr[n];
        arr[n]= climbStairsRecur(n-1 , arr) + climbStairsRecur(n-2, arr);
        return arr[n];
    }
    int climbStairs(int n) {
        vector<int>arr(n+1, -1);
        return climbStairsRecur(n, arr);
    }
};