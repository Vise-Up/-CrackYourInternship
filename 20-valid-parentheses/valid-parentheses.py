class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapped = {'}':"{",')':'(',']':'['}
        for i in s:
            if i in mapped:
                if stack and stack[-1] == mapped[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
            

