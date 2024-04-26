# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        start_h = None
        current_water = 0
        for h in height:
            if start_h is None:
                start_h = h
                continue

            if start_h > h:
                current_water += start_h - h

            if start_h

            water += current_water



s = Solution()

assert s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6