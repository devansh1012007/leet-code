class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int hi = nums.size()-1;
        int lo = 0;
        while(hi > lo){
            int mid = lo + (hi - lo)/2;
            if (nums[mid] > nums[mid+1]){
                hi = mid;
            }
            else{lo = mid+1;}
        }
        return lo;
        }
};