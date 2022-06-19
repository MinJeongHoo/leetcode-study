class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        
        for i in range(1,len(nums)):
            curr = nums[i]
            temp_max = max(curr,max_so_far*curr,min_so_far*curr)
            min_so_far = min(curr,max_so_far*curr,min_so_far*curr)
            
            max_so_far = temp_max
            
            result = max(max_so_far,result)
        return result
## 0을 곱할 경우 -를 곱할 경우의 두가지 상황을 고려해야한다. 완전탐색은 시간복잡도를 초과하기 때문에
## DP를 이용해서 풀이가 가능하다.
## max와 min은 index 0 번째 값에서 출발한다.
## 반복적으로 최소값과 최대값을 구해나가면서 마지막 result값과 비교