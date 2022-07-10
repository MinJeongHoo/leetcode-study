class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # without repeating이기 때문에 set을 활용해 중복 방지
        char_set = set()
        left = result = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # 인덱스를 순회하며 char을 모으고, max length를 갱신한다
            # 중복되는 단어가 나오면, 중복이 해결될때까지 왼쪽의 char를 지워나간다
            char_set.add(s[right])

            # 0번째 인덱스도 길이는 1이기 때문에, 포인터 차이에 1을 더해준다
            result = max(result, right - left + 1)

        return result