class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        owner = {}
        
        
        
        def find(a):
            while parent[a] != a:
                a = parent[a]
            return parent[a]

        #每个邮箱先创建自己为根
        for account in accounts:
            name = account[0]
            for acc in account[1:]:
                if acc not in parent:
                    parent[acc] = acc
                    owner[acc] = name
            
            #每个账号的根挂到第一个的根的根上
            root = find(account[1])
            for acc in account[2:]:
                parent[find(acc)] = root

        #检查邮箱每个，根是否相同，挂在一起；     
        groups = defaultdict(list)
        for email in parent:
            root = parent[find(email)]
            groups[root].append(email)
        
        #同样根的邮箱合并，并加上名字；
        res = []
        for r, e in groups.items():
            name = owner[r]
            res.append([name] + sorted(groups[r]))
        
        return res

                    

