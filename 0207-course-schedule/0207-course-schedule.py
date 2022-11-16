class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: [] for i in range(numCourses)}
        for prereq in prerequisites:
            prereqs[prereq[0]].append(prereq[1])
        
        def dfs(node, visited):
            if node in outer:
                return
            
            for neighNode in prereqs[node]:
                if neighNode in visited:
                    return False
                visited.add(neighNode)
                if dfs(neighNode, visited) == False:
                    return False
                visited.remove(neighNode)
        
        outer = set()
        for node in range(numCourses):
            curr_visited = set()
            if dfs(node, curr_visited) == False:
                return False
            outer.add(node)
        
        return True
        