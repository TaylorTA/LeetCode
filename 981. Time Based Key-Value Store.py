from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.dic = defaultdict(SortedDict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        op = ""
        if key in self.dic:
            pos = self.dic[key].bisect_right(timestamp)-1
            if pos == -1:
                return op
            op = self.dic[key][self.dic[key].keys()[pos]]
        
        return op
