class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c:[] for w in words for c in w}
        n = len(words)
        for i in range(n-1):
            w1, w2 = words[i],words[i+1]
            p = 0
            while p < len(w1) and p < len(w2) and w1[p] == w2[p]:
                p += 1
            if p == len(w2) and len(w1) > len(w2):
                return ''
            if p == len(w1):
                continue
            graph[w1[p]].append(w2[p])
        
        visited = set() #已符合条件的完成
        cycle = set() #正在路径上
        res = []
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for ni in graph[node]:
                if not dfs(ni):return False

            cycle.remove(node)
            visited.add(node)
            res.append(node)
            return True
        
        for c in graph: #读取c，如果c不在graph里，defaultdict会自动创建c键，遍历中突然多出，会导致报错
            if not dfs(c): return ''
        return ''.join(res[::-1])
            
