from typing import List

# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try:
                return [i, nums.index(target - nums[i], i+1, len(nums))]
            except ValueError:
                continue


s = Solution()

assert s.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
assert s.twoSum(nums=[3, 2, 4], target=6) == [1, 2]
assert s.twoSum(nums=[3, 3], target=6) == [0, 1]
