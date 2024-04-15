from collections import Counter

# https://leetcode.com/problems/ransom-note/


class Solution:  # first attempt
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        try:
            for letter in ransomNote:
                magazine.remove(letter)
        except ValueError:
            return False
        return True


s = Solution()

assert not s.canConstruct('a', 'b')
assert not s.canConstruct('aa', 'ab')
assert s.canConstruct('aa', 'aab')


class Solution:  # https://docs.python.org/3/library/collections.html#collections.Counter
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_note, counter_magazine = Counter(ransomNote), Counter(magazine)
        return counter_note & counter_magazine == counter_note


s = Solution()

assert not s.canConstruct('a', 'b')
assert not s.canConstruct('aa', 'ab')
assert s.canConstruct('aa', 'aab')
