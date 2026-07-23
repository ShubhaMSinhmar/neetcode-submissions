from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = defaultdict(list)
        result = []

        for word in strs:
            sorted_word = tuple(sorted(word))
            anagram_list[sorted_word].append(word)

        for value in anagram_list.values():
            result.append(value)

        return result