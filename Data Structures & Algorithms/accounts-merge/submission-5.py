class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        owner = {}
        #每个邮箱先创建自己为根
        #每个账号挂到第一个的根上
        
        #检查邮箱重复出现，根是否相同，挂在一起；
        #同样根的邮箱合并，并加上名字；
        def find(a):
            while parent[a] != a:
                a = parent[a]
            return parent[a]


        for account in accounts:
            name = account[0]
            for acc in account[1:]:
                if acc not in parent:
                    parent[acc] = acc
                    owner[acc] = name
            
            root = find(account[1])
            for acc in account[2:]:
                parent[find(acc)] = root
                
        groups = defaultdict(list)
        for email in parent:
            root = parent[find(email)]
            groups[root].append(email)
        
        res = []
        for r, e in groups.items():
            name = owner[r]
            res.append([name] + sorted(groups[r]))
        
        return res

                    

