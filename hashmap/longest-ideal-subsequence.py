# https://leetcode.com/problems/longest-ideal-subsequence/?envType=daily-question&envId=2024-04-25

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        chars = [0] * 26
        a = ord('a')
        for c in s:
            i = ord(c) - a
            left = 0 if i - k < 0 else i - k
            right = 26 if i + k + 1 > 26 else i + k + 1
            chars[i] = max(chars[left:right]) + 1
        return max(chars)


s = Solution()

assert s.longestIdealString(s="acfgbd", k=2) == 4
assert s.longestIdealString(s="abcd", k=3) == 4
assert s.longestIdealString(s="pvjcci", k=4) == 2
assert s.longestIdealString(s="zjhngjkfv", k=25) == 9
