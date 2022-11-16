class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
            
        for i, j in prerequisites:
            graph[i].append(j)
        
        visiting = set()
        visited = set()
        courses = []
        
        def dfs(graph, course, visited):
            if course in visited:
                return
            
            visiting.add(course)
            
            for prereq in graph[course]:
                if prereq in visiting:
                    return False
                if dfs(graph, prereq, visited) == False:
                    return False
                
            visiting.remove(course)
            visited.add(course)
            courses.append(course)
        
        for course in range(numCourses):
            if dfs(graph, course, visited) == False:
                return []
        
        return courses
            
        
#         for course in graph:
#             if dfs(graph, course, visited) == False:
#                 return []
            
#         for course in graph:
#             if course not in visited:
#                 visited.add(course)
#                 courses.append(course)
                
#         return courses