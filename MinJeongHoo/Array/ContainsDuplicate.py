from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for i in nums:
            if counter[i]>1:
                return True
        return False
## counter class를 사용해서 각 값들의 갯수를 구한후 루프를 돌면서 값중에 2개이상이 있을경우 True 아니면 False return
