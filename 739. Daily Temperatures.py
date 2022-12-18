class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<t:
                p = stack.pop()
                answer[p] = i-p
            stack.append(i)
        return answer
