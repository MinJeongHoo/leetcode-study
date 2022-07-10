class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i =='[' or i == '{':
                stack.append(i)
            elif len(stack) == 0 and (i ==')' or i ==']' or i=='}'):
                return False
            elif len(stack)>0 and i ==')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif len(stack)>0 and i ==']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif len(stack)>0 and i =='}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if len(stack)>0:
            return False
        return True