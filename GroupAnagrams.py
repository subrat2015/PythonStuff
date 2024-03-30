from collections import defaultdict

class GroupAnagram:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        return list(anagram_map.values())


obj = GroupAnagram()
strs = ["eat","tea","tan","ate","nat","bat"]
result = obj.groupAnagrams(strs)
print(result)