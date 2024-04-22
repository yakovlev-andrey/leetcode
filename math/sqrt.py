# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        answer = x
        while answer * answer > x:
            answer = (answer + x // answer) // 2
        return answer
