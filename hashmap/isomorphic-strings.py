# https://leetcode.com/problems/isomorphic-strings/

# https://leetcode.com/problems/isomorphic-strings/solutions/4962460/one-line-solution/ - nice solutions

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        word_map = [{}, {}]
        for i in range(len(s)):
            if s[i] not in word_map[0]:
                word_map[0][s[i]] = t[i]
            elif word_map[0][s[i]] != t[i]:
                return False

            if t[i] not in word_map[1]:
                word_map[1][t[i]] = s[i]
            elif word_map[1][t[i]] != s[i]:
                return False
        return True


s = Solution()

assert s.isIsomorphic(s="egg", t="add")
assert not s.isIsomorphic(s="foo", t="bar")
assert s.isIsomorphic(s="paper", t="title")
assert not s.isIsomorphic(s="badc", t="baba")


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


s = Solution()

assert s.isIsomorphic(s="egg", t="add")
assert not s.isIsomorphic(s="foo", t="bar")
assert s.isIsomorphic(s="paper", t="title")
assert not s.isIsomorphic(s="badc", t="baba")
