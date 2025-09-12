class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        in_node = defaultdict(list)
        out_node = defaultdict(list)

        for x, y in edges:
            in_node[y].append(x)
            out_node[x].append(y)
        
        print(in_node)

        # in case a node has two parents
        candidate1 = candidate2 = None
        for child, parents in in_node.items():
            if len(parents) == 2:
                candidate1 = [parents[0], child] 
                candidate2 = [parents[1], child] 
                break  

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            X, Y = find(x), find(y)
            if X != Y:
                parent[Y] = X
                return True
            return False

        for root, children in out_node.items():
            for child in children:
                if candidate2 and [root, child] == candidate2:
                    continue  
                if not union(root, child):
                    #cycle found and we skipped candidate2, so candidate1 must be a bad one
                    if candidate1:
                        return candidate1 
                    return [root, child]  

        #no cycle was found (cuz we skipped candidate2) so candidate2 must be the bad one
        if candidate2:
            return candidate2
