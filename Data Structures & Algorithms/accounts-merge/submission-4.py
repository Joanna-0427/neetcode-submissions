class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #找连通块，find，有共同根则是同一个连通块
        #相同连通块合并

        parent = {}
        owner = {}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a in accounts:
            name = a[0]
            for email in a[1:]:
                if email not in parent: #新邮箱，根是自己
                    parent[email] = email
                owner[email] = name
            
            #每一组邮箱，根都统一
            root = find(a[1])
            for c in a[2:]:
                parent[find(c)] = root
        
        groups = defaultdict(list)
        for e in parent:
            groups[find(e)].append(e)
        
        res = []
        for k, em in groups.items():
            res.append([owner[k]] + sorted(em))
        return res

