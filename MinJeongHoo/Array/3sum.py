class Solution(object):
    def threeSum(self, nums):
        ans,n = [], len(nums)        
        nums.sort()

        for i in range(n) :
            ## 값이 같을때 스킵(다음 값으로 스킵)
            if i > 0 and nums[i] == nums[i-1] :
                continue

            # 범위 지정해서 탐색
            l, r = i+1, n-1

            while l < r :
                s = nums[i] + nums[l] + nums[r]
                if s < 0 :
                    l += 1
                elif s > 0 :
                    r -= 1
                else :
                    # 탐색 완료
                    ans.append([nums[l],nums[i],nums[r]])
                    ## 배열에 중복되게 들어가는 것을 막아주기 위해서 같은 다음 값과 같을때 l 혹은 r 값을 한번 더 움직여 준다.
                    while l < n-1 and nums[l] == nums[l+1] :
                        l += 1
                    while r > 1 and nums[r] == nums[r-1] :
                        r -= 1
                    l += 1
                    r -= 1

        return ans
## 투포인터 전략을 사용한다. 