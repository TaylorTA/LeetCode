class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        topn = nsmallest(k, count.keys(), key = lambda x:(-count[x],x))
        return topn
