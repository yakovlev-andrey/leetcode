from itertools import accumulate
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_value = nums[0]
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if nums[i] < min_value:
                min_value = nums[i]
        return 1 if 1 - min_value < 1 else 1 - min_value


s = Solution()

assert s.minStartValue([-3, 2, -3, 4, 2]) == 5
assert s.minStartValue([1, 2]) == 1
assert s.minStartValue([1, -2, -3]) == 5 


class Solution:
    def minStartValue(self, nums):
        cur_sum, min_sum = 0, 0
        for num in nums:
            cur_sum += num
            min_sum = min(min_sum, cur_sum)
        return 1 - min_sum


s = Solution()

assert s.minStartValue([-3, 2, -3, 4, 2]) == 5
assert s.minStartValue([1, 2]) == 1
assert s.minStartValue([1, -2, -3]) == 5 


class Solution:
    def minStartValue(self, nums):
        return max(1, 1 - min(accumulate(nums)))


s = Solution()

assert s.minStartValue([-3, 2, -3, 4, 2]) == 5
assert s.minStartValue([1, 2]) == 1
assert s.minStartValue([1, -2, -3]) == 5
