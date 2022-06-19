

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxResult = nums[0]
        currMax = 1
        
        for num in nums:
            if num == 0:
                currMax = 1
                continue
            currMax *= num
            
            maxResult = max(maxResult, currMax)
            
        return maxResult
