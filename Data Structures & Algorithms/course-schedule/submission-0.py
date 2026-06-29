class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prereqs -> list of lists: prereq[2] = [a, b] :
        # means that u must take course b to take course a
        #  
        # pair [0, 1] -> course 1 is prereq to course 0
        # numCourses is total # of courses u r req. to take labeled from '0' to 'numCourses - 1'
        # 
        # return true if we can finish all courses, else return false
        # 
        # ex 1: numCourses = 2, prereqs = [[0, 1]] -> output is "true"
        #       why: we take course 1 then course 0
        # 
        # ex 2: numCourses = 2, prereqs = [[0, 1], [1, 0]] -> output is "false"
        #       why: must take 1 to take 0 and vice versa, so neither can ever be taken, impossible
        # 
        # 

        # loop through prereqs -> prereq[i] as i increases
        # since prereq[i] has length == 2, create a hasPrereq dict

        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finish == numCourses


