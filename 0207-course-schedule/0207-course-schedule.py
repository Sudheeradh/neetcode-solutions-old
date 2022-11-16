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
    
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         graph = {}
#         for i in range(numCourses):
#             graph[i] = []
            
#         for i, j in prerequisites:
#             graph[i].append(j)
        
#         visiting = set()
#         visited = set()
        
#         def dfs(graph, course, visited):
#             if course in visited:
#                 return
            
#             visiting.add(course)
            
#             for prereq in graph[course]:
#                 if prereq in visiting:
#                     return False
#                 if dfs(graph, prereq, visited) == False:
#                     return False
                
#             visiting.remove(course)
#             visited.add(course)
        
#         for course in graph:
#             if dfs(graph, course, visited) == False:
#                 return False
        
#         return True
        