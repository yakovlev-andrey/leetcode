# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if 0 <= x <= 9:
            return True
        if x < 0 or x % 10 == 0:
            return False

        x = str(x)
        for i in range(len(x) // 2 + 1):
            if x[i-1] != x[-i]:
                return False
        return True


s = Solution()

assert not s.isPalindrome(1000030001)
assert not s.isPalindrome(123456)
assert s.isPalindrome(121)
assert not s.isPalindrome(-121)
assert not s.isPalindrome(10)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if 0 <= x <= 9:
            return True
        if x < 0 or x % 10 == 0:
            return False

        reversed_x = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_x = reversed_x * 10 + digit
            temp //= 10

        return reversed_x == x


s = Solution()

assert not s.isPalindrome(1000030001)
assert not s.isPalindrome(123456)
assert s.isPalindrome(121)
assert not s.isPalindrome(-121)
assert not s.isPalindrome(10)