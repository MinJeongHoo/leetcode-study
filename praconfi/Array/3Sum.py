class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sum_dict에 nums의 값을 value: index 형식으로 추가한다
        # nums를 이중for문으로 순환하며 i와 j의 값을 선정하고 sum_dict와 비교한다
        # sum_dict의 key값중 더해서 0이되는 경우 index값을 하나의 배열로 합친다
    
        
        sum_dict = defaultdict(list)
        result_arr = []
        for i, num in enumerate(nums):
            sum_dict[num].append(i)

        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)-1):
                if -(nums[i] + nums[j]) in sum_dict:
                    sum_dict[-(nums[i] + nums[j])].append(nums[j])
                    sum_dict[-(nums[i] + nums[j])].append(nums[i])
                    result_arr.append(sum_dict[-(nums[i] + nums[j])])

        return result_arr
