class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i],i))
            elif stack[-1][0] >= temperatures[i]:
                stack.append((temperatures[i],i))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    index = stack.pop()[1]
                    final[index] = i - index
            stack.append((temperatures[i],i))
        return final




            
        