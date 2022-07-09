import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 필요한 값과, 개수를 key, value로 저장해둔다
        # need = Counter({'A': 2, 'B': 1, 'C': 1})
        need = collections.Counter(t)
        missing = len(t)

        left = start = end = 0

        # 오른쪽 포인터 이동
        # 1부터 시작(slice값에는 마지막 값이 포함되지 않기때문)          
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            # 필요한 문자가 0개가 되면 왼쪽포인터를 오른쪽으로 이동
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if end == 0 or right - left <= end - start:
                    # 최소길이 저장후, 왼쪽포인터 한칸이동                     
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1
                    # 이후 상위 for문으로 이동

        return s[start: end]