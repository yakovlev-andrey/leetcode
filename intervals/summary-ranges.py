# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        ranges = []
        start = end = None
        for num in nums:
            if start is None:
                start = end = num
                continue
            if num - 1 == end:
                end = num
                continue
            else:
                if end == start:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{end}")
                start = end = num
        if end == start:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}->{end}")
        return ranges


s = Solution()

assert s.summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
assert s.summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
assert s.summaryRanges([0]) == ["0"]
assert s.summaryRanges([0, 1]) == ["0->1"]
assert s.summaryRanges([0, 2, 4, 7]) == ["0", "2", "4", "7"]
assert s.summaryRanges([0]) == ["0"]


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ranges = []  # [start, end] or [x, y]
        for n in nums:
            if ranges and ranges[-1][1] == n-1:
                ranges[-1][1] = n
            else:
                ranges.append([n, n])

        return [f"{x}->{y}" if x != y else f"{x}" for x, y in ranges]


s = Solution()

assert s.summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
assert s.summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
assert s.summaryRanges([0]) == ["0"]
assert s.summaryRanges([0, 1]) == ["0->1"]
assert s.summaryRanges([0, 2, 4, 7]) == ["0", "2", "4", "7"]
assert s.summaryRanges([0]) == ["0"]