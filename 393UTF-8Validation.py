class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        if len(data) == 0:
            return False
        
        numBytes = 0
        
        for num in data:
            # print(num)
            # print(numBytes)
            if numBytes == 0:
                mask = 1 << 7
                while mask & num:
                    numBytes +=1
                    mask = mask >> 1
                
                
                if numBytes == 1 or numBytes > 4:
                    return False
                if numBytes == 0:
                    continue
                    
                numBytes -= 1
            else:
                if not(num & (1 << 7) and not num & (1 << 6)):
                    return False
                
                numBytes -= 1
            
            # print(numBytes)
            
            
        if numBytes == 0:
            return True
        else:
            return False
