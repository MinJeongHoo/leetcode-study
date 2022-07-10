class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        mp = {}

        i = 0
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         chars = [0] * 128

#         left = right = 0

#         res = 0
#         while right < len(s):
#             r = s[right]
#             chars[ord(r)] += 1

#             while chars[ord(r)] > 1:
#                 l = s[left]
#                 chars[ord(l)] -= 1
#                 left += 1

#             res = max(res, right - left + 1)

#             right += 1
#         return res