class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

## solution
## 이 문제는 완전 탐색으로도 풀 수 있지만, hashmap을 이용해서도 풀이가 가능하다
## for문 돌면서 target에 차를 구한다. hashmap에 없으면 hashmap에 {키 숫자 : value 인덱스} 를 넣어주고
## 있으면 i 깂과 value(index)를 리턴해준다.