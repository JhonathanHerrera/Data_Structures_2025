class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        prereq = defaultdict(list)
        visited = set()
        res = []

        for curr, pre in prerequisites:
            prereq[curr].append(pre)

        def dfs(course):
            if course in visited:
                return False
            if course in res:
                return True
        
            visited.add(course)            
            for x in prereq[course]:
                if not dfs(x): return False
            res.append(course)
            visited.remove(course)
      
            return True

        for i in range(numCourses):
            if not dfs(i): return []
        
        return res

        