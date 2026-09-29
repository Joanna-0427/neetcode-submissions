class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        mapping = []
        for p, s in zip(position,speed):
            mapping.append((p,s))
        mapping.sort(key=lambda x:x[0]) #升序

        stack = []
        total = 1
        for j in range(n-1,-1,-1):
            time = (target - mapping[j][0]) / mapping[j][1]
            if stack and stack[-1] >= time:
                continue
            
            if stack and stack[-1] < time:
                total += 1
            
            stack.append(time)
        
        return total


