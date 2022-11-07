class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)

        for i, d in enumerate(num):
            if d == '6':
                num = num[:i] + '9' + num[i+1:]
                break
        
        return int(num)
