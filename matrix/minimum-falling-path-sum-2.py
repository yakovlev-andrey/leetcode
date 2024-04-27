# https://leetcode.com/problems/minimum-falling-path-sum-ii/description/?envType=daily-question&envId=2024-04-26

class Solution:
    """ O(n^3) """
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        length = len(grid)
        dp = grid[0]

        for r in range(1, length):
            next_dp = [float("inf")] * length
            for curr_col in range(length):
                for prev_col in range(length):
                    if curr_col != prev_col:
                        next_dp[curr_col] = min(
                            next_dp[curr_col],
                            grid[r][curr_col] + dp[prev_col]
                        )
            dp = next_dp
        return min(dp)


s = Solution()

assert s.minFallingPathSum(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 13
assert s.minFallingPathSum(grid=[[7]]) == 7


class Solution:
    """ O(n^2) """
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        def get_min_two(row: list[int]):
            min_two = []
            for value, index in row:
                if len(min_two) < 2:
                    min_two.append((value, index))
                elif min_two[1][0] > value:
                    min_two.pop()
                    min_two.append((value, index))
                min_two.sort()
            return min_two

        length = len(grid)
        first_row = [(value, index) for index, value in enumerate(grid[0])]
        dp = get_min_two(first_row)
        for r in range(1, length):
            next_dp = []
            for curr_col in range(length):
                curr_value = grid[r][curr_col]
                min_value = float("inf")
                for prev_value, prev_col in dp:
                    if curr_col != prev_col:
                        min_value = min(min_value, curr_value + prev_value)
                next_dp.append((min_value, curr_col))
                next_dp = get_min_two(next_dp)
            dp = next_dp
        return min([value for value, _ in dp])


s = Solution()

assert s.minFallingPathSum(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 13
assert s.minFallingPathSum(grid=[[7]]) == 7
