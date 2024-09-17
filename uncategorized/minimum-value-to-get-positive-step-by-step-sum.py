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


assert s.minStartValue([-3, 2, -3 ,4 , 2]) == 5
assert s.minStartValue([1, 2]) == 1
assert s.minStartValue([1, -2, -3]) == 5
