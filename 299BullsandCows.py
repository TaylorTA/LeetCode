class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hashmap = {}
        dic = {}
        for i, v in enumerate(secret):
            if v not in hashmap:
                hashmap[v] = set([i])
            else:
                hashmap[v].add(i)
        for i, v in enumerate(guess):
            if v not in dic:
                dic[v] = set([i])
            else:
                dic[v].add(i)
        
        bulls = 0
        cows = 0
        for i, v in enumerate(guess):
            if v in hashmap and i in hashmap[v]:
                bulls += 1
                hashmap[v].remove(i)
                if len(hashmap[v]) == 0:
                    hashmap.pop(v)
                dic[v].remove(i)
                if len(dic[v]) == 0:
                    dic.pop(v)
        for v in dic:
            for i in dic[v]:
                if v in hashmap:
                    cows += 1
                    hashmap[v].pop()
                    if len(hashmap[v]) == 0:
                        hashmap.pop(v)
        
        return str(bulls) + "A" + str(cows) + "B"
