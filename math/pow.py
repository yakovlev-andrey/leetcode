# https://leetcode.com/problems/powx-n/submissions/1421744270/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x: float, n: int):
            if x == 0:
                return 0
            if n == 0:
                return 1
            powed = pow(x * x, n // 2)
            return powed * x if n % 2 == 1 else powed

        result = pow(x, abs(n))
        return result if n >= 0 else 1 / result


s = Solution()

assert (res := s.myPow(2, 2)) == (exp := pow(2, 2)), f"{res} != {exp}"
assert (res := s.myPow(2, -2)) == (exp := pow(2, -2)), f"{res} != {exp}"
assert (res := s.myPow(2, 10)) == (exp := pow(2, 10)), f"{res} != {exp}"
assert (res := s.myPow(2.00000, 10)) == (exp := pow(2.00000, 10)), f"{res} != {exp}"
