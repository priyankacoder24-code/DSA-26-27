class Solution:
    def isValid(self, s: str) -> bool:
        alltypes = {"]":"[" , "}" : "{" , ")" : "("}
        stack = []

        for c in s:
            if stack and c in alltypes and stack[-1] == alltypes[c]:
                stack.pop()
            else:
                stack.append(c)
        return True if len(stack)==0 else False
        