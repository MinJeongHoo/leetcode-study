class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letterDict = collections.defaultdict(int)

        s_arr = list(s)
        t_arr = list(t)

        for letter in s_arr:
            letterDict[letter] += 1

        for letter in t_arr:
            if letterDict[letter] == 1:
                del letterDict[letter]
            else:
                letterDict[letter] -= 1

        return True if letterDict == {} else False