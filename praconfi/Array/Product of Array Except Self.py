
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_arr = []
        for i, num in enumerate(nums):
            # 현재 요소를 제외한 배열을 만든후
            except_arr = nums[:i] + nums[i+1:]
            
            # 배열의 모든값을 곱한다
            result_arr[i] = reduce(lambda x, y: x * y, except_arr)

        return result_arr