class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        topn = nsmallest(k, count.keys(), key = lambda x:(-count[x],x))
        return topn

from sortedcontainers import SortedList    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        sl = SortedList(key=lambda pair: (-pair[0], pair[1]))
        for w in c:
            sl.add((c[w], w))
        return [sl[i][1] for i in range(k)]
