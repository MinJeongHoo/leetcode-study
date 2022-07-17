class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
## 투포인터로 해결을 할 수 있다. 혹시나 숫자,문자를 제외한 다른 것들이 있는지 체크한 다음 현재 가리키고 있는 i j 가 같으면 계속 진행하고 같지 않다면 False로 리턴