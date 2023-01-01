class Solution:
    def confusingNumber(self, n: int) -> bool:
        l = []
        ns = str(n)
        for d in ns:
            if d in ["0", "1", "8"]:
                l.append(d)
            elif d in ["2", "3", "4", "5", "7"]:
                return False
            elif d == '6':
                l.append("9")
            else:
                l.append("6")
        return "".join(l[::-1]) != ns
