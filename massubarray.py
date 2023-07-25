class Solution:
    def maxSubArray(self, nums):
        maxsub = nums[0]
        cursum = 0

        for n in nums:
            if cursum < 0:
                cursum = 0
            cursum +=n
            maxsub = max(maxsub, cursum)
        return maxsub
    
obj = Solution()
print(obj.maxSubArray([1,2,-3,4,-1,-2,3,4]))