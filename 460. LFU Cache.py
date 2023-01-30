class LFUCache:

    def __init__(self, capacity: int):
        self.ht = {}
        self.fre = defaultdict(dict)
        self.mc = capacity
        self.mf = 0
        

    def get(self, key: int) -> int:
        if key not in self.ht:
            return -1
        else:
            pair = self.ht[key]
            self.ht[key] = [pair[0], pair[1]+1]
            self.fre[pair[1]].pop(key)
            self.fre[pair[1]+1][key] = 0
            if not self.fre[self.mf]:
                self.mf += 1
            return pair[0]
        

    def put(self, key: int, value: int) -> None:
        # print(self.ht)
        # print(self.fre)
        # print(key)
        if self.mc == 0:
            return
        if key in self.ht:
            pair = self.ht[key]
            pair[0] = value
            self.ht[key] = pair
            self.get(key)
            return
        if self.mc == len(self.ht):
            k = next(iter(self.fre[self.mf]))
            self.fre[self.mf].pop(k)
            self.ht.pop(k)
            # print("key")
            # print(k)
        self.mf = 1
        self.ht[key] = [value, 1]
        self.fre[1][key] = 0
        

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
