import collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:        
        cnt = collections.defaultdict(int)
        i = 0
        res = 0
        for j in range(len(s)):
            cnt[s[j]] += 1
            while j - i + 1 - max(cnt.values()) > k:
                cnt[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res