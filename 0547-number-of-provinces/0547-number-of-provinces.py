class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = set()
        def dfs(city):
            visited.add(city)

            for i in range(n):
                if isConnected[city][i] == 1 and i not in visited:
                    dfs(i)
        provinces = 0
        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)

        return provinces

        