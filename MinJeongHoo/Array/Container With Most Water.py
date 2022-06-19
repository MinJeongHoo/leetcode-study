class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
        return maxarea
## 투포인터로 접근 해본다. 조건은 left right중 높이 값이 작은값과 넓이 값을 곱한 후 현재 maxarea와 비교하는 방법으로 구현