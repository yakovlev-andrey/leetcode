from collections import Counter, defaultdict

# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_dict = defaultdict(int)
        for letter in s:
            letters_dict[letter] += 1
        for letter in t:
            letters_dict[letter] -= 1
        for letter_count in letters_dict.values():
            if letter_count != 0:
                return False
        return True


s = Solution()

assert s.isAnagram("anagram", "nagaram")
assert not s.isAnagram("rat", "car")


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


s = Solution()

assert s.isAnagram("anagram", "nagaram")
assert not s.isAnagram("rat", "car")
