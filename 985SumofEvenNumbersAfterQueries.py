class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = [0] * len(queries)
        evenSum = 0
        for num in nums:
            if num%2 == 0:
                evenSum += num
        
        answerI = 0
        for val, index in queries:
            og = nums[index]
            if og%2 == 0:
                evenSum -= og
            og += val
            if og%2 == 0:
                evenSum += og
            nums[index] = og
            answer[answerI] = evenSum
            answerI += 1
        
        return answer
