from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index


s = Solution()

nums = [3, 2, 2, 3]
assert (n := s.removeElement(nums, 3)) == 2, f"{n} != 2"
assert nums[:2] == [2, 2]

nums = [0, 1, 2, 2, 3, 0, 4, 2]
assert (n := s.removeElement(nums, 2)) == 5, f"{n} != 5"
assert nums[:5] == [0, 1, 3, 0, 4]
