## mySolution

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def getSubMax(start,end):
            if start>=end:
                return nums[start]
            else:
                mid = (start+end)//2
                left = getSubMax(start,mid)
                right = getSubMax(mid+1,end)
                leftSum = 0
                leftMax= -98394829
                for i in range(mid,start-1,-1):
                    leftSum += nums[i]
                    leftMax = max(leftMax,leftSum)
                rightSum = 0
                rightMax = -98394829
                for i in range(mid+1,end+1):
                    rightSum+=nums[i]
                    rightMax = max(rightMax,rightSum)
                myMax = leftMax+rightMax
                return max(left,right,myMax)
        return getSubMax(0,len(nums)-1)
## 분할 정복으로 재귀를 통해서 왼쪽의 최대값 오른쪽의 최대값 그리고 합쳐진 최대값 중 가장 큰 최대값을 리턴 시킨다.

## solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            if left > right:
                return -math.inf
            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)
            return max(best_combined_sum, left_half, right_half)
        return findBestSubarray(nums, 0, len(nums) - 1)

