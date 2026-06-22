class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in pairs.values():  # opening bracket
                stack.append(char)
            else:  # closing bracket
                if not stack or stack.pop() != pairs[char]:
                    return False

        return len(stack) == 0
        