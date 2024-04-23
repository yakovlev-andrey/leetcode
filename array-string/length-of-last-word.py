class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        word_start = False
        for i in range(1, len(s)+1):
            if s[-i] != " ":
                word_start = True
                length += 1
            else:
                if word_start:
                    break
        return length


s = Solution()

assert s.lengthOfLastWord("aa aaa") == 3, f"{s.lengthOfLastWord("aa aaa")} != 3"
assert s.lengthOfLastWord("aa aaa  ") == 3
assert s.lengthOfLastWord("aaaa") == 4
assert s.lengthOfLastWord("aa aaa           ") == 3
assert s.lengthOfLastWord("a") == 1
assert s.lengthOfLastWord(" a") == 1


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])


s = Solution()

assert s.lengthOfLastWord("aa aaa") == 3, f"{s.lengthOfLastWord("aa aaa")} != 3"
assert s.lengthOfLastWord("aa aaa  ") == 3
assert s.lengthOfLastWord("aaaa") == 4
assert s.lengthOfLastWord("aa aaa           ") == 3
assert s.lengthOfLastWord("a") == 1
assert s.lengthOfLastWord(" a") == 1