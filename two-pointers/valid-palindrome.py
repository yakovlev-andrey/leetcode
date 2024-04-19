# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start_index = 0
        end_index = len(s) - 1
        while start_index < end_index:
            while not s[start_index].isalnum() and start_index < end_index:
                start_index += 1
            while not s[end_index].isalnum() and start_index < end_index:
                end_index -= 1
            if s[start_index].lower() == s[end_index].lower():
                start_index += 1
                end_index -= 1
            else:
                return False
        return True

s = Solution()

assert s.isPalindrome("A man, a plan, a canal: Panama")
assert not s.isPalindrome("race a car")
assert s.isPalindrome("ada")
assert s.isPalindrome(" ")
assert s.isPalindrome("0P")
