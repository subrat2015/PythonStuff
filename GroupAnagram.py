from collections import defaultdict
class GroupAnagram:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        return list(anagram_map.values())


groupAnagram = GroupAnagram()
#var = list[list[str]]
output = groupAnagram.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(output)
