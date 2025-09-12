class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = defaultdict(list)
       
        visited = set()
        for course, pre in prerequisites:
            preMap[course].append(pre)

        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            visited.add(course)
            for crs in preMap[course]:
                if not dfs(crs): return False
            visited.remove(course)
            preMap[course] = []
            return True
            

        for i in range(numCourses):
            if not dfs(i): return False
        return True
            