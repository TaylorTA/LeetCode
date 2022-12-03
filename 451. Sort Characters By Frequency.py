class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(c * t for c,t in Counter(s).most_common())
