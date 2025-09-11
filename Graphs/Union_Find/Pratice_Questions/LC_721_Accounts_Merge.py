class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        X,Y = self.find(x), self.find(y)
        if X != Y:
            self.parent[Y] = X
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                print("f")
                print(email)
                uf.union(first_email, email)
                email_to_name[email] = name
            
        print(uf.parent)
        print(email_to_name)

        # group emails by their root
        groups = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            groups[root].append(email)

        #format output
        res = []
        for root, emails in groups.items():
            print(emails)
            res.append([email_to_name[root]] + sorted(emails))
        return res

        