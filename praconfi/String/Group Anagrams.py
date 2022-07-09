import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # 초기값을 []로 같는 dict를 생성한다
        anagrams = collections.defaultdict(list)

        # sort메서드로 정렬된값을 key로, 원래값을 value로 삽입한다
        for item in strs:
            anagrams[''.join(sorted(item))].append(item)
        # values()를 통해 리스트들을 리턴한다
        return anagrams.values()