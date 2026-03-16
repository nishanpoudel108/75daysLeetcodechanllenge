class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in anagram_map:
                anagram_map[key] = []

            anagram_map[key].append(word)

        return anagram_map.values()