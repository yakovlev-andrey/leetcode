# https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(1, len(digits) + 1):
            digits[-i] += 1
            if digits[-i] == 10:
                digits[-i] = 0
            else:
                break
        if digits[0] == 0:
            return [1] + digits
        return digits


s = Solution()

assert s.plusOne([9]) == [1, 0]
assert s.plusOne([9, 9, 9]) == [1, 0, 0, 0]
assert s.plusOne([1, 2, 3]) == [1, 2, 4]
assert s.plusOne([1, 9, 8]) == [1, 9, 9]
