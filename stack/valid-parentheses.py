# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []
        parentheses_dict = {"}": "{", ")": "(", "]": "["}
        for ch in s:
            if ch in parentheses_dict.values():
                parentheses.append(ch)
            elif not parentheses:
                return False
            elif parentheses.pop() != parentheses_dict[ch]:
                return False
        return True if not parentheses else False


s = Solution()

assert s.isValid("()")
assert s.isValid("()[]{}")
assert not s.isValid("(]")
assert not s.isValid("{")
assert not s.isValid("}")
