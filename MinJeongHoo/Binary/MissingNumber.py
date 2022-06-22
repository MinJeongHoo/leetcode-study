class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        startNum = 0
        nums.sort()
        for i in nums:
            if i != startNum:
                return startNum
            startNum+=1
        return startNum