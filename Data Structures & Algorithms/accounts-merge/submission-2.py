class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        par = {}
        #每个邮箱的父节点都是自己
        for account in accounts:
            for email in account[1:]:
                par[email] = email

        def find(x):
            while x != par[x]:
                x = par[x]
            return par[x]

        def union(x,y):
            root1, root2 = find(x), find(y)
            par[root1] = root2

        #每组邮箱都建立父子关系，a-b,b-c,c-c
        for account in accounts:
            first_email = account[1]
            for email in account[2:]:
                union(first_email,email)
        
        #-----
        #找到根节点root，把属于一组email合并
        groups = defaultdict(list)
        for email in par:
            root = find(email)
            groups[root].append(email)

        #记录每个邮箱对应的姓名，后续查找root邮箱对应的姓名，只会出现一个姓名
        email_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
        
        #root对应的name，对应的一组group
        res = []
        for root, emails in groups.items():
            name = email_to_name[root]
            res.append([name]+sorted(emails)) #list+list合并

        return res



        

        
        

            
            

            
