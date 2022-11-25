class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        s = 0

        for i in range(len(arr)+1):
            # print(i==len(arr))
            # print(stack)
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                # print(mid)
                # print(stack)
                # print(i)
                s += arr[mid] * (mid-left) * (right-mid) 
            stack.append(i)
        
        return s % (10**9+7)
