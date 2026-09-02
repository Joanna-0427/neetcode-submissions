class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []


        def dfs(start):
            if start == len(s):
                res.append(path[:])
                return
            
            #不同切割方式:
            #1.[start:i+1]a1[i+1:i+1+1]a2;[start:i+1]a1[i+1:i+1+2]a2b
            #2.[start:i+2]a1a2[i+2:i+2+1]b;[start:i+2][i+2:i+2+2]
                
            #如果[start:i+1]不是palindromic，这种切割方式直接跳过，这一层有一个不是palindrome，其他是也不行；
            #从[start:i+2]尝试
            for i in range(start,len(s)):
                #可以允许重复，因为是不同的切割 [a a a][a aa][aa a][aaa]不同切割方案
                
                if self.is_palindromic(s[start:i+1]):
                    path.append(s[start:i+1])
                    dfs(i+1)
                    path.pop()
                
                

        dfs(0)
        return res



    def is_palindromic(self,x):
        i, j = 0, len(x)-1
        while i < j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True


        