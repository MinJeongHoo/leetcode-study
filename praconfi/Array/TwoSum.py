class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # new_dict[값] = 인덱스값 으로 딕셔너리를 만든다
        # 요소를 순회하며 target - 현재요소값이 있는지 확인하고,
        # 없다면 key, value로 저장하고
        # 있다면 각각 인덱스값을 반환한다
    
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [i, num_dict[target - num]]
            num_dict[num] = i   