class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # simplest way --> take 1st number from nums ; subtract the target and then binary search .
        # better way --> thinking abt it ....  It might be related to how v get 1st and last pos of target using BS . 

        # imp pts : for bigger Array BS is good but v can do better 

        for i in range(len(numbers)-1):
            t2 = target - numbers[i]
            ans=-1
            low=0
            high=len(numbers)-1
            while(low<=high):
                mid=(low+high)//2
                if t2==numbers[mid] and mid != i:
                    return [i+1 , mid+1]
                elif(t2>=numbers[mid]):
                    low=mid+1
                else:
                    high=mid-1 

        # this will fail so i won't submit
        # imp : two numbers index1 and index2, each incremented by one

        # think !!
        # logic --> pointers move close when sum > target ; else move away
        # 1st go to mid ; if 2xmid > target --> 0 to mid-1 itrates while right side is BS from mid to last 
        # how to add 2 bs ? 