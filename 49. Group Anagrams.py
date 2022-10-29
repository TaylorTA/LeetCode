class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for w in strs:
            dic[tuple(sorted(w))].append(w)
        return dic.values()
