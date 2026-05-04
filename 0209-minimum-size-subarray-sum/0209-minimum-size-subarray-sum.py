class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # reattempt later
        min_len = float("inf")
        left = 0
        cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                cur_sum -= nums[left]
                left += 1
        
        return min_len if min_len != float("inf") else 0                
            # simple approch-> just sort it and then use for loop [O(n log(n))]
            # my approch -> find max, pop max; till u run out of array or find ur solution
            # Imp point -> q is askin us to find answer with complexity O(n) but BS has complexity of O(log n); i am not sure how v will us BS coz arr is not sorted
            # my approch is wrong coz it not sliding window
            # better approch -> Sliding Window and Prefix Sum BS
