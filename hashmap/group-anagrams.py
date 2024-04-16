from collections import defaultdict

# https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 1:
            return [strs]
        result = defaultdict(list)
        for s in strs:
            result[''.join(sorted(s))].append(s)
        return list(result.values())


sol = Solution()

print(f"{sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])} \n"
      f"{[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]}")
