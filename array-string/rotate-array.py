# https://leetcode.com/problems/rotate-array/


class Solution:
    def rotate(self, nums: list[int], k: int) -> list[int]:
        if k > len(nums):
            k = k % len(nums)
        nums = nums[-k:] + nums[:-k]
        return nums


s = Solution()

assert s.rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
assert s.rotate([1, 2, 3, 4, 5, 6, 7], 10) == [5, 6, 7, 1, 2, 3, 4]
assert s.rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]


class Solution:
    def rotate(self, nums: list[int], k: int) -> list[int]:
        if k > len(nums):
            k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        return nums


s = Solution()
assert s.rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
assert s.rotate([1, 2, 3, 4, 5, 6, 7], 10) == [5, 6, 7, 1, 2, 3, 4]
assert s.rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
