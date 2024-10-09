# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

bad_version = float('inf')


def isBadVersion(version: int) -> bool:
    global bad_version
    if version >= bad_version:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        while start < end:
            middle = start + (end - start) // 2
            if isBadVersion(middle):
                end = middle
            else:
                start = middle + 1
        return start


s = Solution()

for n in range(10):
    for bv in range(1, n+1):
        bad_version = bv
        print(f"n = {n}, bad_version = {bad_version}")
        first_bad = s.firstBadVersion(n)
        assert first_bad == bad_version, f"{first_bad} != {bad_version}"
